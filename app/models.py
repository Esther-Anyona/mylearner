from . import db
from datetime import datetime



class User(db.Model):
    __tablename__='users'
    id = db.Column(db.Integer, primary_key=True)
    username = db. Column(db.String(30), unique=True, nullable=False)
    email = db. Column(db.String(150), unique=True, nullable=False)
    profile_pic_path = db.Column(db.String(50), nullable=False, default='default.jpg')
    password_hash = db.Column(db.String(70), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User{self.username}"


class Post(db.Model):
    __tablename__='posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    user_id =db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return f"User{self.title}"