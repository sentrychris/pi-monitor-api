# Pi Monitor API

View a client [here!](https://github.com/chrisrowles/pi-monitor)

## Requirements

- A Raspberry Pi with at least 1GB of RAM (running a Linux distro)
- MySQL (optional, if you want to add authentication and access control)

## Installation

Clone the repository:
```sh
git clone git@github.com:chrisrowles/pi-monitor-api.git
```

Create the virtual environment:
```sh
virtualenv pi-monitor-api
```

Activate the virtual environment:
```sh
source pi-monitor-api/bin/activate
```

Install dependencies:
```sh
pip install -r requirements.txt
```

Test it works:
```sh
python manage.py run
```

### Optional

You'll need to do the following if you would like authentication and user management.

Install extra dependencies:
```
sudo apt install libmysqlclient-dev
```

Inside the virtualenv:
```
pip install mysqlclient
```

Initialise the database and run migrations:
```sh
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
```

export your database connection string:
```sh
export DB_CONNECTION_STRING='mysql://<user>:<password>@<host>/<database>
```

## Development Server

You can run the development server using the following command:

```sh
python manage.py run

* Serving Flask app "app.main" (lazy loading)
* Environment: development
WARNING: This is a development server. Do not use it in a production deployment.
Use a production WSGI server instead.
* Debug mode: on
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
* Restarting with stat
* Debugger is active!
* Debugger PIN: <PIN>
```

## Endpoints

[Documented here.](https://sysapi.ddns.net)

## Deployment

### Apache Configuration
Firstly, make sure you have `libapache2-mod-wsgi-py3` installed:

```sh
sudo apt install libapache2-mod-wsgi-py3
```

Then create and enable your new virtualhost configuration:

```conf
<VirtualHost *:80>
    ServerName api.raspberrypi.local
    ServerAlias www.api.raspberrypi.local
    WSGIScriptAlias / /var/www/flaskapps/pi-monitor-api/api.wsgi
    <Directory /var/www/flaskapps/raspi-mon-api/app>
        Options Indexes FollowSymLinks MultiViews
        AllowOverride all
        Require all granted
    </Directory>
    ErrorLog /var/log/apache2/api.raspberrypi.local-error.log
    CustomLog /var/log/apache2/api.raspberrypi.local-access.log combined
</VirtualHost>
```

```sh
sudo a2ensite api.raspberrypi.local.conf
sudo systemctl reload apache2
```

#### Optional

If you want to enable authentication for user management, you'll need to add the following line to either your apache or virtualhost configuration:

```sh
WSGIPassAuthorization On
```

## License

This is open-source software licensed under the MIT license.
