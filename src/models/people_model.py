# The examples in this file come from the Flask-SQLAlchemy documentation
# For more information take a look at:
# http://flask-sqlalchemy.pocoo.org/2.1/quickstart/#simple-relationships

from datetime import datetime

from src.database import db

class People(db.Model):
    __tablename__ = 'People'

    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String, nullable=False)
    Contact = db.Column(db.String, nullable=False)
    QuarantineStatus = db.Column(db.Integer, nullable=False, default=0)
    CurrentCovidStatus = db.Column(db.Integer, nullable=False, default=0)
    UpdatedAt = db.Column(db.DateTime, default=db.func.now())

    def __init__(self, Name, Contact):
        self.Name = Name
        self.Contact = Contact


    def __repr__(self):
        return '<Person %r>' % self.id


