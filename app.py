import sys
from flask import Flask, render_template, request
from flask_socketio import SocketIO, send, emit, join_room, leave_room
from flask_sqlalchemy import SQLAlchemy
from models import *
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
socketio = SocketIO(app)
db.init_app(app)

users = {}

@socketio.on('message')
def handleMessage(msg):
    print('Message: ' + str(msg))
    send(msg, broadcast=True)

@socketio.on('username', namespace='/private')
def receive_username(username):
    users[username] = request.sid
    print('Username added!')

@socketio.on('private_message', namespace='/private')
def private_message(payload):
    recipient_session_id = users[payload['username']]
    message = payload['message']

    emit('new_private_message', message, room=recipient_session_id)

# @socketio.on('message')
# def handleMessage(msg):
#     print('Message: ' + str(msg))
#     message = History(message=msg)
#     db.session.add(message)
#     db.session.commit()
#     send(msg, broadcast=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/private')
def private():
    return render_template("private.html")

# @app.route('/live')
# def live():
#     messages = History.query.all()
#     return render_template('better.html', messages=messages)

def main():
    if (len(sys.argv)==2):
        print(sys.argv)
        if sys.argv[1] == 'createdb':
            db.create_all()
    else:
        print("Run app using 'flask run")
        print("To create a database use 'python app.py createdb")

if __name__ == '__main__':
    with app.app_context():
        main()
    socketio.run(app)
