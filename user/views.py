from flask import Blueprint, render_template, request, redirect, url_for, session
from user.forms import RegisterForm, LoginForm
from app import home, db
from models import User

users_blueprint = Blueprint('users', __name__, template_folder='Templates')


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


@users_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        print(user.email)
        email = request.form.get('email')
        print(email)
        return home()

    return render_template('login.html', form=form)
