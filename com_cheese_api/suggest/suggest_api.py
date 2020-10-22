from flask_restful import Resource, reqparse

class SuggestAPI(Resource):
    def get(self):
        return {'message': 'Suggest API Start !!'}