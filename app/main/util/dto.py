from flask_restx import Namespace, fields, marshal
from ..service.network_service import get_interfaces


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
    action = api.model('system_action', {
        'action': fields.String(required=True, description='System shutdown/reboot')
    })

    cpu_fields = api.model('cpu_fields', {
        "usage": fields.Float(description='CPU usage'),
        "temp": fields.Float(description='CPU temperature'),
        "freq": fields.Float(description='CPU clock rate')
    })
    disk_fields = api.model('disk_fields', {
        "total": fields.Float(description='Disk total'),
        "used": fields.Float(description='Disk used'),
        "free": fields.Float(description='Disk free'),
        "percent": fields.Float(description='Disk used percent')
    })
    platform_fields = api.model('platform_fields', {
        "distro": fields.String(description="Current distribution"),
        "kernel": fields.String(description="Current kernel version"),
        "uptime": fields.String(description="System uptime")
    })
    processes_fields = api.model('processes_fields', {
        "pid": fields.Integer(description='Process ID'),
        "username": fields.String(description='Process Owner'),
        "name": fields.String(description='Process Name'),
        "mem": fields.Float(description='Process memory usage')
    })
    system = api.model('system', {
        "cpu": fields.Nested(cpu_fields, description='CPU information'),
        "disk": fields.Nested(disk_fields, description='Disk information'),
        "platform": fields.Nested(platform_fields, description='Platform information'),
        "user": fields.String(description='Current user'),
        "processes": fields.List(fields.Nested(processes_fields), description='Running processes')
    })


class NetworkDto:
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
    addrs = dict()
    for addr in get_interfaces():
        addrs[addr] = fields.Nested(interface_fields, description='Interface ' + addr)
    interfaces_fields = api.model('interfaces_fields', addrs)

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
