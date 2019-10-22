import os
import requests
from flask import Flask, render_template, request, session, redirect, url_for, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)


engine = create_engine(os.getenv("DATABASE_URL"),pool_size=20, max_overflow=100)
db = scoped_session(sessionmaker(bind=engine))
app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

@app.route("/")
def index():
    if 'name' not in session :
        return render_template("index.html", user = 'none')

    else :
        return render_template("index.html", user = str(session['name']))

@app.route("/register")
def register():

    return render_template('register.html', user='none')





@app.route("/check_login", methods=["POST"])
def check_login():
    user_name = request.form.get("user_name")
    password = request.form.get('password')
    if db.execute("SELECT * FROM users WHERE name = :name AND password = :password", {"name": user_name, "password": password}).rowcount == 0:
        return render_template('error.html', error='User name or Password is incorrect')
    else:
        user_id = db.execute("SELECT name FROM users WHERE name = :name",{'name': user_name}).first()
        session['name'] = user_name
        return  redirect('/search')

@app.route("/search")
def search():
    if 'name' not in session :
        return render_template('error.html', error = 'please log in ', user = 'none')
    try:
        name = str(session['name'])
        return render_template("search.html", user = name)

    except:
        return render_template('error.html', error='please log in to search', user='none')



@app.route("/logout", methods=['post','get'])
def logout():
    if 'name' in session :
        session.pop("name")
    return redirect('/')




@app.route('/add_user', methods=['POST'])
def add_user():
    user_name = request.form.get("user_name")
    password = request.form.get("password")
    email = request.form.get('email')
    full_name = request.form.get('full_name')
    if db.execute("SELECT * FROM users WHERE name = :name",{"name": user_name}).rowcount != 0:
        return render_template('error.html',error='user name alrady excest please select another')
    db.execute("INSERT INTO users (name, password, email, full_name) VALUES (:name, :password, :email, :full_name)", {'name':user_name, 'password':password, 'email':email, 'full_name':full_name})
    db.commit()
    return redirect('/')


@app.route('/search_resolts', methods=["POST"])
def search_resolts():
    if 'name' not in session :
        return render_template('error.html',error = 'please log in to search', user='none')

    serarch_by = request.form.get("search_by")
    search_for = request.form.get("search_for").title()
    if serarch_by == "ISBN":
        resolt = db.execute("SELECT * FROM books WHERE isbn LIKE :search_for ",{'search_for': '%'+str(search_for+'%')})
    elif serarch_by == 'Title':
        resolt = db.execute("SELECT * FROM books WHERE title LIKE :search_for ",{'search_for': '%'+str(search_for)+'%'})
    elif serarch_by == 'Author':
        resolt = db.execute("SELECT * FROM books WHERE author LIKE :search_for ",{'search_for': '%'+str(search_for)+'%'})
    elif serarch_by == 'Year' :
        resolt = db.execute("SELECT * FROM books WHERE year LIKE :search_for ",{'search_for': search_for})
    if resolt.fetchone()== None:
        return render_template('error.html', error='No search results found')
    return render_template('search_resolts.html', resolt= resolt)


@app.route("/book/<string:isbn>", methods=["GET","POST"])
def book(isbn):
    if 'name' not in session :
        return render_template('error.html', error = 'please log in ', user = 'none')
    book_info =db.execute('SELECT * FROM books WHERE isbn = :isbn ',{'isbn':isbn}).fetchone()
    res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": "87zWhiy6izGJsFbzbf0lsw", "isbns": book_info['isbn']})
    data = res.json()
    reviews = db.execute("SELECT * FROM reviews WHERE book = :id", {'id': book_info['id']})

    return render_template('book.html', res=data, isbn=book_info['isbn'],review= reviews, book_info = book_info)


@app.route('/add_review')
def add_review():
    if 'name' not in session :
        return render_template('error.html', error = 'please log in ', user = 'none')
    rating = request.args.get("review_rate")
    text = request.args.get("review_text")
    isbn = request.args.get("isbn")
    user = db.execute("SELECT * FROM users WHERE name = :user_name ",{'user_name': session['name']}).fetchone()
    book = db.execute("SELECT * FROM books WHERE isbn = :isbn ",{'isbn': isbn}).fetchone()
    book_reviews = db.execute("SELECT * FROM reviews WHERE book = :book_id AND user_id = :user_id",{'book_id':book['id'],'user_id':user['id']}).fetchone()

    if book_reviews != None :
        return render_template('error.html', error='you already reviewed this book')

    if user['full_name'] == '':
        if user['email'] == '':
            review_by = session['name']
        else:
            review_by = user['email']
    else :
        review_by = user['full_name']

    db.execute('INSERT INTO reviews (rating, review, book, user_id, user_name) VALUES (:rating, :review, :book, :user_id, :user_name)',
               {'rating': rating, 'review': text, 'book':book['id'],'user_id':user['id'],'user_name':review_by})

    db.commit()

    return redirect('/book/'+book['isbn'])

@app.route("/api/<string:isbn>")
def book_api(isbn):
    if db.execute('SELECT * FROM books WHERE isbn = :isbn',{'isbn':isbn}).rowcount == 0 :
        return jsonify(error=404 ), 404
    book = db.execute('SELECT * FROM books WHERE isbn = :isbn',{'isbn':isbn}).fetchone()
    res = requests.get("https://www.goodreads.com/book/review_counts.json",params={"key": "87zWhiy6izGJsFbzbf0lsw", "isbns": book['isbn']})
    data = res.json()
    return jsonify({"title": book['title'],"author": book['author'],"year": book['year'],"isbn": book['isbn'],"average_score": data['books'][0]['average_rating'], "review_count":data['books'][0]['ratings_count']})

