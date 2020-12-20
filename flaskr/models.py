from flaskr import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True, nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def get_password(self, password):
        return generate_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)

class Entry(db.Model):
    __tablename__ = 'entries'

    id =  db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False, default=datetime.now())
    # author_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)
    mood_rate = db.Column(db.Integer, nullable=False)
    journal = db.Column(db.Text)

    # author = db.relationship('User', backref=db.backref('entries', lazy=True))

    def __init__(self, mood_rate, journal):
        self.mood_rate = mood_rate
        self.journal = journal

    def __repr__(self):
        return '<Entry {}>'.format(self.journal[:30])

#db.create_all()
