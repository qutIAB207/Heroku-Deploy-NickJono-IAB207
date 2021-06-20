
from typing import Text
from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField, SubmitField, StringField, PasswordField
from wtforms.validators import InputRequired, Length, Email, EqualTo
from wtforms.widgets import TextArea
from flask_wtf.file import FileField, FileRequired, FileAllowed


class CreateEventForm(FlaskForm):

    name = StringField("Name:", validators=[InputRequired('Please enter an Event name')])
    venue = StringField("Venue:", validators=[InputRequired('Please enter a Venue')])
    genre = StringField("Genre:", validators=[InputRequired('Please select a Genre')])
    artists = StringField("Artists:", validators=[InputRequired('Please enter Artists')])
    ##image = FileField(validators=[FileAllowed(photos, 'Image only!'), FileRequired('File was empty!')])
    date =  StringField("Date:", validators=[InputRequired('Please enter date')])
    

    submit = SubmitField('Create Event')


# creates the login information
class LoginForm(FlaskForm):
    user_name = StringField("User Name", validators=[
                            InputRequired('Enter user name')])
    password = PasswordField("Password", validators=[
                             InputRequired('Enter user password')])
    submit = SubmitField("Login")

 # this is the registration form


class RegisterForm(FlaskForm):
    user_name = StringField("User Name", validators=[InputRequired()])
    email_id = StringField("Email Address", validators=[
                           Email("Please enter a valid email")])

    # add buyer/seller - check if it is a buyer or seller hint : Use RequiredIf field

    # linking two fields - password should be equal to data entered in confirm
    password = PasswordField("Password", validators=[InputRequired(),
                                                     EqualTo('confirm', message="Passwords should match")])
    confirm = PasswordField("Confirm Password")

    # submit button
    submit = SubmitField("Register")


class ReviewForm(FlaskForm):
    user_name = StringField("User Name", validators=[InputRequired()])
    comment = TextAreaField("Write a comment: ", validators=[
                            InputRequired()], widget=TextArea())
    submit = SubmitField("Submit Review")
