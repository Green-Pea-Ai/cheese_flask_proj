# ==============================================================
# ====================                     =====================
# ====================       Modeling      =====================
# ====================                     =====================
# ==============================================================
# DB로 접속하는 부분

# review_num,
# category,
# brand_name,
# product_name,
# review_title,
# review_detail,
# review_date,
# review_views

class ReviewDto(db.Model):
    __tableName__="reviews"
    __table_args__={'mysql_collate':'utf8_general_ci'}

    rev_id: int = db.Column(db.Integer, primary_key=True, index=True)
    review_title: str = db.Column(db.String(100))
    review_detail: str = db.Column(db.String(500))

    user_id = db.Column(db.String(10), db.ForeignKey(UserDto.user_id))
    user = db.relationship('UserDto', back_populates='reviews')
    item_id = db.Column(db.Integer, db.ForeignKey(ItemDto.item_id))
    item = db.relationship('ItemDto', back_populates='reviews')

    def __init__(self, title, review_detail, user_id, item_id):
        self.review_title = title
        self.review_detail = review_detail
        self.user_id = user_id
        self.item_id = item_id

    def __repr__(self):
        return f'rev_id={self.rev_id}, user_id={self.user_id}, item_id={self.item_id},\
            review_title={self.review_title}, review_detail={self.review_detail}'

    def json(self):
        return {
            'rev_id': self.rev_id,
            'user_id': self.user_id,
            'item_id': self.item_id,
            'review_title': self.review_title,
            'review_detail': self.review_detail
        }


class ReviewVo():
    rev_id: int = 0
    user_id: str = ''
    item_id: int = 0
    review_title: str = ''
    review_detail: str = ''