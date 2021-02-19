from flask_restx import Namespace, fields, marshal


class AuthRepresentation:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password'),
    })
    auth_details = api.model('user_auth', {
        'user_id': fields.String(required=True, description='The user ID'),
        'email': fields.String(required=True, description='The user email address'),
        'admin': fields.String(required=True, description='Is user admin'),
        'registered_on': fields.String(required=True, description='Date user registered'),
    })