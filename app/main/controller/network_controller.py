from flask_restx import Resource

from ..util.dto import NetworkDto
from ..service.network_service import get_network_info, get_network_status, get_wifi_info, get_wifi_speed

api = NetworkDto.api

_network = NetworkDto.network
_ping = NetworkDto.ping
_wifi = NetworkDto.wifi
_speed = NetworkDto.speed_fields


@api.route('/')
class Network(Resource):
    @api.doc('network_information')
    @api.marshal_with(_network, envelope='data')
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
    @api.doc('network_wifi_information')
    @api.marshal_with(_wifi, envelope='data')
    def get(self):
        return get_wifi_info()


@api.route('/wifi/speed')
class NetworkWifiSpeed(Resource):
    @api.doc('network_wifi_speed_information')
    @api.marshal_with(_speed, envelope='data')
    def get(self):
        return get_wifi_speed()
