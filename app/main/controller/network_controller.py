import json
from flask_restx import Resource

from ..util.dto import NetworkDto
from ..service.network_service import get_network_info, stream_connection

api = NetworkDto.api


@api.route('/')
class Network(Resource):
    @api.doc('network_information')
    def get(self):
        return get_network_info()

@api.route('/stats')
class NetworkStats(Resource):
    @api.doc('Stream network connection statistics.')
    def get(self):
        return json.dumps(stream_connection(interface='wlan0'))
