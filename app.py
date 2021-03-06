"""
Main module of the program. Run this file to start the program.

Contains database setup, error handling, log in setup as well as references to the html templates.
"""
from flask import Flask, render_template, redirect
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

# database setup
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://csc2033_team04:Rush|Cam[Fun@' \
                                        '127.0.0.1:3333/csc2033_team04'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'LongAndRandomSecretKey'

db = SQLAlchemy(app)


# html template references
@app.route('/')
def base():
    return redirect('home')


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/games')
def games():
    return render_template('games.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


# Error handling
@app.errorhandler(400)
def bad_request(error):
    return render_template('400.html'), 400


@app.errorhandler(403)
def page_forbidden(error):
    return render_template('403.html'), 403


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500


@app.errorhandler(503)
def service_unavailable(error):
    return render_template('503.html'), 503


if __name__ == '__main__':
    # sets up the login manager required for the login to work
    login_manager = LoginManager()
    login_manager.login_view = 'users.login'
    login_manager.init_app(app)

    # cannot import at the top as it would cause a circular import error
    from models import User


    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))


    # sets up the blueprint from user.views with the app
    from user.views import users_blueprint
    from games.blueprint import games_blueprint

    app.register_blueprint(users_blueprint)
    app.register_blueprint(games_blueprint)

    app.run(debug=True)
