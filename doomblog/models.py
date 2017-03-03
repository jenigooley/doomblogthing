from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///doom.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    body = db.Column(db.Text)
    pub_date = db.Column(db.DateTime)

    lyric_id = db.Column(db.Integer, db.ForeignKey('lyric.id'))
    lyric = db.relationship('lyric',
        backref=db.backref('posts', lazy='dynamic'))

    def __init__(self, title, body, lyric, pub_date=None):
        self.title = title
        self.body = body
        if pub_date is None:
            pub_date = datetime.utcnow()
        self.pub_date = pub_date
        self.lyric = lyric

    def __repr__(self):
        return '<Post %r>' % self.title


class Lyric(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    band = db.Column(db.String(100))
    song = db.Column(db.String(100))
    words = db.Column(db.Text)

    def __init__(self, band, song, words):
        self.band = band
        self.song = song
        self.words = words

    def __repr__(self):
        return '<lyric %r>' % self.name

db.create_all()
