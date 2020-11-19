from os import stat
from com_cheese_api.cop.ord.order.model.order_dto import OrderDto
from com_cheese_api.cop.ord.order.model.order_dao import OrderDao

#from com_cheese_api.util.file import FileReader
from com_cheese_api.cmm.utl.file import FileReader

import numpy as np
import pandas as pd
from flask import request
from flask_restful import Resource, reqparse
from flask import jsonify
import json
import os


'''
json = json.loads() => dict
dict = json.dumps() => json
'''

'''
서버와 정보를 주고 받는다.
'''

parser = reqparse.RequestParser() 

class Order(Resource):

    @staticmethod
    def post():
        print(f' =========== Order =========== \n')
        body = request.get_json()
        order = OrderDto(**body)
        OrderDao.save(order)
        user_id = order.user_id

        return {'user_id': str(user_id)}, 200

    @staticmethod
    def get(user_id: str):
        """
        유저 아이디를 받아와 해당 유저 객체를 리턴한다
        Parameter: User ID 를 받아온다
        return: 해당 아이디 유저 객체
        """
        print('===========user_id=============')
        print(user_id)
        try:
            print(f'User ID is {user_id}')
            user = OrderDao.find_by_id(user_id)

            if user:
                return jsonify([user.json])
        except Exception as e:
            print(e)
            return {'message': 'User not found'}, 404

    @staticmethod
    def put(user_id: str):
        """
        서버에서 해당 ID 의 새로운 유저 정보를 받아온다.
        정보를 토대로 해당 ID 유저의 정보를 바꿔서
        정보를 서버에 보내준다.
        parameter: 유저 아이디를 받아온다
        return: 새로운 유저 데이터를 리턴 한다
        """
        # 주문번호에 대한 주문 정보 수정
        parser.add_argument('order_no', type=str, required=True, help='This is order_no field')
        parser.add_argument('user_id', type=str, required=True, help='This is user_id field')
        parser.add_argument('cheese_id', type=str, required=True, help='This is cheese_id field')
        parser.add_argument('buy_count', type=str, required=True, help='This is buy_count field')
        parser.add_argument('total_price', type=str, required=True, help='This is total_price field')
    
        print("argument added")
        # def __init__(self, user_id, password,fname, lname, age, gender,email):
        args = parser.parse_args()
        # print(f'User {args["user_id"]} updated')
        # print(f'User {args["password"]} updated')
        # user = OrderDto(args.user_id, args.password, args.gender, args.age_group)
        # print("user created")
        # OrderDao.update(user)
        # data = user.json()
        # return data, 200


    @staticmethod
    def delete(user_id: str):
        """
        주문번호에 맞는 데이터를 삭제한다.
        Parameter: 파라미터
        """
        # UserDao.delete(id)
        # print(f'User {id} Deleted')
        print(f'[ ========= Order DELETE() =========  ]')
        args = parser.parse_args()
        # print(f'User {args["user_id"]} deleted')
        print(f'Order delete!!')
        return {'code': 0, 'message': 'SUCCESS'}, 200
        


class Orders(Resource):

    @staticmethod
    def post():
        print(f'[ ========= Orders POST() =========  ]')

        order_count = OrderDao.count()

        if order_count[0] == 0:
            OrderDao.bulk()
        else:
            print("Orders Data exists...")

    @staticmethod
    def get():
        print(f'[ ========= Orders GET() =========  ]')
        data = OrderDao.find_all()
        return jsonify([item.json for item in data])
        # return json.dumps(jsonify([item.json for item in data])), 200

