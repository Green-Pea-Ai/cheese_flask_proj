from flask_restful import Resource, reqparse

class BoardAPI(Resource):
    def get(self):
        return {'message': 'Board API Start !!'}