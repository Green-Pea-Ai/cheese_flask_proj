from flask_restful import Resource, reqparse

class SignUpAPI(Resource):
    def get(self):
        return {'message': 'Logout API Start !!'}