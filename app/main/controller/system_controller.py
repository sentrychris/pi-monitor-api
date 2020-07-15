from flask import request
from flask_restx import Resource

from ..util.dto import SystemDto
from ..service.system_service import get_system_info, do_system_action

api = SystemDto.api
_system = SystemDto.system

@api.route('/')
class System(Resource):
    @api.doc('system_information')
    def get(self):
        return get_system_info()

    @api.doc('Perform system shutdown or reboot.')
    @api.expect(_system, validate=True)
    def post(self):
        data = request.json
        return do_system_action(data=data)
