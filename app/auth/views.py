from flask import render_template, redirect, request, url_for, flash
from . import auth
from ..models import User
from .. import db
from .forms import RegistrationForm, LoginForm
from flask_login import login_user,logout_user,login_required



@auth.route('auth/login',methods=['GET','POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email = login_form.email.data).first()

        if user is not None and user.verify_password(login_form.password.data):
            login_user(user,login_form.remember.data)
            return redirect(request.args.get('next') or url_for('main.home'))

        flash('Invalid username or Password')

    title = "Myblog login"


    return render_template('auth/login.html', login_form = login_form, title=title)

@auth.route('auth/register',methods = ["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data,password = form.password.data)
        db.session.add(user)
        db.session.commit()

        mail_message("Welcome to Myblog","email/welcome_user",user.email,user=user)
        title = "New Account"

        return redirect(url_for('auth.login'))
    return render_template('auth/register.html',registration_form = form)


@auth.route('auth/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.home"))