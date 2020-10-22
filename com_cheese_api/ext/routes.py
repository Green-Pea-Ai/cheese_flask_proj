from com_cheese_api.home.api import HomeAPI
from com_cheese_api.cheese.cheese_api import CheeseAPI
from com_cheese_api.board.board_api import BoardAPI
from com_cheese_api.suggest.suggest_api import SuggestAPI
from com_cheese_api.admin.admin_api import AdminAPI
from com_cheese_api.login.login_api import LoginAPI
from com_cheese_api.login.sign_up_api import SignUpAPI


def initialize_routes(api):
    api.add_resource(HomeAPI, '/api')

def initialize_routes_cheese(cheese_api):
    cheese_api.add_resource(CheeseAPI, '/api/cheese')

def initialize_routes_board(board_api):
    board_api.add_resource(BoardAPI, '/api/board')

def initialize_routes_suggest(suggest_api):
    suggest_api.add_resource(SuggestAPI, '/api/suggest')

def initialize_routes_admin(admin_api):
    admin_api.add_resource(AdminAPI, '/api/admin')

def initialize_routes_login(login_api):
    login_api.add_resource(LoginAPI, '/api/login')

def initialize_routes_logout(sign_up_api):
    sign_up_api.add_resource(SignUpAPI, '/api/sign_up')
