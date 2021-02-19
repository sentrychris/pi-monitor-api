from flask_restx import Resource

from app.main.service.network_service import *
from app.main.representation.network import NetworkRepresentation
from app.main.decorator.auth_decorator import token_required

api = NetworkRepresentation.api
_network = NetworkRepresentation.network
_ping = NetworkRepresentation.ping
_wifi = NetworkRepresentation.wifi
_speed = NetworkRepresentation.speed


@api.route('/')
class Network(Resource):
    @token_required
    @api.doc('network_information')
    @api.marshal_with(_network, envelope='data')
    def get(self):
        return get_network_info()


@api.route('/ping')
class NetworkPing(Resource):
    @api.doc('network_ping_information')
    @api.marshal_with(_ping)
    def get(self):
        return get_network_status()


@api.route('/interfaces')
class NetworkInterfaces(Resource):
    @token_required
    @api.doc('network_interfaces_information')
    def get(self):
        return get_interfaces()


@api.route('/wifi')
class NetworkWifi(Resource):
    @token_required
    @api.doc('network_wifi_information')
    @api.marshal_with(_wifi, envelope='data')
    def get(self):
        return get_wifi_info()


@api.route('/wifi/speed')
class NetworkWifiSpeed(Resource):
    @token_required
    @api.doc('network_wifi_speed_information')
    @api.marshal_with(_speed, envelope='data')
    def get(self):
        return get_wifi_speed()
