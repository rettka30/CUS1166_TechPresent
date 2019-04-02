from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Subject(db.Model):
    __tablename__="subject"
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('subject', db.String(120))
    message = db.relationship('History', backref='subject', lazy=True)

    def add_message(self,message):
        # Notice that we set the foreign key for the passenger class.
        new_message = History(message=message, subject_id=self.id )
        db.session.add(message)
        db.session.commit()

class History (db.Model):
    __tablename__="histories"
    id = db.Column('id', db.Integer, primary_key=True)
    message = db.Column('message', db.String(140))
    subject_id = db.Column(db.Integer, db.ForeignKey('subject.id'), nullable=False)
