from flask_restplus import Resource

from ..util.dto import NetworkDto
from ..service.network_service import get_network_info

api = NetworkDto.api


@api.route('/')
class System(Resource):
    @api.doc('network_information')
    def get(self):
        return get_network_info()
