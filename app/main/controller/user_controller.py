from flask import request
from flask_restx import Resource

from app.main.service.user_service import *
from app.main.representation.user import UserRepresentation
from app.main.util.decorator import token_required

api = UserRepresentation.api
_user = UserRepresentation.user


@api.route('/')
class UserList(Resource):
    @token_required
    @api.doc('list_of_registered_users')
    @api.marshal_list_with(_user, envelope='data')
    def get(self):
        return get_all_users()

    @token_required
    @api.response(201, 'User successfully created.')
    @api.doc('create a new user')
    @api.expect(_user, validate=True)
    def post(self):
        data = request.json
        return save_new_user(data=data)


@api.route('/<public_id>')
@api.param('public_id', 'The User identifier')
@api.response(404, 'User not found.')
class User(Resource):
    @token_required
    @api.doc('get a user')
    @api.marshal_with(_user)
    def get(self, public_id):
        user = get_a_user(public_id)
        if not user:
            api.abort(404)
        else:
            return user