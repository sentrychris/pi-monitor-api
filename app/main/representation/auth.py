from flask_restx import Namespace, fields, marshal


class AuthRepresentation:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password'),
    })
    user_fields = api.model('user_fields', {
        'user_id': fields.String(description='The user ID'),
        'email': fields.String(description='The user email address'),
        'admin': fields.String(description='Is user admin'),
        'registered_on': fields.String(description='Date user registered'),
        'token': fields.String(description='User authentication token')
    })
    auth_details = api.model('user_auth', {
        'status': fields.String(description='Status'),
        'data': fields.Nested(user_fields, description='User details'),
    })