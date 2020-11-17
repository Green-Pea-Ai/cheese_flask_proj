import logging
from flask import Blueprint
from flask_restful import Api
from com_cheese_api.cmm.hom.home import Home
from com_cheese_api.cop.rev.review.model.review_dto import ReviewVo
from com_cheese_api.cop.rev.review.resource.review import Review, Reviews

from com_cheese_api.cop.itm.cheese.resource.cheese import Cheeses, Cheese, CheeseSearch
from com_cheese_api.cop.itm.cheese.model.cheese_dto import CheeseVo


home = Blueprint('home', __name__, url_prefix='/api')

# login_user = Blueprint('login_user', __name__, url_prefix='/api/login')
# user = Blueprint('user', __name__, url_prefix='/api/user')
# users = Blueprint('users', __name__, url_prefix='/api/users')

cheese = Blueprint('cheese', __name__, url_prefix='/api/cheese')
cheeses = Blueprint('cheeses', __name__, url_prefix='/api/cheeses')
cheese_search = Blueprint('cheese_search', __name__, url_prefix='/api/cheese/search')

# review = Blueprint('review', __name__, url_prefix='/api/review')
reviews = Blueprint('reviews', __name__, url_prefix='/api/reviews')


api = Api(home)
# api = Api(user)

# api = Api(cheese)
api = Api(cheeses)
api = Api(cheese_search)

# api = Api(review)
api = Api(reviews)

def initialize_routes(api):
    # cheese = CheeseVo()

    api.add_resource(Home, '/api')
    # api.add_resource(User, '/api/user', '/api/user/<user_id>')
    api.add_resource(Cheese, '/api/cheese', '/api/cheese/<cheese_id>')
    api.add_resource(Cheeses, '/api/cheeses')
    api.add_resource(CheeseSearch, '/api/cheese/search', '/api/cheese/search/<category>')
    api.add_resource(Reviews, '/api/reviews')


@home.errorhandler(500)
def home_api_error(e):
    logging.exception('An error occurred during home request. %s' % str(e))
    return 'An internal error occurred.', 500

# @user.errorhandler(500)
# def user_api_error(e):
#     logging.exception('An error occurred during user request. %s' % str(e))
#     return 'An internal error occurred.', 500

# @cheese.errorhandler(500)
# def cheese_api_error(e):
#     logging.exception('An error occurred during cheese request. %s' % str(e))
#     return 'An internal error occurred.', 500

@cheeses.errorhandler(500)
def cheeses_api_error(e):
    logging.exception('An error occurred during cheeses request. %s' % str(e))
    return 'An internal error occurred.', 500



# ==============================================================
# ====================                     =====================
# ====================         TEST        =====================
# ====================                     =====================
# ==============================================================

# from com_cheese_api.home.api import HomeAPI
# from com_cheese_api.cheese.cheese_api import CheeseAPI
# from com_cheese_api.board.board_api import BoardAPI
# from com_cheese_api.suggest.suggest_api import SuggestAPI
# from com_cheese_api.admin.admin_api import AdminAPI
# from com_cheese_api.login.login_api import LoginAPI
# from com_cheese_api.login.sign_up_api import SignUpAPI


# def initialize_routes(api):
#     api.add_resource(HomeAPI, '/api')
#     api.add_resource(CheeseAPI, '/api/cheese')
#     api.add_resource(BoardAPI, '/api/board')
#     api.add_resource(SuggestAPI, '/api/suggest')
#     api.add_resource(AdminAPI, '/api/admin')
#     api.add_resource(LoginAPI, '/api/login')
#     api.add_resource(SignUpAPI, '/api/sign_up')


