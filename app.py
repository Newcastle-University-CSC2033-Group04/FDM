from flask import Flask, render_template, redirect, request
from flask_login import LoginManager
from user.forms import RegisterForm
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# TODO: fixes the annoying error when running the app. To be changed when working with the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lottery.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'LongAndRandomSecretKey'

db = SQLAlchemy(app)


@app.route('/')
def base():
    return redirect('home')


# TODO: everything except base (and maybe home) to be moved out of this file
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/games')
def games():
    return render_template('games.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    # TODO: commented out for now, to be returned (?) when working with the login page
    # login_manager = LoginManager()
    # login_manager.login_view = 'users.login'
    # login_manager.init_app(app)

    from user.views import users_blueprint

    app.register_blueprint(users_blueprint)

    app.run(debug=True)
