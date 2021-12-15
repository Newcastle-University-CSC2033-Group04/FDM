from flask import Blueprint, render_template, request, redirect, url_for
from user.forms import RegisterForm, LoginForm
from app import home

users_blueprint = Blueprint('users', __name__, template_folder='Templates')


@users_blueprint.route('/register')
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        print(request.form.get('username'))
        print(request.form.get('email'))
        print(request.form.get('password'))
        print(request.form.get('confirm password'))
        print(request.form.get('firstname'))
        print(request.form.get('lastname'))
        return redirect(url_for('user.login'))

    return render_template('register.html', form=form)


@users_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        email = request.form.get('email')
        print(email)
        return home()

    return render_template('login.html', form=form)

# TODO: previous code that was here, not sure what it does, but the above code works

# from flask import Blueprint, render_template, request
# from user.forms import LoginForm
#
# users_blueprint = Blueprint('user', __name__, template_folder='Templates')
#
#
# @users_blueprint.route('/login', methods=['GET', 'POST'])
# def login():
#     form = LoginForm
#
#     return render_template('login.html', form=form)
#
#
# @users_blueprint.route('/register')
# def register():
#     return render_template('register.html')
#
#
# @users_blueprint.route('/register', methods=['POST'])
# def register_post():
#     username = request.form.get('username')
#     print(username)
#
#     return login()
