from flask import request
from flask_restx import Resource

from app.main.representation.user import UserRepresentation
from app.main.service.user_service import save_new_user

api = UserRepresentation.api
_user = UserRepresentation.user


@api.route('/')
class UserList(Resource):
    @api.response(201, 'User successfully created.')
    @api.doc('create a new user')
    @api.expect(_user, validate=True)
    def post(self):
        data = request.json
        return save_new_user(data=data)
