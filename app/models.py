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
    username = db. Column(db.String(30), unique=True, nullable=False)
    email = db. Column(db.String(150), unique=True, nullable=False)
    profile_pic_path = db.Column(db.String(50), nullable=False, default='default.jpg')
    password_hash = db.Column(db.String(70), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

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
    title = db.Column(db.String(120), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    user_id =db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return f"User{self.title}"