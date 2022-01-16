from flask import Blueprint, render_template
from flask_login import current_user, login_required
from app import db, games
from models import User, Scores
from tabulate import tabulate
import json
from user.forms import GameTwoForm
from random import shuffle

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


# questions for game two
questions = [['FDM _____ graduates, ex-forces personnel, etc, '
              'to become IT professionals.', 'trains'],
             ['How many high-profile clients worldwide do we '
              'partner with?', '200+'],
             ['Approximately, how many graduates do we employ '
              'each year?', '1000'],
             ['We have a median gender pay gap of ___%', '0'],
             ['In the Social Mobility Index, we are ranked as top ___ '
              'employers.', '50'],
             ['We are a _____, multi award-winning employer.', 'FTSE 250']]


@games_blueprint.route('/game2', methods=['GET', 'POST'])
@login_required
def game2():
    form = GameTwoForm()
    score = 0
    # if submit is pressed, checks all answers
    if form.validate_on_submit():
        score += 50 if form.answer1.data.lower() == questions[0][1] else 0
        score += 50 if form.answer2.data.lower() == questions[1][1] else 0
        score += 50 if form.answer3.data.lower() == questions[2][1] else 0
        score += 50 if form.answer4.data.lower() == questions[3][1] else 0
        score += 50 if form.answer5.data.lower() == questions[4][1] else 0
        return render_template("endPage2.html", score=score)
    else:
        # shuffles the questions once, once the page is loaded
        shuffle(questions)
    return render_template('game2.html', form=form,
                           q1=questions[0][0],
                           q2=questions[1][0],
                           q3=questions[2][0],
                           q4=questions[3][0],
                           q5=questions[4][0])


@games_blueprint.route('/game2Home')
@login_required
def game2Home():
    return render_template('game2Home.html')


@games_blueprint.route('/endPage')
@login_required
def endPage():
    return render_template('endPage.html')


@games_blueprint.route('/saveScore/<score>')
def saveScore(score):
    # gets the score data of the current user
    last_score = Scores.query.filter_by(user_id=current_user.id).first()
    # if user has no score in the database, adds new score
    if not last_score:
        new_score = Scores(user_id=current_user.id)
        new_score.game_1 = 0
        new_score.game_2 = score
        db.session.add(new_score)
    # if new score is greater than the last, it's stored in the database
    elif last_score.game_2 < int(score):
        last_score.game_2 = score

    db.session.commit()
    return render_template('games.html')


# stores user score to the database
@games_blueprint.route('/processScore/<string:user_score>', methods=['POST'])
def process_user_score(user_score):
    # gets data from the json file
    user_score = json.loads(user_score)

    # gets the score data of the current user
    last_score = Scores.query.filter_by(user_id=current_user.id).first()
    # if user has no score in the database, adds new score
    if not last_score:
        new_score = Scores(user_id=current_user.id)
        new_score.game_1 = user_score['score']
        new_score.game_2 = 0
        db.session.add(new_score)
    # if new score is greater than the last, it's stored in the database
    elif last_score.game_1 < int(user_score['score']):
        last_score.game_1 = user_score['score']

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
