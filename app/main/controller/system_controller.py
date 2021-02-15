from flask import request
from flask_restx import Resource

from ..util.dto import SystemDto
from ..service.system_service import get_system_info, do_system_action, get_cpu_info, get_disk_info, get_mem_info, get_processes

api = SystemDto.api

_system = SystemDto.system
_action = SystemDto.action
_cpu = SystemDto.cpu_fields
_mem = SystemDto.mem_fields
_disk = SystemDto.disk_fields
_processes = SystemDto.processes_fields


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

@api.route('/mem')
class Mem(Resource):
    @api.doc('memory_information')
    @api.marshal_with(_mem, envelope='data')
    def get(self):
        return get_mem_info()


@api.route('/processes')
class Processes(Resource):
    @api.doc('processes_information')
    @api.marshal_with(_processes, envelope='data')
    def get(self):
        return get_processes()
