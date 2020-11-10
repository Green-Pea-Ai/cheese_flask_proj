from flask import Flask
from flask_restful import Api
from com_cheese_api.ext.db import url, db
from com_cheese_api.ext.routes import initialize_routes
# from com_cheese_api.usr.user.resource.user import UserDao
# from com_cheese_api.cop.rev.review.model.review_kdd import ReviewKdd
from com_cheese_api.usr.user.model.user_dao import UserDao
from com_cheese_api.usr.user.model.user_dfo import UserDfo
from com_cheese_api.cop.itm.cheese.model.cheese_dao import CheeseDao

from com_cheese_api.cop.rev.review.model.review_dao import ReviewDao
from com_cheese_api.cop.rev.review.model.review_dto import ReviewDto
from flask_cors import CORS



app = Flask(__name__)
CORS(app, resources={r'/api/*': {"origins": "*"}})

app.config['SQLALCHEMY_DATABASE_URI'] = url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

api = Api(app)

with app.app_context():

    db.create_all()

    user_count = UserDao.count()

    print(f'USER TABLE CNT : {user_count[0]:10}')

    print(f'===== Users Total Count is {user_count} =====')
    if user_count[0] == 0:
        UserDao.bulk()

    user_all = UserDao.find_all()
    print(f'insert 테스트!!')
    # print(f'===== Users Total Count is {user_all} =====')
    # UserDao.bulk()
    # user_all.bulk()

    # cheese_all = CheeseDao.find_all()
    CheeseDao.bulk()

initialize_routes(api)


# kdd = ReviewKdd()
# temp = kdd.crawling()
# kdd.save_csv(temp)

# dfo = ReviewDfo()
# cheese_data_frame = dfo.cheese_df()
# df = dfo.data_refine(cheese_data_frame)
# print("-------------------------------------")
# print(df.head(10))

    