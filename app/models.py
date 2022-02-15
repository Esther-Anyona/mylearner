from . import db
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin, db.Model):
    __tablename__='users'
    id = db.Column(db.Integer, primary_key=True)
    username = db. Column(db.String(255), unique=True, nullable=False)
    email = db. Column(db.String(255), unique=True, nullable=False)
    profile_pic_path = db.Column(db.String(255), nullable=False, default='default.jpg')
    password_hash = db.Column(db.String(255), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)
    bio = db.Column(db.Text)
    comments = db.relationship('Comment',backref='author',lazy='dynamic')


    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)


    def __repr__(self):
        return f"User{self.username}"


class Post(db.Model):
    __tablename__='posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    user_id =db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    comments = db.relationship('Comment',backref='post',lazy='dynamic')
    def __repr__(self):
        return f"User{self.title}"

class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.Text(),nullable = False)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'),nullable = False)
    post_id = db.Column(db.Integer,db.ForeignKey('posts.id'),nullable = False)

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls,post_id):
        comments = Comment.query.filter_by(post_id=post_id).all()

        return comments

    
    def __repr__(self):
        return f'comment:{self.comment}'