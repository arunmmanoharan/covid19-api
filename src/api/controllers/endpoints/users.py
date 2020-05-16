import logging

from flask import request
from flask_restx import Resource, abort

from src.database import db
from src.request_validation import json_request
from src.api.controllers.controllers import create_new_person, update_test_result_status, update_person_contact
from src.api import api
from src.models.people_model import People
from src.api.controllers.serializers import people, test_result, person_meeting
from enum import IntEnum

log = logging.getLogger(__name__)

ns = api.namespace('users', description='Operations related to users')


class QuarantineStatusEnum(IntEnum):
    HEALTHY = 0
    RISK = 1
    HIGH_RISK = 2


class CovidStatusEnum(IntEnum):
    NEVER_INFECTED = 0
    INFECTED = 1
    RECOVERED = 2


class TestResultStatusEnum(IntEnum):
    POSITIVE = 0
    NEGATIVE = 1


@ns.route('/createNewUsers')
@api.response(404, 'Endpoint not found.')
class CreateNewPerson(Resource):

    @api.expect(people, validate=True)
    @api.response(204, 'Post successfully updated.')
    @json_request
    def post(self):
        """
        Creates a new user.
        """
        data = request.json
        create_new_person(data)
        return data, 200


@ns.route('/getUsers')
@api.response(404, 'Endpoint not found.')
class GetAllPeople(Resource):
    @api.marshal_with(people)
    def get(self):
        peopleData = People.query.all()
        return peopleData


@ns.route('/updateUserTestResultStatus')
@api.response(404, 'Endpoint not found.')
class UpdateUserTestResultStatus(Resource):

    @api.expect(test_result, validate=True)
    @api.response(204, 'Post successfully updated.')
    @json_request
    def post(self):
        """
        Updates the test result status of a user.
        """
        data = request.json
        PersonId = data.get('PersonId')
        TestResultStatus = data.get('TestResultStatus')
        person = People.query.filter_by(id=PersonId).first()
        if person.CurrentCovidStatus == CovidStatusEnum.NEVER_INFECTED and TestResultStatus == TestResultStatusEnum.NEGATIVE:
            abort(409, 'Person is not infected at all')
        if person.CurrentCovidStatus == CovidStatusEnum.INFECTED and TestResultStatus == TestResultStatusEnum.POSITIVE:
            abort(409, 'Person is already infected')
        if person.CurrentCovidStatus == CovidStatusEnum.RECOVERED:
            abort(409, "Person is recovered")

        if person.CurrentCovidStatus == CovidStatusEnum.INFECTED and TestResultStatus == TestResultStatusEnum.NEGATIVE:
            person.QuarantineStatus = QuarantineStatusEnum.RISK
            person.CurrentCovidStatus = CovidStatusEnum.RECOVERED
            person.UpdatedAt = db.func.now()
        if person.CurrentCovidStatus == CovidStatusEnum.NEVER_INFECTED and TestResultStatus == TestResultStatusEnum.POSITIVE:
            person.QuarantineStatus = QuarantineStatusEnum.HIGH_RISK
            person.CurrentCovidStatus = CovidStatusEnum.INFECTED
            person.UpdatedAt = db.func.now()
        db.session.commit()
        update_test_result_status(data)
        return data, 200


@ns.route('/updatePersonMeeting')
@api.response(404, 'Endpoint not found.')
class UpdatePersonMeetingStatus(Resource):

    @api.expect(person_meeting, validate=True)
    @api.response(204, 'Post successfully updated.')
    @json_request
    def post(self):
        """
        Updates the meeting status of a user.
        """
        data = request.json
        update_person_contact(data)
        return data, 200
