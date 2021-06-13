from . import db


class User(db.Model):
    __tablename__ = 'users'  # good practice to specify table name
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True, unique=True, nullable=False)
    emailid = db.Column(db.String(100), index=True, nullable=False)
    # password is never stored in the DB, an encrypted password is stored
    # the storage should be at least 255 chars long
    password_hash = db.Column(db.String(255), nullable=False)


class Event(db.model):
    _tablename__ = 'events'
    festivalID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True, unique=True, nullable=False)
    venue = db.Column(db.String(100), index=True, nullable=False)
    genre = db.Column(db.String(100), nullable=False)
    artists = db.Column(db.String(300),  nullable=False)
    date = db.Column(db.datetime.date(), nullable=False)
    time = db.Column(db.datetime.time(), nullable=False)
    status = db.Column(db.String(100), nullable=False)
    ticket_availability = db.Column(db.String(100), nullable=False)
