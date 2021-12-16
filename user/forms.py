import re
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError


def character_check(form, field):
    excluded_chars = "* ? ! ' ^ + % & / ( ) = } ] [ { $ # @ < >"
    for char in field.data:
        if char in excluded_chars:
            raise ValidationError(
                f"Character {char} is not allowed.")


class RegisterForm(FlaskForm):  # register form containing all the input fields
    username = StringField(validators=[DataRequired()])
    email = StringField(validators=[DataRequired(), Email()])
    firstname = StringField(validators=[DataRequired(), character_check])
    lastname = StringField(validators=[DataRequired(), character_check])
    password = PasswordField(validators=[DataRequired(),
                                         Length(min=8, max=16, message='Password must be between 8 and 16 characters.')])
    confirm_password = PasswordField(validators=[DataRequired(),
                                                 EqualTo('password', message='Both password fields must be equal!')])
    submit = SubmitField()

    def validate_password(self, password):
        pa = re.compile(r'(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*\W)')
        if not pa.match(self.password.data):
            raise ValidationError("Password must contain at least: 1 digit, 1 special character,"
                                  " 1 lowercase and 1 uppercase letter.")


class LoginForm(FlaskForm):
    email = StringField(validators=[DataRequired(), Email(message="Please enter a valid email")])
    password = PasswordField(validators=[DataRequired()])
    submit = SubmitField()
