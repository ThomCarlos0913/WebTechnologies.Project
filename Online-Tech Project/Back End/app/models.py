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
