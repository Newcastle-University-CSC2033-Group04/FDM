"""
Handles user registration, login and logout.
Each function uses a form for user.forms, takes input from the user, verifies it (if needed)
and stores this data in the database.
"""
from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import login_user, logout_user, login_required
from datetime import datetime
from user.forms import RegisterForm, LoginForm
from app import home, db
from models import User
from werkzeug.security import check_password_hash

# creates a blueprint to be used when running the app
users_blueprint = Blueprint('users', __name__, template_folder='Templates')


# register form for the user. Takes input from the user, stores it in the database,
# and redirects user to the appropriate page.
@users_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        new_user = User(username=form.username.data,
                        email=form.email.data,
                        password=form.password.data,
                        first_name=form.firstname.data,
                        last_name=form.lastname.data)
        db.session.add(new_user)
        db.session.commit()
        return login()

    return render_template('register.html', form=form)


# login form. Takes input and validates the password. User is redirected
# to the appropriate page.
@users_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        # gets the user from the database with matching email
        user = User.query.filter_by(email=form.email.data).first()

        # checks if input password hash matches the hash in the database
        if not user or not check_password_hash(user.password, form.password.data):
            flash("Email or password is incorrect")
            return render_template('login.html', form=form)

        # logs in the user
        login_user(user)
        # stores current log in time
        user.last_logged_in = user.current_log_in
        user.current_log_in = datetime.now()
        db.session.add(user)
        db.session.commit()
        return home()

    return render_template('login.html', form=form)


# logs out the  user.
@users_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))
