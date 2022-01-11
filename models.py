from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash
from app import db


# connects the Users table to the code so data in the table can be accessed through
# requests in the code.
class User(db.Model, UserMixin):
    __tablename__ = 'Users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    registered_on = db.Column(db.DateTime, nullable=True)
    last_logged_in = db.Column(db.DateTime, nullable=True)
    current_log_in = db.Column(db.DateTime, nullable=True)

    def __init__(self, username, email, password, first_name, last_name):
        self.username = username
        self.password = generate_password_hash(password)
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.registered_on = datetime.now()
        self.last_logged_in = None
        self.current_log_in = None


class Scores(db.Model):
    __tablename__ = 'Scores'

    score_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)
    game_1 = db.Column(db.Integer, nullable=True)
    game_2 = db.Column(db.Integer, nullable=True)
    game_3 = db.Column(db.Integer, nullable=True)
    game_4 = db.Column(db.Integer, nullable=True)
    
    def __init__(self, score_id, user_id, game_1, game_2, game_3, game_4):
        self.score_id = score_id
        self.user_id = user_id
        self.game_1 = game_1
        self.game_2 = game_2
        self.game_3 = game_3
        self.game_4 = game_4
        