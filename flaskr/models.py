from flaskr import db, login
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True, nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))

    entry = db.relationship('Entry', backref='author')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class Entry(db.Model):
    id =  db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False, default=datetime.now())
    author_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)
    mood_rate = db.Column(db.Integer, nullable=False)
    title = db.Column(db.Text)
    journal = db.Column(db.Text)

    author = db.relationship('User', backref=db.backref('entries', lazy=True))

    def __init__(self, mood_rate, title, journal, author):
        self.mood_rate = mood_rate
        self.title = title
        self.journal = journal
        self.author = author

    def __repr__(self):
        return '<Entry {}>'.format(self.journal[:30])

#db.create_all()
