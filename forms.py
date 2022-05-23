from flask_wtf import FlaskForm
import email_validator
from wtforms import validators
from wtforms.fields import StringField,PasswordField,SubmitField,BooleanField,EmailField
from wtforms.validators import DataRequired,Length,EqualTo,Email

class RegistrationForm(FlaskForm):
    username=StringField('Username',validators=[DataRequired(),Length(min=2,max=20)])
    # email=StringField('Email',validators=[DataRequired(),Email()])
    email = EmailField('Email address', [validators.DataRequired(), validators.Email()])
    passward=PasswordField('Password',validators=[DataRequired()])
    confirm_passward=PasswordField('Confirm Passward',validators=[DataRequired(),EqualTo('passward')])
    submit=SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email=StringField('Email',validators=[DataRequired(),Email()])
    passward=PasswordField('Password',validators=[DataRequired()])
    remember=BooleanField('Remember Me')
    submit=SubmitField('Login')