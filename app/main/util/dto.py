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

    ping = api.model('ping', {
        "status": fields.String(description='Network connection status'),
    })

    details_fields = api.model('details_fields', {
        "name": fields.String(description='Wireless SSID'),
        "quality": fields.String(description='Wireless quality'),
        "channel": fields.String(description='Wireless channel'),
        "encryption": fields.String(description='Wireless encryption'),
        "address": fields.String(description='MAC address'),
        "signal": fields.String(description='Wireless signal')
    })
    speed_fields = api.model('speed_fields', {
        "ping": fields.String(description='Ping'),
        "download": fields.String(description='Upload speed'),
        "upload": fields.String(description='Download speed')
    })
    wifi = api.model('network', {
        'details': fields.Nested(details_fields, description='Wifi details'),
        'speed': fields.Nested(speed_fields, description='Wifi speed')
    })

