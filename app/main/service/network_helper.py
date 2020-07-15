import re
import subprocess

interface = "wlan0"


class Network:
    @staticmethod
    def get_wifi_info():
        cells = [[]]
        parsed_cells = []

        proc = subprocess.Popen(["iwlist", interface, "scan"], stdout=subprocess.PIPE, universal_newlines=True)
        out, err = proc.communicate()

        for line in out.split("\n"):
            cell_line = Network.match(line, "Cell ")
            if cell_line is not None:
                cells.append([])
                line = cell_line[-27:]
            cells[-1].append(line.rstrip())

        cells = cells[1:]

        for cell in cells:
            parsed_cells.append(Network.parse_cell(cell))

        return parsed_cells

    @staticmethod
    def get_wifi_speed():
        speedtest = subprocess.Popen('/usr/local/bin/speedtest-cli --simple', shell=True,
                                     stdout=subprocess.PIPE).stdout.read().decode('utf-8')

        ping = re.findall(r'Ping:\s(.*?)\s', speedtest, re.MULTILINE)
        download = re.findall(r'Download:\s(.*?)\s', speedtest, re.MULTILINE)
        upload = re.findall(r'Upload:\s(.*?)\s', speedtest, re.MULTILINE)

        response = dict()
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
        return Network.matching_line(cell, "ESSID:")[1:-1]

    @staticmethod
    def get_quality(cell):
        quality = Network.matching_line(cell, "Quality=").split()[0].split('/')
        return str(int(round(float(quality[0]) / float(quality[1]) * 100))).rjust(3)

    @staticmethod
    def get_channel(cell):
        return Network.matching_line(cell, "Channel:")

    @staticmethod
    def get_signal_level(cell):
        return Network.matching_line(cell, "Quality=").split("Signal level=")[1]

    @staticmethod
    def get_encryption(cell):
        enc = ""
        if Network.matching_line(cell, "Encryption key:") == "off":
            enc = "Open"
        else:
            for line in cell:
                matching = Network.match(line, "IE:")
                if matching is not None:
                    wpa = Network.match(matching, "WPA Version ")
                    if wpa is not None:
                        enc = "WPA v." + wpa
            if enc == "":
                enc = "WEP"
        return enc

    @staticmethod
    def get_address(cell):
        return Network.matching_line(cell, "Address: ")

    @staticmethod
    def matching_line(lines, keyword):
        for line in lines:
            matching = Network.match(line, keyword)
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
            "name": Network.get_name,
            "quality": Network.get_quality,
            "channel": Network.get_channel,
            "encryption": Network.get_encryption,
            "address": Network.get_address,
            "signal": Network.get_signal_level
        }

        parsed_cell = {}
        for key in rules:
            rule = rules[key]
            parsed_cell.update({key: rule(cell)})

        return parsed_cell
