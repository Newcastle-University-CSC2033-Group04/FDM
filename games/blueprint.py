from flask import Blueprint, render_template
from flask_login import current_user, login_required
from app import db
from models import User, Scores
from tabulate import tabulate
import json

# creates a blueprint to be used when running the app
games_blueprint = Blueprint('games', __name__, template_folder='Templates')


@games_blueprint.route('/game1Home')
@login_required
def game1Home():
    return render_template('game1Home.html')


@games_blueprint.route('/game1')
@login_required
def game1():
    return render_template('game1.html')


@games_blueprint.route('/game2')
@login_required
def game2():
    return render_template('game2.html')


@games_blueprint.route('/endPage')
@login_required
def endPage():
    return render_template('endPage.html')


# stores user score to the database
@games_blueprint.route('/processScore/<string:user_score>', methods=['POST'])
def process_user_score(user_score):
    # gets data from the json file
    user_score = json.loads(user_score)
    # adds score to the database and saves it
    new_score = Scores(user_id=current_user.id)
    new_score.game_1 = user_score['score']
    new_score.game_2 = 0
    db.session.add(new_score)
    db.session.commit()
    return render_template('games.html')


@games_blueprint.route('/leaderboard')
@login_required
def leaderboard():
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
