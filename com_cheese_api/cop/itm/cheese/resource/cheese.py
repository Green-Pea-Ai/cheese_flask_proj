import pandas as pd

from wordcloud import WordCloud
from collections import Counter
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

from flask import request, jsonify
from flask_restful import Resource, reqparse, marshal_with, fields
import json
from collections import OrderedDict

from com_cheese_api.ext.db import db, openSession
from com_cheese_api.cop.itm.cheese.model.cheese_dao import CheeseDao
from com_cheese_api.cop.itm.cheese.model.cheese_dto import CheeseDto, CheeseVo

# from com_cheese_api.cop.itm.cheese.model.cheese_service import CheeseService


'''
결과물 적어서 남겨놓기
'''

# service는 전처리하는 곳
# hook = 아래의 순서대로 하겠다.
# 'userid' : this.train.PassengerId = train에 있는 Pclass를 가져와서 userid로 바꾼다
# odf 랑 df 를 따로 만들어서 axis =1 로 양옆으로 둘을 붙일 수 있게(concat) 함
# staticmethod는  self가 없음 create_train같은 함수를 가져다 쓸 수 있게함


# parser = reqparse.RequestParser()
# parser.add_argument('cheese_id', type=str, required=True, help='This cheese_id')
# parser.add_argument('ranking', type=int, required=True, help='This ranking')
# parser.add_argument('category', type=str, required=True, help='This category')
# parser.add_argument('brand', type=str, required=True, help='This brand')
# parser.add_argument('name', type=str, required=True, help='This name')
# parser.add_argument('content', type=str, required=True, help='This content')
# parser.add_argument('texture', type=str, required=True, help='This texture')
# parser.add_argument('types', type=str, required=True, help='This types')
# parser.add_argument('price', type=int, required=True, help='This price')
# parser.add_argument('img', type=str, required=True, help='This img')


# ==============================================================
# ====================                     =====================
# ====================      Resourcing     =====================
# ====================                     =====================
# ==============================================================
# Api가 될 녀석
# 외부에 공표될 부분

cheese_fields = {
    'cheese_id': fields.String, 
    'ranking': fields.Integer, 
    'category': fields.String,
    'brand': fields.String,
    'name': fields.String,
    'content': fields.String,
    'texture': fields.String,
    'types': fields.String,
    'price': fields.Integer,
    'img': fields.String
}

# ==============================================================
# ====================                     =====================
# ====================      Cheeses        =====================
# ====================                     =====================
# ==============================================================

parser = reqparse.RequestParser()

class Cheeses(Resource):

    def __init__(self):
        self.parser = reqparse.RequestParser()

    @marshal_with(cheese_fields)
    def post(self):
        print(f'[========Cheeses POST!!!(bulk)========]')
        CheeseDao.bulk()
        # try:
        #     CheeseDao.save(cheese)
        #     return {'code': 0, 'message' : 'SUCCESS'}, 200
        # except:
        #     return {'message': 'cheese insert error!!'}, 500

    # cheese find_all
    @staticmethod
    def get():

        print("=================== Cheeses GET() HEAD ===================\n\n")
        cheese = CheeseDao.query.order_by(CheeseDao.ranking).all()

        return jsonify([item.json for item in cheese])

        # 1차 flask -> react 전송 json 데이터, 정렬 안됨
        # cheese = CheeseDao.find_all()
        # return jsonify([item.json for item in cheese])

        # 2차 rank로 정렬한 json 데이터 만들기, 완성!
        # cheese = CheeseDao.query.order_by(CheeseDao.ranking).all()        
        # return jsonify([item.json for item in cheese])

    print("=================== Cheeses GET() END ===================\n\n")



# ==============================================================
# ====================                     =====================
# ====================       Cheese        =====================
# ====================                     =====================
# ==============================================================
class Cheese(Resource):

    @marshal_with(cheese_fields)
    def post(self):
        print(f'[========Cheese POST!!!========]')
        body = request.get_json()
        cheese = CheeseDto(**body)
        CheeseDao.save(cheese)
        cheese_id = cheese.cheese_id

        return {'cheese': str(cheese_id)}, 200
    
    # find_one
    @staticmethod
    def get(cheese_id):
        print("=================== Cheese GET() HEAD ===================\n\n")
        cheese = CheeseDao.find_by_cheese(cheese_id)
        if cheese:
            return cheese.json()
        return {'message': 'Not use find_one Cheese.'}, 404

    # @staticmethod
    # def get(cheese_id: str):
    #     print('read one')
    #     try:
    #         print(f'Cheese ID is {cheese_id}')
    #         cheese = CheeseDao.find_one(cheese_id)
    #         if cheese:
    #             return cheese.json()
    #     except Exception as e:
    #         return {'message': 'Cheese not found'}, 404

    @staticmethod
    def put():
        print("=================== PUT() HEAD ===================\n\n")
        parser.add_argument('cheese_id')
        parser.add_argument('ranking')
        parser.add_argument('category')
        parser.add_argument('brand')
        parser.add_argument('name')
        parser.add_argument('content')
        parser.add_argument('texture')
        parser.add_argument('types')
        parser.add_argument('price')
        parser.add_argument('img')

        args = parser.parse_args()
        CheeseDao.update(args)
        cheese = CheeseDao.find_one(args.cheese_id)
        if args.ranking == cheese.ranking and\
            args.category == cheese.category and\
            args.brand == cheese.brand and\
            args.name == cheese.name and\
            args.content == cheese.content and\
            args.texture == cheese.texture and\
            args.types == cheese.types and\
            args.price == cheese.price and\
            args.img == cheese.img:
                print(f'Cheese Update Success!!')
                return cheese.json(), 200
        else:
            print(f'Cheese Update Fail!!')
            return {'message': 'Cheese not found'}, 404


    @staticmethod
    def delete():
        print("=================== DELETE() HEAD ===================\n\n")
        try:
            args = parser.parse_args()
            params = json.loads(request.get_data(), encoding='utf-8')
            # print(args)
            # print(params['cheese_id'])
            print("======== del =========")
            print(CheeseDao.delete(params['cheese_id']))
            print('deleted')
            return {'message': 'SUCCESS'}, 200

        except Exception as e:
            return {'message': 'NOT FOUND DATA'}, 404


# class CheeseSearch():
#     ...


# class CheeseWordCloud():

#     cheese_list = pd.read_csv('cheese_data.csv', encoding='utf-8')
#     cheese_list
#     text = ""

#     with open('./cheese_data.txt', 'r', encoding='utf-8') as f:
#         lines = f.readlines()
#         for line in lines:
#             text += line
    
#     font_path = ''

#     wc = WordCloud(font_path=font_path, background_color="white", width=1000, height=700)
#     wc.generate(text)
#     wc.to_file("result.png")
#     plt.imshow(wc)
#     plt.show