import os
import pwd
import platform
import psutil


def get_system_info():
    system = dict()
    system["cpu"] = get_cpu_info()
    system["disk"] = get_disk_info()
    system["mem"] = get_mem_info()
    system["platform"] = get_platform_info()
    system["platform"]["uptime"] = get_system_uptime()
    system["user"] = get_user()
    system["processes"] = []
    processes = get_processes()
    for process in processes[:10]:
        system["processes"].append(process)

    return system


def do_system_action(data):
    if data['action'] == 'reboot':
        return reboot()
    elif data['action'] == 'shutdown':
        return shutdown()
    else:
        response_object = {
            'status': 'fail',
            'message': 'Invalid action provided, please try again.',
        }

        return response_object, 400


def get_platform_info():
    return {
        'distro': os.popen('cat /etc/*-release | awk NR==1 | cut -c 12-').read().replace('"', '').rstrip(),
        'kernel': platform.release()
    }


def get_system_uptime():
    try:
        f = open("/proc/uptime")
        contents = f.read().split()
        f.close()
    except Exception:
        return "Cannot open uptime file: /proc/uptime"

    total_seconds = float(contents[0])
    days = int(total_seconds / 86400)
    hours = int((total_seconds % 86400) / 3600)
    minutes = int((total_seconds % 3600) / 60)
    seconds = int(total_seconds % 60)

    uptime = ""

    if days > 0:
        uptime += str(days) + " " + (days == 1 and "day" or "days") + ", "
    if len(uptime) > 0 or hours > 0:
        uptime += str(hours) + " " + (hours == 1 and "hour" or "hours") + ", "
    if len(uptime) > 0 or minutes > 0:
        uptime += str(minutes) + " " + (minutes == 1 and "minute" or "minutes") + ", "

    uptime += str(seconds) + " " + (seconds == 1 and "second" or "seconds")

    return uptime


def get_cpu_info():
    return {
        'usage': round(psutil.cpu_percent(interval=1), 2),
        'temp': 50,
        'freq': round(psutil.cpu_freq().current, 2)
    }


def get_disk_info():
    disk = psutil.disk_usage('/')

    return {
        'total': round(disk.total / (1024.0 ** 3), 2),
        'used': round(disk.used / (1024.0 ** 3), 2),
        'free': round(disk.free / (1024.0 ** 3), 2),
        'percent': disk.percent
    }


def get_mem_info():
    mem = psutil.virtual_memory()

    return {
        'total': round(mem.total / (1024.0 ** 3), 2),
        'used': round(mem.used / (1024.0 ** 3), 2),
        'free': round(mem.free / (1024.0 ** 3), 2),
        'percent': mem.percent
    }

def get_processes():
    processes = []
    for proc in psutil.process_iter():
        try:
            process = proc.as_dict(attrs=['pid', 'name', 'username'])
            process['mem'] = round(proc.memory_info().rss / (1024 * 1024), 2)
            processes.append(process)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    processes = sorted(processes, key=lambda sort: sort['mem'], reverse=True)

    return processes


def get_user():
    return pwd.getpwuid(os.getuid())[0]


def shutdown():
    return os.system('sudo shutdown -h now')


def reboot():
    return os.system('sudo reboot')
