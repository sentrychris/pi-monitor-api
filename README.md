# RaspiMon API

A simple API for monitoring your raspberry pi.

## Installation

Clone the repository:
```
$ git clone git@github.com:raekw0n/raspi-mon-api.git
```

Create the virtual environment:
```
$ pip virtualenv piMonitor
```

Activate the virtual environment:
```
$ source piMonitor/bin/activate
```

Install the project's dependencies:
```
$ pip install -r requirements.txt
```

## How it Works

It's incredibly simple, just submit a GET request to your chosen endpoint to receive data, which will always be returned in JSON format, then you can consume that data with whatever library/language you're using and use it to display information about your Pi.

## Endpoints

#### GET `/system`
Returns a JSON object containing core system information, including:

- **CPU**: temperature, clock speed (frequency) and system-wide usage as a percentage.
- **Disk**: total size (GB), used amount (GB), remaining space (GB) and usage as a percentage.
- **Processes**: top ten processes by memory usage, process information includes name, PID, username and memory (MB).
- **Platform**: distribution name and kernel version.
- **Uptime**: system uptime represented in format "_n_ days, _n_ hours, _n_ minutes and _n_ seconds".

### GET `/network`
Returns a JSON object containing network information, including:

- **connections**: established UNIX socket connections.
- **interfaces**: network interfaces and send/receive, error and dropout statistics.
- **wifi**: wireless SSID, host MAC address, channel, encryption, signal strength, and quality as a percentage.

### GET `/network/counter/<interface>`
(e.g. /network/counter/wlan0)

Streams a JSON representation of kB/s sent/received for the chosen interface

## Apache Configuration
Firstly, make sure you have `libapache2-mod-wsgi-py3` installed:

```bash
$ sudo apt install libapache2-mod-wsgi-py3
```

Then create and enable your new virtualhost configuration:

```conf
<VirtualHost *:80>
    ServerName api.raspberrypi.local
    ServerAlias www.api.raspberrypi.local
    WSGIScriptAlias / /var/www/flaskapps/raspimon/raspimon.wsgi
    <Directory /var/www/flaskapps/raspimon/app>
            Options Indexes FollowSymLinks MultiViews
            AllowOverride all
            Require all granted
    </Directory>
    ErrorLog /var/log/apache2/api.raspberrypi.local-error.log
    CustomLog /var/log/apache2/api.raspberrypi.local-access.log combined
</VirtualHost>
```

```bash
$ sudo a2ensite api.raspberrypi.local.conf
$ sudo systemctl reload apache2
```
 
A working example client can be downloaded from [here](https://github.com/raekw0n/raspi-mon).

## License

RaspiMon API is open-sourced software licensed under the MIT license.
