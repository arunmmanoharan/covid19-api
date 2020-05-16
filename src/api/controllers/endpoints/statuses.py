import logging

from flask import request
from flask_restx import Resource
from src.api import api
from src.api.controllers.serializers import quarantine_status, covid_status, test_result_status

log = logging.getLogger(__name__)

ns = api.namespace('status', description='Operations related to statuses')


@ns.route('/getQuarantineStatus')
@api.response(404, 'Endpoint not found.')
class GetAllQuarantineStatus(Resource):
    @api.marshal_with(quarantine_status)
    def get(self):
        return [{
            'id': 0,
            'Status': 'Healthy',
            'Color': 'Green'
        }, {
            'id': 1,
            'Status': 'Risk',
            'Color': 'Yellow'
        }, {
            'id': 2,
            'Status': 'High Risk',
            'Color': 'Red'
        }]


@ns.route('/getCovidStatus')
@api.response(404, 'Endpoint not found.')
class GetAllCovidStatus(Resource):
    @api.marshal_with(covid_status)
    def get(self):
        return [{
            'id': 0,
            'Status': 'Never Infected',
        }, {
            'id': 1,
            'Status': 'Infected',
        }, {
            'id': 2,
            'Status': 'Recovered',
        }]


@ns.route('/getTestResultStatus')
@api.response(404, 'Endpoint not found.')
class GetAllTestResultStatus(Resource):
    @api.marshal_with(test_result_status)
    def get(self):
        return [{
            'id': 0,
            'Status': 'Positive',
        }, {
            'id': 1,
            'Status': 'Negative',
        }]
