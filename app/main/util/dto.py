from flask_restx import Namespace, fields


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        'public_id': fields.String(description='user Identifier')
    })


class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password'),
    })


class SystemDto:
    api = Namespace('system', description='system monitor core related operations')
    system = api.model('system', {
        'action': fields.String(required=True, description='System shutdown/reboot')
    })


class NetworkDto:
    api = Namespace('network', description='system monitor network related operations')

    details_fields = api.model('details_fields', {
        "name": fields.String(required=True, description='Wireless SSID'),
        "quality": fields.String(required=True, description='Wireless quality'),
        "channel": fields.String(required=True, description='Wireless channel'),
        "encryption": fields.String(required=True, description='Wireless encryption'),
        "address": fields.String(required=True, description='MAC address'),
        "signal": fields.String(required=True, description='Wireless signal')
    })
    speed_fields = api.model('speed_fields', {
        "ping": fields.String(required=True, description='Ping'),
        "download": fields.String(required=True, description='Upload speed'),
        "upload": fields.String(required=True, description='Download speed')
    })
    wifi = api.model('network', {
        'details': fields.Nested(details_fields),
        'speed': fields.Nested(speed_fields)
    })

