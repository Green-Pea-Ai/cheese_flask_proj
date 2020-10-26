from typing import List
from flask import request
from flask_restful import Resource, reqparse
from com_cheese_api.review.dao import UserDao
from com_cheese_api.review.dto import UserDto, UserVo
import json
from flask import jsonify

parser = reqparse.RequestParser()   # only allow price changes, no name changes allowed
parser.add_argument('userid', type=str, required=True, help='This field should be a userid')
parser.add_argument('password', type=str, required=True, help='This field should be a password')

class User(Resource):
    @staticmethod
    def post():
        args = parser.parse_args()
        print(f'User {args["id"]} added ')
        params = json.loads(request.get_data(), encoding='utf-8')
        if len(params) == 0:

            return 'No parameter'

        params_str = ''
        for key in params.keys():
            params_str += 'key: {}, value: {}<br>'.format(key, params[key])
        return {'code':0, 'message': 'SUCCESS'}, 200
    @staticmethod
    def get(id):
        print(f'User {id} added ')
        try:
            user = UserDao.find_by_id(id)
            if user:
                return user.json()
        except Exception as e:
            return {'message': 'User not found'}, 404

    