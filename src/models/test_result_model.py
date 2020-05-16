# The examples in this file come from the Flask-SQLAlchemy documentation
# For more information take a look at:
# http://flask-sqlalchemy.pocoo.org/2.1/quickstart/#simple-relationships

from datetime import datetime

from src.database import db


class TestResultModel(db.Model):
    __tablename__ = 'TestResult'

    id = db.Column(db.Integer, primary_key=True)
    PersonId = db.Column(db.Integer, nullable=False)
    TestResult = db.Column(db.Integer, nullable=False)
    TestTakenDate = db.Column(db.DateTime, nullable=False)
    CreatedAt = db.Column(db.DateTime, default=db.func.now())

    def __init__(self, PersonId, TestResult, TestTakenDate):
        self.PersonId = PersonId
        self.TestResult = TestResult
        self.TestTakenDate = TestTakenDate

    def __repr__(self):
        return '<TestResult %r>' % self.TestResult
