from flask_restful import Resource, reqparse
from com_cheese_api.usr.user.model.user_dao import UserDao 
from com_cheese_api.usr.user.model.user_dto import UserVo
import json
from flask import jsonify

parser = reqparse.RequestParser()

class Login(Resource):
    print(f'[ User Login Resource Enter ]')

    @staticmethod
    def post():
        print('====== login.py POST(), 로그인 처리 ======')
        parser.add_argument('userId', type=str, required=True, help='user_id field')
        parser.add_argument('password', type=str, required=True, help='password field')
        args = parser.parse_args()
        print(args)

        user = UserVo()
        print(f'[ ID ] {args.userId} \n [ Password ] {args.password}')
        user.user_id = args.userId
        user.password = args.password

        print('ID: ', user.user_id)
        print('Password: ', user.password)

        data = UserDao.login(user)
        print(f'Login Result : {data}')

        return print(f'로그인 성공!!! {data[0]}'), 200


    # def get(self):
    #     return {'message': 'Login API Start !!'}