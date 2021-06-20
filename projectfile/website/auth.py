from projectfile.website.views import festival
from flask import (
    Blueprint, flash, render_template, request, url_for, redirect
)
from werkzeug.security import generate_password_hash, check_password_hash
from .models import Festival
from .forms import LoginForm, RegisterForm, CreateEventForm
from flask_login import login_user, login_required, logout_user
from flask_wtf import FlaskForm
from . import db


# create a blueprint
bp = Blueprint('auth', __name__, url_prefix='/templates')


@bp.route('/event_creation', methods=['GET', 'POST'])
def create():
    print(f'Method Type: {request.method}')
    event_form = CreateEventForm()

    if event_form.validate_on_submit():
        # event = Festival(
        # name=event_form.name.data,
        # artists=event_form.name.data

        # )
        # db.session.add(festival)
        # db.session.commit()
        print("Succussfully Created Event", "success")
        # return redirect(url_for('auth.create'))

    # return render_template("templates/event.creation.html", form=event_form)


# test

# this is the hint for a login function
# @bp.route('/login', methods=['GET', 'POST'])
# def authenticate(): #view function
#     print('In Login View function')
#     login_form = LoginForm()
#     error=None
#     if(login_form.validate_on_submit()==True):
#         user_name = login_form.user_name.data
#         password = login_form.password.data
#         u1 = User.query.filter_by(name=user_name).first()
#         if u1 is None:
#             error='Incorrect user name'
#         elif not check_password_hash(u1.password_hash, password): # takes the hash and password
#             error='Incorrect password'
#         if error is None:
#             login_user(u1)
#             nextp = request.args.get('next') #this gives the url from where the login page was accessed
#             print(nextp)
#             if next is None or not nextp.startswith('/'):
#                 return redirect(url_for('index'))
#             return redirect(nextp)
#         else:
#             flash(error)
#     return render_template('user.html', form=login_form, heading='Login')
