from flask_restx import Resource

from ..util.dto import NetworkDto
from ..service.network_service import get_network_info, get_network_status, get_wifi_info

api = NetworkDto.api
_ping = NetworkDto.ping
_wifi = NetworkDto.wifi


@api.route('/')
class Network(Resource):
    @api.doc('network_information')
    def get(self):
        return get_network_info()


@api.route('/ping')
class NetworkPing(Resource):
    @api.doc('Ping the network.')
    @api.marshal_with(_ping)
    def get(self):
        return get_network_status()


@api.route('/wifi')
class NetworkWifi(Resource):
    @api.doc('Get wifi information.')
    @api.marshal_with(_wifi, envelope='data')
    def get(self):
        return get_wifi_info()
