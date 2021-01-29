from flask import Flask, render_template, request, redirect, session, jsonify
from flask_sqlalchemy import SQLAlchemy
import urllib.parse
import uuid

from passlib.hash import sha256_crypt
import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg', 'gif'}


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
app.secret_key = os.urandom(24)

from models import User, contract, link

#check if upload file in allowed extensions
def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def main():
    if 'username' in session:
        return render_template('home.html', name=session['username'])
    else:
        return render_template('home.html', name='None')

@app.route('/upload_header', methods=['POST'])
def upload_header():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            return redirect('/settings')
        file = request.files['file']
        if file.filename == '':
            return render_template('error.html', message="the file name can't be empty")
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect('/')

@app.route('/settings')
def settings():
    if 'username' in session:
        return render_template('settings.html', name=session['username'])
    else:
        return render_template('error.html',message='Please login to view settings')

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        print('got the user name and password')
        user_search = User.query.filter_by(username=username).first()
        if user_search == None:
            return render_template("error.html", message='Wrong User name')
        elif not(sha256_crypt.verify(password, user_search.password)):
            return render_template("error.html", message='Wrong password')
        else:
            session['username'] = username
            return render_template("error.html", message='all is good')
    else:
        print('this is get')
    return render_template('login.html', name='None')


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'GET':
        return render_template("register.html", name='None')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')
        if User.query.filter_by(username=username).first() != None:
            return render_template('error.html', message='username alrady exist in the database')
        elif User.query.filter_by(email=email).first() != None:
            return render_template('error.html', message='this email alrady exist in our database')
        else:
            new_user = User(username=username, email=email, password = sha256_crypt.hash(password))
            db.session.add(new_user)
            db.session.commit()
            session['username'] = username
            return redirect('/')

@app.route('/logout', methods=['POST', 'GET'])
def logout():
    if 'username' not in session:
        return redirect('/')
    session.pop('username')
    return redirect('/')


@app.route('/My_Forms', methods=['GET'])
def My_Forms():
    user_id = User.query.filter_by(username=session['username']).first().id
    contracts = contract.query.filter_by(user_id=user_id).all()
    links = link.query.filter_by(user_id = user_id).all()
    return render_template('my_forms.html', contracts=contracts, links = links)


@app.route('/contract_save', methods=['POST'])
def form_save():
    #user_select = request.form.get('userName')
    form = request.form['form']
    title = request.form['title']
    user = User.query.filter_by(username=session['username']).first()
    Contract = contract(title=title , body=form, user_id = user.id )
    db.session.add(Contract)
    db.session.commit()
    return jsonify(form=form)


@app.route('/show_contract', methods=['GET'])
def show_contract():
    contract_id = request.args.get('id')
    new_contract = contract.query.filter_by(id=contract_id).first()
    return render_template('contract.html',contract = new_contract.body)


@app.route('/get_contract', methods=['POST'])
def get_contract():
    contract_id = request.form.get('id')
    new_contract = contract.query.filter_by(id=contract_id).first()
    return jsonify({
  "title": new_contract.title,
  "body": new_contract.body,
  "id": new_contract.id
})

@app.route('/delete_contract', methods=['POST'])
def delete_contract():
    print(request.form['id'])
    print(type(request.form['id']))


    db.session.delete(contract.query.filter_by(id=int(request.form['id'])).first())
    db.session.commit()
    return 'good'

@app.route('/edit_existing_contract', methods=['POST'])
def edit_existing_contract():

    form = request.form['form']
    title = request.form['title']
    form_id = request.form['id']
    user = User.query.filter_by(username=session['username']).first()
    Contract_new = contract.query.filter_by(id=form_id).first()
    Contract_new.body = form
    Contract_new.title = title
    db.session.add(Contract_new)
    db.session.commit()
    return 'good'



@app.route('/generate_link', methods=['POST'])
def generate_link():
    contracts = list(request.form['contracts'].split(','))
    email = request.form['email']
    user = User.query.filter_by(username = session['username']).first()
    new_link = link(user_id = str(user.id), email=email, contracts_id = str(contracts), link_hash = 'temp')
    x = uuid.uuid4()
    new_link.link_hash = x.hex
    db.session.add(new_link)
    db.session.commit()

    return ''' localhost:5000/sign/''' + str(new_link.link_hash)


@app.route('/sign/<link_info>', methods=['GET'])
def sign(link_info):
    print(link_info)
    link_request = link.query.filter_by(link_hash = link_info).first()
    print('''############################# database use #############################################''')
    print(link_request)
    if link_request == None:
        print('going into none')
        return render_template('error.html', message='Cant find the link')
    else:
        contracts = link_request.contracts_id
        contracts = contracts.replace("'","")
        contracts = contracts.strip("][").split(', ')
        print('''############################# database use #############################################''')
        print(contracts)
        list_of_contracts = []
        for i in contracts:
            temp_contract = contract.query.filter_by(id=i).first()
            list_of_contracts.append({'title':temp_contract.title,'body': temp_contract.body, 'id':temp_contract.id})
        print(list_of_contracts)


    return render_template('sign.html', content = list_of_contracts)

