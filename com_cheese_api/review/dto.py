from com_cheese_api.ext.db import db


class ReviewDto(db.Model):

    __tablename__ = 'reviews'
    __table_args__ = {'mysql_collate':'utf8_general_ci'}

    review_num: int = db.Column(db.Integer, primary_key = True, index = True, autoincrement = True)
    brand_name: str = db.Column(db.String(10))
    product_name: str = db.Column(db.String(20))
    review_title: str = db.Column(db.String(50))
    review_detail: str = db.Column(db.String(500))
    review_create_date: str = db.Column(db.DateTime, default = db.func.now())
    review_views: int = db.Column(db.Integer)

    def __init__(self, review_num, brand_name, product_name, review_title, review_detail, review_create_date, review_views):
        self.review_num = review_num
        self.brand_name = brand_name
        self.product_name = product_name
        self.review_title = review_title
        self.review_detail = review_detail
        self.review_create_date = review_views
        self.review_views = review_views

    def __repr__(self):
        return f''
