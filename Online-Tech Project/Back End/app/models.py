from flask_sqlalchemy import SQLAlchemy
from config import Configuration

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = Configuration.USER_TABLENAME
    id = db.Column('id', db.Integer, primary_key=True)
    username = db.Column('account_username', db.Text)
    password = db.Column('account_password', db.Text)
    email = db.Column('account_email', db.Text)
    privelege = db.Column('account_privelege', db.Integer)

    def __init__(self, username, password, email, privelege):
        self.username = username
        self.password = password
        self.email = email
        self.privelege = privelege

# Event table template
class Event(db.Model):
    __tablename__ = Configuration.EVENT_TABLENAME
    id = db.Column('event_id', db.Integer, primary_key=True)
    title = db.Column('event_title', db.Text)
    venue = db.Column('event_venue', db.Text)
    time = db.Column('event_date', db.DATE)
    details = db.Column('event_description', db.Text)
    isPassed = db.Column('event_passed', db.Integer)

    def __init__(self, i_title, i_time, i_venue, i_details, i_passed):
        self.title = i_title
        self.venue = i_venue
        self.time = i_time
        self.details = i_details
        self.isPassed = i_passed

# Featued Event table template
class Featured(db.Model):
    __tablename__ = Configuration.FEATURED_TABLENAME
    id = db.Column('f_id', db.Integer, primary_key=True)
    title = db.Column('f_title', db.Text)
    venue = db.Column('f_venue', db.Text)
    time = db.Column('f_date', db.DATE)
    details = db.Column('f_description', db.Text)
    isPassed = db.Column('f_passed', db.Integer)

    def __init__(self, i_title, i_time, i_venue, i_details, i_passed):
        self.title = i_title
        self.venue = i_venue
        self.time = i_time
        self.details = i_details
        self.isPassed = i_passed

# User Events table template
class UserEvents(db.Model):
    __tablename__ = Configuration.USEREVENTS_TABLENAME
    id = db.Column('log_id', db.Integer, primary_key=True)
    user_id = db.Column('user_id', db.Integer)
    event_id = db.Column('event_id', db.Integer)
    title = db.Column('event_title', db.Text)
    venue = db.Column('event_venue', db.Text)
    time = db.Column('event_date', db.DATE)
    details = db.Column('event_description', db.Text)

    def __init__(self, u_id, e_id, i_title, i_time, i_venue, i_details):
        self.user_id = u_id
        self.event_id = e_id
        self.title = i_title
        self.venue = i_venue
        self.time = i_time
        self.details = i_details
