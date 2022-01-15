"""
Contains the forms for user registration and log in.
Is referenced when setting up the forms for the html templates.
"""
import re
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError


# ensures that the field selected contains no restricted characters
def character_check(form, field):
    excluded_chars = "* ? ! ' ^ + % & / ( ) = } ] [ { $ # @ < >"
    for char in field.data:
        if char in excluded_chars:
            raise ValidationError(
                f"Character {char} is not allowed.")


# register form containing all the required input fields
class RegisterForm(FlaskForm):
    username = StringField(validators=[DataRequired()])
    email = StringField(validators=[DataRequired(), Email()])
    firstname = StringField(validators=[DataRequired(), character_check])
    lastname = StringField(validators=[DataRequired(), character_check])
    password = PasswordField(validators=[DataRequired(),
                                         Length(min=8, max=16,
                                                message="Password must be between 8 and 16 characters.")])
    confirm_password = PasswordField(validators=[DataRequired(),
                                                 EqualTo("password", message="Both password fields must be equal!")])
    submit = SubmitField()

    # ensures that the password is secure and contains an uppercase and lowercase letter,
    # a number and a special character
    def validate_password(self, password):
        pa = re.compile(r"(?=.*\d)(?=.*[A-Z])(?=.*[a-z])(?=.*\W)")
        if not pa.match(self.password.data):
            raise ValidationError("Password must contain at least: 1 digit, 1 special character,"
                                  " 1 lowercase and 1 uppercase letter.")


# login form containing all the required input fields
class LoginForm(FlaskForm):
    email = StringField(validators=[DataRequired(), Email()])
    password = PasswordField(validators=[DataRequired()])
    submit = SubmitField()


# input fields for the second game
class GameTwoForm(FlaskForm):
    answer1 = StringField()
    answer2 = StringField()
    answer3 = StringField()
    answer4 = StringField()
    answer5 = StringField()
    submit = SubmitField()
