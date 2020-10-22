from flask_restful import Resource, reqparse

class AdminAPI(Resource):
    def get(self):
        return {'message': 'Admin API Start !!'}