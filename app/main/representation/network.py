from flask_restx import Namespace, fields, marshal
from app.main.service.network_service import get_interfaces


class NetworkRepresentation:
    api = Namespace('network', description='system monitor network related operations')

    interface_fields = api.model('interface_fields', {
        "mb_sent": fields.Float(description='Megabytes sent'),
        "mb_received": fields.Float(description='Megabytes received'),
        "pk_sent": fields.Float(description='Packets sent'),
        "pk_received": fields.Float(description='Packets received'),
        "error_in": fields.Float(description='Errors in'),
        "error_out": fields.Float(description='Errors out'),
        "dropout": fields.Float(description='Dropout rate')
    })
    interfaces = dict()
    for addr in get_interfaces():
        interfaces[addr] = fields.Nested(interface_fields, description='Interface ' + addr)
    interfaces_fields = api.model('interfaces_fields', interfaces)

    ssh_fields = api.model('ssh_fields', {
        'local_port': fields.Integer(description='Local port'),
        'remote_ip': fields.String(description='Remote IP')
    })
    connections = api.model('connections_fields', {
        "ssh": fields.List(fields.Nested(ssh_fields), description='Remote SSH connections')
    })
    network = api.model('network', {
        'interfaces': fields.Nested(interfaces_fields, description='Network interfaces'),
        'connections': fields.Nested(connections, description='Connections')
    })

    ping = api.model('ping', {
        "status": fields.String(description='Network connection status'),
    })
    speed = api.model('speed', {
        "ping": fields.String(description='Ping'),
        "download": fields.String(description='Upload speed'),
        "upload": fields.String(description='Download speed')
    })
    wifi = api.model('wifi', {
        "name": fields.String(description='Wireless SSID'),
        "quality": fields.String(description='Wireless quality'),
        "channel": fields.String(description='Wireless channel'),
        "encryption": fields.String(description='Wireless encryption'),
        "address": fields.String(description='MAC address'),
        "signal": fields.String(description='Wireless signal')
    })