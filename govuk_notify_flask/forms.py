from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo, Length

EMAILS = [('e389a7f6-fc65-4b32-9d85-ed067e726735', 'Hello World'),
          ('1e6a28c8-3555-4e10-897d-8d19ad058598', 'Reset Password')]

TEXTS = [('e1d9690c-2f40-4de0-8417-087f389b3e3f', 'Hello World')]


class EmailForm(FlaskForm):
    email_address = StringField('Email Address', validators=[DataRequired(), Email()])
    template = SelectField('Template', choices=EMAILS, validators=[DataRequired()])


class TextForm(FlaskForm):
    mobile_number = StringField('Mobile Number', validators=[DataRequired()])
    template = SelectField('Template', choices=TEXTS, validators=[DataRequired()])


class PasswordReset(FlaskForm):
    email_address = StringField('Email Address', validators=[DataRequired(), Email()])
    salutation = StringField('Salutation', validators=[DataRequired(), Length(min=2, max=4)])
    first_name = StringField('First Name', validators=[DataRequired()])
    surname = StringField('Surname', validators=[DataRequired()])
    password = PasswordField('New Password', validators=[DataRequired(),
                             EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Confirm     Password', validators=[DataRequired()])
