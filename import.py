import os
import csv

from flask import Flask, render_template, request, session, redirect, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
app = Flask(__name__)
engine = create_engine("postgres://lgfawvxjeajxee:e75711224c5ab06c3656a5506cd35917a4c0216c324d735c3c45aaca1bd8b05f@ec2-174-129-241-14.compute-1.amazonaws.com:5432/d34u0l6frujlo0")
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
