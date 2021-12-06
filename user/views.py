from flask import Blueprint, render_template
from user.forms import LoginForm


users_blueprint = Blueprint('users', __name__, template_folder='templates')


@users_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm

    return render_template('login.html', form=form)

