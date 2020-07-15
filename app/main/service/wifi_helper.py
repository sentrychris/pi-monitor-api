import re
import subprocess

interface = "wlan0"


class Wifi:
    @staticmethod
    def get_wifi_info():
        cells = [[]]
        info = {}

        proc = subprocess.Popen(["iwlist", interface, "scan"], stdout=subprocess.PIPE, universal_newlines=True)
        out, err = proc.communicate()

        for line in out.split("\n"):
            cell_line = Wifi.match(line, "Cell ")
            if cell_line is not None:
                cells.append([])
                line = cell_line[-27:]
            cells[-1].append(line.rstrip())

        cells = cells[1:]

        for cell in cells:
            info.update(Wifi.parse_cell(cell))

        return info

    @staticmethod
    def get_wifi_speed():
        speedtest = subprocess.Popen('/usr/local/bin/speedtest-cli --simple', shell=True,
                                     stdout=subprocess.PIPE).stdout.read().decode('utf-8')

        ping = re.findall(r'Ping:\s(.*?)\s', speedtest, re.MULTILINE)
        download = re.findall(r'Download:\s(.*?)\s', speedtest, re.MULTILINE)
        upload = re.findall(r'Upload:\s(.*?)\s', speedtest, re.MULTILINE)

        response = {}
        try:
            response.update({
                'ping': ping[0].replace(',', '.'),
                'download': download[0].replace(',', '.'),
                'upload': upload[0].replace(',', '.')
            })
        except Exception:
            pass

        return response

    @staticmethod
    def get_name(cell):
        return Wifi.matching_line(cell, "ESSID:")[1:-1]

    @staticmethod
    def get_quality(cell):
        quality = Wifi.matching_line(cell, "Quality=").split()[0].split('/')
        return str(int(round(float(quality[0]) / float(quality[1]) * 100))).rjust(3)

    @staticmethod
    def get_channel(cell):
        return Wifi.matching_line(cell, "Channel:")

    @staticmethod
    def get_signal_level(cell):
        return Wifi.matching_line(cell, "Quality=").split("Signal level=")[1]

    @staticmethod
    def get_encryption(cell):
        enc = ""
        if Wifi.matching_line(cell, "Encryption key:") == "off":
            enc = "Open"
        else:
            for line in cell:
                matching = Wifi.match(line, "IE:")
                if matching is not None:
                    wpa = Wifi.match(matching, "WPA Version ")
                    if wpa is not None:
                        enc = "WPA v." + wpa
            if enc == "":
                enc = "WEP"
        return enc

    @staticmethod
    def get_address(cell):
        return Wifi.matching_line(cell, "Address: ")

    @staticmethod
    def matching_line(lines, keyword):
        for line in lines:
            matching = Wifi.match(line, keyword)
            if matching is not None:
                return matching
        return None

    @staticmethod
    def match(line, keyword):
        line = line.lstrip()
        length = len(keyword)
        if line[:length] == keyword:
            return line[length:]
        else:
            return

    @staticmethod
    def parse_cell(cell):
        rules = {
            "name": Wifi.get_name,
            "quality": Wifi.get_quality,
            "channel": Wifi.get_channel,
            "encryption": Wifi.get_encryption,
            "address": Wifi.get_address,
            "signal": Wifi.get_signal_level
        }

        parsed_cell = {}
        for key in rules:
            rule = rules[key]
            parsed_cell.update({key: rule(cell)})

        return parsed_cell
