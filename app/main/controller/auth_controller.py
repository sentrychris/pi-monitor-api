from flask import request
from flask_restx import Resource

from app.main.service.auth_service import *
from app.main.representation.auth import AuthRepresentation
from app.main.decorator.auth_decorator import token_required

api = AuthRepresentation.api
user_auth = AuthRepresentation.user_auth
auth_details = AuthRepresentation.auth_details


@api.route('/login')
class UserLogin(Resource):
    @api.doc('user login')
    @api.expect(user_auth, validate=True)
    def post(self):
        post_data = request.json
        return login_user(data=post_data)


@api.route('/verify')
class UserVerify(Resource):
    @api.doc('user verify')
    @api.marshal_with(auth_details)
    def get(self):
        auth_header = request.headers.get('Authorization')
        return verify_user(token=auth_header)


@api.route('/logout')
class UserLogout(Resource):
    @token_required
    @api.doc('logout a user')
    def post(self):
        auth_header = request.headers.get('Authorization')
        return logout_user(token=auth_header)
