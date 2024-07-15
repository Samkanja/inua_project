from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, EqualTo, Length


class AdminRegistrationForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=2,max=30)])
    password = PasswordField("Password",validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')]
    )
    submit = SubmitField("Sign Up")


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")