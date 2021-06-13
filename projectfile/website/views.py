from flask import Blueprint, render_template

bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    return render_template('landing.html')


@bp.route('/festival')
def festival_func():
    return render_template('festival.html')
