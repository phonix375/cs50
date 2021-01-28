from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from app import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'


class contract(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    body = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),
        nullable=False)
    def __repr__(self):
        return f"title {self.title}, user id {self.user_id} , body {self.body}"




class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text(), unique=True, nullable=False)
    email = db.Column(db.Text(), unique=True, nullable=False)
    password = db.Column(db.Text(),unique=True, nullable=False)

    def __repr__(self):
        return f"user name:{self.username}, email : {self.email}"



class link(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    contracts_id = db.Column(db.Text, nullable=False, default='[]')
    email = db.Column(db.Text, nullable=False)
    link_hash = db.Column(db.Text(),unique=True, nullable=False)

    def __repr__(self):
        return f"id {self.id}, Contracts {self.contracts_id} , emails {self.email}, link hash {self.link_hash}"

