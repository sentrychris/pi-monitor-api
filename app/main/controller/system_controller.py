from flask_restplus import Resource

from ..util.dto import SystemDto
from ..service.system_service import get_system_info

api = SystemDto.api


@api.route('/')
class System(Resource):
    @api.doc('system_information')
    def get(self):
        return get_system_info()
