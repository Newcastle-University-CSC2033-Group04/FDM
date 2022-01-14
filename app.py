"""
Main module of the program. Run this file to start the program.

Contains database setup, error handling, log in setup as well as references to the html templates.
"""
from flask import Flask, render_template, redirect
from flask_login import LoginManager, login_required
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from tabulate import tabulate

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


@app.route('/game1Home')
@login_required
def game1Home():
    return render_template('game1Home.html')


@app.route('/game1')
@login_required
def game1():
    return render_template('game1.html')


@app.route('/endPage')
@login_required
def endPage():
    return render_template('endPage.html')


@app.route('/leaderboard')
@login_required
def leaderboard():
    from models import Scores
    # queries all scores from the database and orders them by the sum of both scores
    all_scores = db.session.query(User.username, Scores.game_1, Scores.game_2, Scores.game_1 + Scores.game_2).where(
        User.id == Scores.user_id).order_by(Scores.game_1 + Scores.game_2.desc())
    scores = []

    # adds all the scores to a python list
    for score in all_scores:
        scores.append(list(score))

    # generates an html table using the list above
    headers = ('Username', 'Game one', 'Game two', 'Total')
    score_table = (tabulate(scores, headers, tablefmt='html'))

    # renders the leaderboard template with the scores table provided
    return render_template('leaderboard.html', score_table=score_table)


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

    app.register_blueprint(users_blueprint)

    app.run(debug=True)
