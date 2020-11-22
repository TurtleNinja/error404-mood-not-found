from flaskr import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True, nullable=False)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)

class Entry(db.Model):
    id =  db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)
    mood_rate = db.Column(db.Integer, nullable=False)
    journal = db.Column(db.Text)

    author = db.relationship('User', backref=db.backref('entries', lazy=True))

    def __repr__(self):
        return '<Entry {}>'.format(self.journal[:30])

