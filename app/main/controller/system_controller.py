from flask import request
from flask_restx import Resource

from ..util.dto import SystemDto
from ..service.system_service import get_system_info, do_system_action, get_cpu_info, get_disk_info, get_processes
from ..service.fan_service import get_fan, set_fan

api = SystemDto.api

_system = SystemDto.system
_action = SystemDto.action
_cpu = SystemDto.cpu_fields
_disk = SystemDto.disk_fields
_processes = SystemDto.processes_fields
_fan = SystemDto.fan


@api.route('/')
class System(Resource):
    @api.doc('system_information')
    @api.marshal_with(_system, envelope='data')
    def get(self):
        return get_system_info()

    @api.doc('system_action_information')
    @api.expect(_action, validate=True)
    def post(self):
        data = request.json
        return do_system_action(data=data)


@api.route('/cpu')
class Cpu(Resource):
    @api.doc('cpu_information')
    @api.marshal_with(_cpu, envelope='data')
    def get(self):
        return get_cpu_info()


@api.route('/disk')
class Disk(Resource):
    @api.doc('disk_information')
    @api.marshal_with(_disk, envelope='data')
    def get(self):
        return get_disk_info()


@api.route('/processes')
class Processes(Resource):
    @api.doc('processes_information')
    @api.marshal_with(_processes, envelope='data')
    def get(self):
        return get_processes()


@api.route('/fan')
class Fan(Resource):
    @api.doc('fan_information')
    def get(self):
        return get_fan()

    @api.doc('fan_action_information')    
    @api.expect(_fan, validate=True)
    def post(self):
        data = request.json

        return set_fan(data['status'])
