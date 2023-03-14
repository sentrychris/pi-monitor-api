from flask_restx import Namespace, fields, marshal


class SystemRepresentation:
    api = Namespace('system', description='system monitor core related operations')

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
    mem_fields = api.model('mem_fields', {
        "total": fields.Float(description='Mem total'),
        "used": fields.Float(description='Mem used'),
        "free": fields.Float(description='Mem free'),
        "percent": fields.Float(description='Mem used percent')
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
    # banned_fields = api.model('banned_fields', [fields.List(fields.String(example='192.168.54.10'))])
    system = api.model('system', {
        "cpu": fields.Nested(cpu_fields, description='CPU information'),
        "mem": fields.Nested(mem_fields, description='Memory information'),
        "disk": fields.Nested(disk_fields, description='Disk information'),
        "platform": fields.Nested(platform_fields, description='Platform information'),
        "user": fields.String(description='Current user'),
        'banned': fields.List(fields.String(example="192.168.54.10")),
        "processes": fields.List(fields.Nested(processes_fields), description='Running processes')
    })