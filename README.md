# Raspberry Pi Monitor

View a client [here!](https://pi.mon.rowles.ch)

## Requirements

- A Raspberry Pi with at least 1GB of RAM (running a Linux distro)
- MySQL (optional, if you want to add authentication and user management)

## Installation

Clone the repository:
```
$ git clone git@github.com:chrisrowles/raspi-mon-api.git
```

Create the virtual environment:
```
$ virtualenv raspi-mon-api
```

Activate the virtual environment:
```
$ source raspi-mon-api/bin/activate
```

Install dependencies:
```
$ pip install -r requirements.txt
```

### Optional

You'll need to do the following if you would like authentication and user management.

Initialise the database and run migrations:
```
$ python manage.py db init
$ python manage.py db migrate
$ python manage.py db upgrade
```

## Endpoints

[Documented here.](https://pi.rowles1.net)

## Deployment

### Apache Configuration
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

raspi-mon-api is open-source software licensed under the MIT license.
