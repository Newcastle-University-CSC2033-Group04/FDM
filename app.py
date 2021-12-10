from flask import Flask, render_template, redirect, request
from flask_login import LoginManager
from user.forms import RegisterForm
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'LongAndRandomSecretKey'

db = SQLAlchemy(app)


@app.route('/')
def base():
    return redirect('home')


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/games')
def games():
    return render_template('games.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        print(request.form.get('username'))
        print(request.form.get('email'))
        print(request.form.get('password'))
        print(request.form.get('confirm password'))
        print(request.form.get('phone number'))
        return login()

    return render_template('register.html', form=form)


@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    login_manager = LoginManager()
    login_manager.login_view = 'users.login'
    login_manager.init_app(app)


    from models import User


    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))


    app.run(debug=True)