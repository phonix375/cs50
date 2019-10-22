import os
import csv

from flask import Flask, render_template, request, session, redirect, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
app = Flask(__name__)
engine = create_engine(os.getenv("DATABASE_URL"),pool_size=20, max_overflow=100)
db = scoped_session(sessionmaker(bind=engine))



file = open('books.csv','r')
data = csv.reader(file)
for isbn, title, author, year in data :
    try :
        int(isbn)
        db.execute("INSERT INTO books (isbn, title, author, year) VALUES (:isbn, :title, :author, :year)",{'isbn': isbn, 'title': title, 'author':author, 'year' : year})
        print(isbn,title,author,year)
        db.commit()
    except:
        pass
