from flask_sqlalchemy import SQLAlchemy
from config import Configuration

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = Configuration.USER_TABLENAME
    id = db.Column('id', db.Integer, primary_key=True)
    username = db.Column('account_username', db.Unicode)
    password = db.Column('account_password', db.Unicode)
    email = db.Column('account_email', db.Unicode)
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
    title = db.Column('event_title', db.Unicode)
    venue = db.Column('event_venue', db.Unicode)
    time = db.Column('event_date', db.DATE)
    details = db.Column('event_description', db.Unicode)

    def __init__(self, i_title, i_time, i_venue, i_details):
        self.title = i_title
        self.venue = i_venue
        self.time = i_time
        self.details = i_details
