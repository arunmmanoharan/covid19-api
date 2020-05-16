from src.database import db
from src.models.people_model import People
from src.models.test_result_model import TestResultModel
from src.models.met_person_model import MetPerson
from src.models.meeting_model import Meeting


def create_new_person(data):
    Name = data.get('Name')
    Contact = data.get('Contact')
    people = People(Name, Contact)
    db.session.add(people)
    db.session.commit()


def update_test_result_status(data):
    PersonId = data.get('PersonId')
    TestTakenDate = data.get('TestTakenDate')
    TestResultStatus = data.get('TestResultStatus')
    test_result = TestResultModel(PersonId, TestResultStatus, TestTakenDate)
    db.session.add(test_result)
    db.session.commit()


def update_person_contact(data):
    PersonId = data.get('PersonId')
    MetPersonId = data.get('MetPersonId')
    MetPersonDate = data.get('MetPersonDate')
    meeting = Meeting(MetPersonDate)
    db.session.add(meeting)
    db.session.flush()
    meeting = Meeting.query.order_by(Meeting.id.desc()).first()
    if meeting.id is not None:
        meetingPerson = MetPerson(PersonId, MetPersonId, MetPersonDate, meeting.id)
        db.session.add(meetingPerson)
        db.session.commit()


def update_meeting(data):
    CreatedAt = data.get('MetPersonDate')
    meeting = Meeting(CreatedAt)
    db.session.add(meeting)
    db.session.commit()
