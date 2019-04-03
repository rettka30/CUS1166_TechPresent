from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class History (db.Model):
    __tablename__="histories"
    id = db.Column('id', db.Integer, primary_key=True)
    message = db.Column('message', db.String(140))
