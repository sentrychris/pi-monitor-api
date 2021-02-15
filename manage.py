import os
import unittest

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_cors import CORS

from app.main import create_app, db
from app import blueprint

app = create_app('dev')

config = {
  'origins': [
    'https://pi.mon.rowles.ch',
    'http://192.168.1.100:8080',
  ],
}

CORS(app, resources={ r'/*': {'origins': config['origins']}}, supports_credentials=True)
app.register_blueprint(blueprint)
app.app_context().push()

manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)


@manager.command
def run():
    app.run(host='0.0.0.0')


@manager.command
def test():
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == '__main__':
    manager.run()
