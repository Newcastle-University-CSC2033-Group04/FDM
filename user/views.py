from flask import Blueprint, render_template, request
from user.forms import LoginForm


users_blueprint = Blueprint('users', __name__, template_folder='templates')


@users_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm

    return render_template('login.html', form=form)

@users_blueprint.route('/register')
def register():
     return render_template('register.html')


@users_blueprint.route('/register', methods=['POST'])
def register_post():

    username = request.form.get('username')
    print(username)

    return login()