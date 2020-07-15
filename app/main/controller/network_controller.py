from flask_restx import Resource

from ..util.dto import NetworkDto
from ..service.network_service import get_network_info, stream_connection

api = NetworkDto.api


@api.route('/')
class System(Resource):
    @api.doc('network_information')
    def get(self):
        return get_network_info()

    @api.doc('Stream network connection statistics.')
    def stream(self):
        return stream_connection('wlan_0')
