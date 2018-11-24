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

if __name__ == '__main__':
    app.run()
