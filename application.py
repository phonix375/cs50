import os
import datetime


from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    own =  db.execute("SELECT * FROM own WHERE user_id = :id",id = session['user_id'])
    total = 0
    for i in own:
        i['price'] = lookup(i['symbol'])['price']
        i['total'] = float(lookup(i['symbol'])['price']) * i['shares']
        total += float(i['total'])
    total += float(db.execute("SELECT cash FROM users WHERE id = :id", id=session['user_id'])[0]['cash'])
    return render_template("index.html", stacks = own, cash = usd(db.execute("SELECT cash FROM users WHERE id = :id", id=session['user_id'])[0]['cash']), total = usd(total))


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "GET":
        return render_template("buy.html")
    else:
        symbol=request.form.get("Symbel")
        shares = request.form.get('shares')
        if symbol == '':
            return apology("please select stock symbol")
        elif shares == '':
            return apology("please select the number of shars")
        elif lookup(symbol) == None:
            return apology("Please select a valid symbol")
        res = lookup(symbol)
        price  = res['price']
        print(db.execute('SELECT cash FROM users WHERE id = :ida', ida=session["user_id"])[0]['cash'])
        print(price)
        if int(db.execute('SELECT cash FROM users WHERE id = :ida', ida=session["user_id"])[0]['cash']) < (int(price) * int(shares)):
            return apology("you don't have the money")
        else:
            date = datetime.datetime.now()
            cost = float(price) * float(shares)
            db.execute("UPDATE users SET cash=cash-:cost WHERE id=:id", cost=cost, id=session["user_id"]);
            # check if user have this stock
            if len(db.execute('SELECT * FROM own WHERE user_id = :id AND symbol = :symbol', id=session["user_id"], symbol =symbol) )>0:
                db.execute('UPDATE own SET shares = shares+ :shares WHERE user_id = :id AND symbol =:symbol ',shares =shares, id=session["user_id"], symbol =symbol)
            else:
                db.execute('INSERT INTO own (user_id, symbol, shares, name) VALUES ( :id,:symbol ,:shares, :name);',id=session["user_id"], symbol=symbol, shares=shares, name=res['name'] )
            db.execute('INSERT INTO transactions (user_id, shares, price, date, symbol) VALUES ( :id,:shares ,:price, :date, :symbol);',id=session["user_id"], shares=shares, price=cost, date= date, symbol = symbol)


    return redirect('/')


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    transactions = db.execute('SELECT * FROM transactions WHERE user_id = :id', id=session["user_id"])
    return render_template("history.html", transactions = transactions)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    "https://cloud-sse.iexapis.com/stable/stock/nflx/quote?token=API_KEY"
    if request.method == "GET":
        return render_template("quote.html")
    else:
        symbol = request.form.get('symbol')
        r = lookup(symbol)
        print(r)

        return render_template('quoted.html', stock=r)



@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "GET":
        return render_template("register.html")
    else:
        username = request.form.get("username")
        password = request.form.get("password")
        repassword = request.form.get("password-again")

        if (username == None):
            return apology("The Username can't be empty", code='sorry')
        elif (password != repassword):
            return apology("""The Password Don't matc""", code="sorry")
        elif (len(db.execute("SELECT * FROM users WHERE username = :user", user=username)) > 0):
            return apology("""This Username Is Taken""", code="sorry")

        db.execute("INSERT INTO users (username, hash) VALUES (:user, :hasha)", user=username, hasha = generate_password_hash(password))
        return redirect("/")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "GET":
        own = db.execute("SELECT * FROM own WHERE user_id = :id", id=session['user_id'])
        symbols = []
        for i in own:
            symbols.append(i['symbol'])
        return render_template("sell.html", symbols = symbols)
    else:
        symbol = request.form.get('stack')
        shares = request.form.get('shares')


    # check to see if the user provided a positive integer in the shares feld
    try:
        int(shares)
        if int(shares) < 0:
            return apology("the number must be positive")
    except ValueError:
        return apology("please enter a number")

    # check if the user have this stock
    own = db.execute("SELECT * FROM own WHERE user_id = :id AND symbol = :symbol", id=session['user_id'], symbol = symbol)
    if len(own) == 0:
        return apology("""you don't own this stock""")

    # check if the user have suficent number of this stock
    own = db.execute("SELECT shares FROM own WHERE user_id = :id AND symbol = :symbol", id=session["user_id"], symbol = symbol)
    if int(own[0]['shares']) < int(shares):
        return apology("you don't have sufficient amount to sell")

    price = float(lookup(symbol)['price'])
    db.execute("UPDATE own set shares=shares- :shares WHERE symbol = :symbol", shares=shares, symbol=symbol)
    db.execute("INSERT INTO transactions (user_id, shares, price, date, symbol) VALUES (:user_id, :shares, :price, :date, :symbol)", user_id = session['user_id'], shares='-'+str(shares), price =price*float(shares), date = datetime.datetime.now(),symbol = symbol)
    db.execute("UPDATE users set cash=cash+ :price WHERE id = :id", price=price*float(shares), id=session['user_id'])

    # check if the stock is at zero, delete it from the own table
    own = db.execute('SELECT * FROM own WHERE user_id = :id AND symbol = :symbol', id=session['user_id'], symbol = symbol)

    if own[0]['shares'] == 0:
        db.execute('DELETE FROM own WHERE user_id = :id AND symbol = :symbol', id=session['user_id'], symbol = symbol)

    return redirect("/")





def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)



@app.route("/add", methods=["GET", "POST"])
@login_required
def add():
        if request.method == "GET":
            return render_template('add.html')
        else:
            number = request.form.get('add')
            try:
                int(number)
                if int(number) < 0:
                    return apology("you can't add negative value")
            except ValueError:
                return apology("please enter a number")

        db.execute('UPDATE users SET cash = cash + :add WHERE id = :id', add = float(number), id=session["user_id"])
        return redirect('/')