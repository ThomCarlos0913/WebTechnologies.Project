from flask import Flask, request, jsonify, url_for
from init_db import DbInitData
from models import *
import atexit
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = Configuration.SQLALCHEMY_DATABASE_URI
db.init_app(app)

# Validate entered info on login form
@app.route('/validate_account', methods=['GET'])
def validate_account():
    incoming_username = request.args.get('username', 0)
    incoming_password = request.args.get('password', 0)
    queried_account = User.query.filter(User.username == incoming_username).first()
    if queried_account:
        if queried_account.username == incoming_username and queried_account.password == incoming_password:
            #ENTER CODES HERE
            print('')
        else:
            #ENTER CODES HERE
            print('')
    return ""

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
                        password = s_password,
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
            'time': e.time,
            'details': e.details
        }
        list_events[e.id] = event

    return jsonify(list_events)

# General routines section
##########################

# Initialize database and db content
@app.before_first_request
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

def delete_db():
    with app.app_context():
        db.drop_all()
    print("\n --------------------------\n")
    print(" * Database connection teared down")
    print("\n --------------------------\n")

# Teardown database connection
atexit.register(delete_db)

if __name__ == '__main__':
    app.run()
