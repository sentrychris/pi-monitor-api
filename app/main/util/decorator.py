from functools import wraps
from flask import request

from app.main.service.auth_service import *


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):

        auth_header = request.headers.get('Authorization')
        data, status = verify_user(token=auth_header)
        auth = data.get('data')

        if not auth:
            return data, status

        return f(*args, **kwargs)

    return decorated
