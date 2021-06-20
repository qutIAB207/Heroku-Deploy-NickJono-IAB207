from flask import Blueprint, render_template
from .models import User, Festival, Review, Booking

bp = Blueprint('main', __name__)


@bp.route('/')
def landing():
    festivals = Festival.query.all()
    festivals_length = Festival.query.count()
    return render_template('landing.html', festivals=festivals, festivals_length=festivals_length)


@bp.route('/festival/id=<festivalID>')
def festival(festivalID):
    festivals = Festival.query.filter_by(id=festival.festivalID).first()
    return render_template('festival.html', festivals=festivals)


@bp.route('/account')
def account():
    return render_template('account.html')


@bp.route('/event_creation')
def event_creation():
    return render_template('event_creation.html')
