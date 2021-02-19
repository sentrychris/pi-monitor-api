from flask import request
from flask_restx import Resource

from app.main.service.system_service import *
from app.main.representation.system import SystemRepresentation
from app.main.util.decorator import token_required

api = SystemRepresentation.api

_system = SystemRepresentation.system
_action = SystemRepresentation.action
_cpu = SystemRepresentation.cpu_fields
_mem = SystemRepresentation.mem_fields
_disk = SystemRepresentation.disk_fields
_processes = SystemRepresentation.processes_fields


@api.route('/')
class System(Resource):
    @token_required
    @api.doc('system_information')
    @api.marshal_with(_system, envelope='data')
    def get(self):
        return get_system_info()

    @token_required
    @api.doc('system_action_information')
    @api.expect(_action, validate=True)
    def post(self):
        data = request.json
        return do_system_action(data=data)


@api.route('/cpu')
class Cpu(Resource):
    @token_required
    @api.doc('cpu_information')
    @api.marshal_with(_cpu, envelope='data')
    def get(self):
        return get_cpu_info()


@api.route('/disk')
class Disk(Resource):
    @token_required
    @api.doc('disk_information')
    @api.marshal_with(_disk, envelope='data')
    def get(self):
        return get_disk_info()


@api.route('/mem')
class Mem(Resource):
    @token_required
    @api.doc('memory_information')
    @api.marshal_with(_mem, envelope='data')
    def get(self):
        return get_mem_info()


@api.route('/processes')
class Processes(Resource):
    @token_required
    @api.doc('processes_information')
    @api.marshal_with(_processes, envelope='data')
    def get(self):
        return get_processes()
