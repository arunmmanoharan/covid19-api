# The examples in this file come from the Flask-SQLAlchemy documentation
# For more information take a look at:
# http://flask-sqlalchemy.pocoo.org/2.1/quickstart/#simple-relationships

from datetime import datetime

from src.database import db


class MetPerson(db.Model):
    __tablename__ = 'PersonMeeting'

    PersonId = db.Column(db.Integer, db.ForeignKey('People.id'), primary_key=True, nullable=False)
    MeetingId = db.Column(db.Integer, db.ForeignKey('Meeting.id'), primary_key=True, nullable=False)
    MetPersonId = db.Column(db.Integer, nullable=False)
    CreatedAt = db.Column(db.DateTime, default=db.func.now())

    db.UniqueConstraint('PersonId', 'MetPersonId')

    def __init__(self, PersonId, MetPersonId, CreatedAt, MeetingId):
        self.PersonId = PersonId
        self.MetPersonId = MetPersonId
        self.CreatedAt = CreatedAt
        self.MeetingId = MeetingId

    def __repr__(self):
        return '<MetPersonId %r>' % self.MetPersonId
