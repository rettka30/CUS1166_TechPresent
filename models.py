from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class History (db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    message = db.Column('message', db.String(140))
