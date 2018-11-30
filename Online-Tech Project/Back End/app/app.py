from flask import Flask, request, jsonify, url_for
from models import *

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
                      i_details = e_details)
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

if __name__ == '__main__':
    app.run()
