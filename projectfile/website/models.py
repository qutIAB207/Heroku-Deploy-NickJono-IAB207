from datetime import datetime
from . import db


class User(db.Model):
    __tablename__ = 'users'  # good practice to specify table name
    UserID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True, unique=True, nullable=False)
    emailid = db.Column(db.String(100), index=True, nullable=False)
    # password is never stored in the DB, an encrypted password is stored
    # the storage should be at least 255 chars long
    password_hash = db.Column(db.String(255), nullable=False)
    bookings = db.relationship('Booking', backref='user')


class Festival(db.Model):
    __tablename__ = 'festivals'
    festivalID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True, unique=True, nullable=False)
    venue = db.Column(db.String(100), index=True, nullable=False)
    genre = db.Column(db.String(100), nullable=False)
    artists = db.Column(db.String(300),  nullable=False)
    date = db.Column(db.String(300), nullable=False)
    #time = db.Column(db.Time(), nullable=False)
    reviews = db.relationship('Review', backref='festival')
    bookings = db.relationship('Booking', backref='festival')


class Review(db.Model):
    __tablename__ = 'reviews'
    reviewID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True, unique=True, nullable=False)
    text = db.Column(db.String(400), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())
    festivalID = db.Column(db.Integer, db.ForeignKey("festivals.festivalID"))


class Booking(db.Model):
    __tablename__ = 'bookings'
    bookingID = db.Column(db.Integer, primary_key=True, nullable=False)
    UserID = db.Column(db.Integer, db.ForeignKey("users.UserID"))
    festivalID = db.Column(db.Integer, db.ForeignKey("festivals.festivalID"))
    quantity = db.Column(db.Integer, primary_key=True, nullable=False)
