from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

'''
from wtforms.validators import Required, Email


class LoginForm(FlaskForm):
    username = StringField(validators=[Required(), Email()])
    password = PasswordField(validators=[Required()])
    submit = SubmitField()
'''


class RegisterForm(FlaskForm):
    email = StringField()
    username = StringField()
    password = PasswordField()
    confirm_password = PasswordField()
    firstname = StringField()
    lastname = StringField()
    submit = SubmitField()

