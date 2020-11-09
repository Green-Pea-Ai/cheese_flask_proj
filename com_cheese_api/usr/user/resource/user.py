#from com_cheese_api.usr.model.user_dto import UserDto
#from com_cheese_api.usr.model.user_dao import UserDao
from com_cheese_api.usr.user.model.user_dto import UserDto
from com_cheese_api.usr.user.model.user_dao import UserDao

#from com_cheese_api.util.file import FileReader
from com_cheese_api.cmm.utl.file import FileReader

import numpy as np
import pandas as pd
from flask import request
from flask_restful import Resource, reqparse
from pathlib import Path
from com_cheese_api.ext.db import url, db, openSession, engine
from konlpy.tag import Okt
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import seaborn as sns
from sqlalchemy import func
from sqlalchemy.ext.declarative import declarative_base

import os
import json

'''
json = json.loads() => dict
dict = json.dumps() => json
'''

parser = reqparse.RequestParser()

class User(Resource):
    @staticmethod
    def post():
        print(f'[User Signup Resource Enter]')
        body = request.get_json()
        user = UserDto(**body)
        UserDao.save(user)
        user_id = user_id

        return {'userId': str(user_id)}, 200

    @staticmethod
    def get(userId: str):
        try:
            print(f'User ID is {userId}')
            user = UserDao.find_one(userId)
            if user:
                return json.dumps(user.json()), 200
        except Exception as e:
            print(e)
            return {'message': 'User not found'}, 404

    # @staticmethod
    # def put():
    #     print(f'[User Put Resource Enter]')
    #     parser.add_argument('userId')
    #     parser.add_argument('password')
    #     parser.add_argument('gneder')
    #     parser.add_argument('age_group')
    #     args = parser.parse_args()
    #     UserDao.update(args)
    #     user = UserDao.find_one(args.userId)
    #     if args.password == user.password and \
    #         args.


# class Users(Resource)

#     @staticmethod
#     def post():
#         print(f'[ User Bulk Resource Enter ]')
#         UserDao.bulk()
        
#     @staticmethod
#     def get():
#         print(f'[ User List Resource Enter ]')
#         data = UserDao.find_all()
#         return json.dumps(data), 200