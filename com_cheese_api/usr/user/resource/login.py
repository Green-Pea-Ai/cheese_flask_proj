from flask_restful import Resource, reqparse

class LoginAPI(Resource):
    def get(self):
        return {'message': 'Login API Start !!'}