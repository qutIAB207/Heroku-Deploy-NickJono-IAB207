from projectfile.website import forms
from flask import Blueprint, render_template, request
from .models import User, Festival, Review, Booking
from projectfile.main import db

bp = Blueprint('main', __name__)


@bp.route('/')
def landing():
    festivals = Festival.query.all()
    festivals_length = Festival.query.count()
    return render_template('landing.html', festivals=festivals, festivals_length=festivals_length)


@bp.route('/festival/id=<festivalID>')
def festival(festivalID):
    festivals = Festival.query.filter_by(festivalID=festivalID).first()
    reviews = Review.query.filter_by(festivalID=festivalID)
    return render_template('festival.html', festivals=festivals, reviews=reviews)


@bp.route('/account')
def account():
    return render_template('account.html')


@bp.route('/event_creation', methods=['GET', 'POST'])
def event_creation():
    print(f'Method Type: {request.method}')
    event_form = forms.CreateEventForm()

    if event_form.validate_on_submit():
        festival = Festival(
            name=event_form.name.data,
            artists=event_form.name.data
        )
        db.session.add(festival)
        db.session.commit()
        print("Successfully created event", "success")

    return render_template("event_creation.html", form=event_form)
