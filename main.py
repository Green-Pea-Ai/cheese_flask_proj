from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from com_cheese_api.ext.routes import initialize_routes
from com_cheese_api.cop.rev.review.model.review_kdd import ReviewKdd
from com_cheese_api.cop.rev.review.model.review_dfo import ReviewDfo

app = Flask(__name__)
CORS(app)
api = Api(app)

initialize_routes(api)

# kdd = ReviewKdd()
# temp = kdd.crawling()
# kdd.save_csv(temp)

dfo = ReviewDfo()
cheese_data_frame = dfo.cheese_df()
df = dfo.data_refine(cheese_data_frame)
print("-------------------------------------")
print(df.head(10))

    