from flask import Flask, request, jsonify, url_for
from init_db import DbInitData
from models import *
from werkzeug.security import generate_password_hash, check_password_hash

import click
from flask.cli import FlaskGroup
import jwt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = Configuration.SQLALCHEMY_DATABASE_URI
app.config['SECRET_KEY'] = 'groupionlinetech'
db.init_app(app)

# Validate entered info on login form
@app.route('/validate_account', methods=['GET'])
def validate_account():
    auth = request.authorization
    account = User.query.filter(User.username == auth.username).first()
    if account:
        if auth and auth.username == account.username and check_password_hash(account.password, auth.password):
            # create token
            token = jwt.encode({'id':account.id, 'user':account.username, 'exp':50000}, app.config['SECRET_KEY'])
            return jsonify({'code':'200','id': account.id, 'user':account.username, 'privelege':account.privelege})
    else:
        return 'Username or password is incorrect'
    return '500'

# Subscribe to an Event
@app.route('/subscribe_event', methods=['POST'])
def subscribe_event():
    payload = request.get_json()
    u_id = payload.get('u_id', None)
    ev_id = payload.get('e_id', None)
    e_name = payload.get('i_title', None)
    e_time = payload.get('i_time', None)
    e_location = payload.get('i_venue', None)
    e_details = payload.get('i_details', None)

    queried_account = UserEvents.query.filter(UserEvents.user_id == u_id, UserEvents.event_id == ev_id).all()
    if queried_account:
        return "500"

    sub_event = UserEvents(u_id = u_id,
                           e_id = ev_id,
                           i_title = e_name,
                           i_venue = e_location,
                           i_time = "2018-10-10",
                           i_details = e_details,)
    db.session.add(sub_event)
    db.session.commit()

    return '200'

# Unsubscribe to an event
@app.route('/unsubscribe_event', methods=['GET'])
def unsubscribe_event():
    ev_id = request.args.get('event_id', None)
    event = UserEvents.query.get(ev_id)
    db.session.delete(event)
    db.session.commit()
    return "200"

# Get subscribed events
@app.route('/get_my_events', methods=['GET'])
def get_my_events():
    u_id = request.args.get('user_id', 0)
    test = int(u_id)
    list_events = {}
    event = {}
    events = UserEvents.query.filter(UserEvents.user_id == u_id).all()
    for e in events:
        event = {
            'user_id': e.user_id,
            'title': e.title,
            'venue': e.venue,
            'time': str(e.time),
            'details': e.details
        }
        list_events[e.id] = event

    return jsonify(list_events)

# Register user
@app.route('/register_acount',methods=['POST'])
def register_account():
    payload = request.get_json()
    s_username = payload.get('s_user', None)
    s_password = payload.get('s_pass', None)
    s_email = payload.get('s_email', None)

    # Check if there is a valid username
    queried_account = User.query.filter(User.username == s_username).first()
    if queried_account:
        return "409"
    else:
        new_user = User(username = s_username,
                        password = generate_password_hash(s_password),
                        email = s_email,
                        privelege = 1)
        db.session.add(new_user)
        db.session.commit()
        return "200"

    return "500"

# Create event
@app.route('/create_event', methods=['POST'])
def create_event():
    payload = request.get_json()
    e_name = payload.get('event_title', None)
    e_time = payload.get('event_time', None)
    e_location = payload.get('event_location', None)
    e_details = payload.get('event_details', None)

    new_event = Event(i_title = e_name,
                      i_venue = e_location,
                      i_time = e_time,
                      i_details = e_details,
                      i_passed = 1)
    db.session.add(new_event)
    db.session.commit()
    return "200"

# Get all events
@app.route('/get_events', methods=['GET'])
def get_events():
    list_events = {}
    event = {}
    events = Event.query.all()
    for e in events:
        event = {
            'id': e.id,
            'title': e.title,
            'venue': e.venue,
            'time': e.time,
            'details': e.details
        }
        list_events[e.id] = event

    return jsonify(list_events)

# Update events
@app.route('/update_event', methods=['GET'])
def update_event():
    id = request.args.get('id', None)
    title = request.args.get('title', None)
    venue = request.args.get('venue', None)
    time = request.args.get('time', None)
    details = request.args.get('details', None)

    event = Event.query.get(id)
    event.title = title
    event.venue = venue
    event.time = time
    event.details = details

    db.session.commit()
    return "200"

# Update events
@app.route('/update_featured', methods=['GET'])
def update_featured():
    id = request.args.get('id', None)
    event = Event.query.get(id)
    current_featured = Featured.query.first()

    current_featured.title = event.title
    current_featured.venue = event.venue
    current_featured.time = event.time
    current_featured.details = event.details

    db.session.commit()
    return "200"

# Delete Event
@app.route('/delete_event', methods=['GET'])
def delete_event():
    id = request.args.get('id', None)
    event = Event.query.get(id)
    db.session.delete(event)
    db.session.commit()
    return "200"

# Get Passed Event
@app.route('/get_passed_events', methods=['GET'])
def get_passed_events():
    passed_event_dict = {}
    event = {}

    passed_events = Event.query.filter(Event.isPassed == 1).all()
    for e in passed_events:
        event = {
            'id': e.id,
            'title': e.title,
            'venue': e.venue,
            'time': e.time,
            'details': e.details
        }
        passed_event_dict[e.id] = event

    return jsonify(passed_event_dict)

# Get Featured Event
@app.route('/get_featured', methods=['GET'])
def get_featured():
    event = Featured.query.first()
    featured_event = {
        'id': event.id,
        'title': event.title,
        'venue': event.venue,
        'time': event.time,
        'details': event.details
    }

    return jsonify(featured_event)

# Get upcoming events
@app.route('/get_upcoming_event', methods=['GET'])
def get_upcoming_event():
    list_events = {}
    event = {}
    events = Event.query.filter(Event.isPassed == 0).all()
    for e in events:
        event = {
            'id': e.id,
            'title': e.title,
            'venue': e.venue,
            'time': str(e.time),
            'details': e.details
        }
        list_events[e.id] = event

    return jsonify(list_events)

# General routines section
##########################

@click.group(cls=FlaskGroup, create_app=lambda: app)
def cli():
    """Management script for the flask application."""

# Initialize database and db content
@cli.command('init_db')
def init_db():
    # Initialize tables
    db.create_all()

    # Fetch data from init_db
    db_data = DbInitData.fetch_data()

    # Insert and commit data in database
    for admin in db_data[0]:
        db.session.add(admin)
    for event in db_data[1]:
        db.session.add(event)
    db.session.add(db_data[2])

    db.session.commit()
    print("\n --------------------------\n")
    print(" * Admin accounts registered")
    print(" * Event details registered")
    print("\n --------------------------\n")

@cli.command('drop_db')
def delete_db():
    with app.app_context():
        db.drop_all()
    print("\n --------------------------\n")
    print(" * Database connection teared down")
    print("\n --------------------------\n")


if __name__ == '__main__':
    cli()
