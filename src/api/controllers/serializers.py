from flask_restx import fields
from src.api import api

people = api.model('People', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of a person'),
    'Name': fields.String(required=True, description='Name of the person'),
    'Contact': fields.String(required=True, description='Contact of the person'),
    'QuarantineStatus': fields.Integer(description='The Quarantine Status of a person'),
    'CurrentCovidStatus': fields.Integer(description='The Current Covid Status of a person'),
    'UpdatedAt': fields.DateTime(description='The date and time when the covid status is updated'),
})

person_meeting = api.model("Person meeting", {
    'PersonId': fields.Integer(description='The unique identifier of a person'),
    'MeetingId': fields.Integer(description='The unique identifier of a meeting'),
    'CreatedAt': fields.DateTime(description='The date and time when one person meets one another'),
    'MetPersonId': fields.Integer(description='The unique identifier of the met person'),
})

meeting = api.model('Meeting', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of a meeting'),
    'Date': fields.DateTime(description='The date and time at which the meeting is created'),
})

test_result = api.model('Test Result', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of a test result'),
    'PersonId': fields.Integer(description='The unique identifier of a person'),
    'TestResult': fields.Integer(description='The unique identifier of the test result'),
    'TestTakenDate': fields.DateTime(description='The test taken date'),
    'CreatedAt': fields.DateTime(description='The test taken date created time'),
})

quarantine_status = api.model('Quarantine Status', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of a Quarantine Status'),
    'Status': fields.String(readOnly=True, description='The value of a Quarantine Status'),
    'Color': fields.String(readOnly=True, description='The color of a Quarantine Status')
})

covid_status = api.model('COVID Status', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of a COVID Status'),
    'Status': fields.String(readOnly=True, description='The value of a COVID Status'),
})

test_result_status = api.model('COVID Status', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of a test result Status'),
    'Status': fields.String(readOnly=True, description='The value of a test result Status'),
})