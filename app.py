import sys
from flask import Flask, render_template, url_for, request
from flask_socketio import SocketIO, send, emit, join_room, leave_room
from flask_sqlalchemy import SQLAlchemy
from models import *
from config import Config

subjects = {}

app = Flask(__name__)
app.config.from_object(Config)
socketio = SocketIO(app)
db.init_app(app)

# @socketio.on('message')
# def handleMessage(msg):
#     print('Message: ' + str(msg))
#     send(msg, broadcast=True)

@socketio.on('message')
def handleMessage(msg):
    print('Message: ' + str(msg))
    message = History(message=msg)
    db.session.add(message)
    db.session.commit()
    send(msg, broadcast=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/live')
def live():
    messages = History.query.all()
    return render_template('better.html', messages=messages)

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
