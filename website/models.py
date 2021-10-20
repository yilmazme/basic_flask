from enum import unique
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Note(db.Model):
    __tablename__ = "notes"
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey("members.id"))

    def __init__(self, data, user_id):
        self.data = data
        self.user_id = user_id
        

class User(db.Model, UserMixin):
    __tablename__ = "members"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    name = db.Column(db.String(150))
    notes = db.relationship("Note")

    def __init__(self, email, password, name):
        self.email = email
        self.password = password
        self.name = name
     
        