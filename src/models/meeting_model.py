# The examples in this file come from the Flask-SQLAlchemy documentation
# For more information take a look at:
# http://flask-sqlalchemy.pocoo.org/2.1/quickstart/#simple-relationships

from datetime import datetime

from src.database import db


class Meeting(db.Model):
    __tablename__ = 'Meeting'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    Date = db.Column(db.DateTime, nullable=False)

    def __init__(self, Date):
        self.Date = Date

    def __repr__(self):
        return '<MeetingId %r>' % self.id
