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


import logging
from flask import Blueprint
from flask_restful import Api
from com_cheese_api.resources.home import Home

home = Blueprint('home', __name__, url_prefix='/api')

api = Api(home)


def initialize_routes(api):
    
    api.add_resource(Home, '/api')


@home.errorhandler(500)
def home_api_error(e):
    logging.exception('An error occurred during home request. %s' % str(e))
    return 'An internal error occurred.', 500
