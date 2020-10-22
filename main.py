from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from com_cheese_api.ext.routes import initialize_routes
from com_cheese_api.ext.routes import initialize_routes_cheese
from com_cheese_api.ext.routes import initialize_routes_board
from com_cheese_api.ext.routes import initialize_routes_suggest
from com_cheese_api.ext.routes import initialize_routes_admin
from com_cheese_api.ext.routes import initialize_routes_login
from com_cheese_api.ext.routes import initialize_routes_logout


app = Flask(__name__)
CORS(app)
api = Api(app)

initialize_routes(api)
initialize_routes_cheese(api)
initialize_routes_board(api)
initialize_routes_suggest(api)
initialize_routes_admin(api)
initialize_routes_login(api)
initialize_routes_logout(api)