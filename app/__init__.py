from flask_restplus import Api
from flask import Blueprint

from .main.controller.user_controller import api as user_ns
from .main.controller.auth_controller import api as auth_ns
from .main.controller.system_controller import api as system_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='RaspiMon API',
          version='1.0',
          description='A lightweight monitoring API for the raspberry pi'
          )

api.add_namespace(user_ns, path='/user')
api.add_namespace(auth_ns)
api.add_namespace(system_ns)
