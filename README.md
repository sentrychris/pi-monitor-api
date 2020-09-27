# RaspiMon API

A simple API for monitoring your raspberry pi.

See it in action [here!](https://pi.rowles.ch)

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

## Endpoints

[Documented here.](https://pi.rowles.ch)

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
    WSGIScriptAlias / /var/www/flaskapps/raspi-mon-api/raspimon.wsgi
    <Directory /var/www/flaskapps/raspi-mon-api/app>
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

## License

raspi-mon-api is open-sourced software licensed under the MIT license.
