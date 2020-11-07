# ==============================================================
# ====================                     =====================
# ====================       Modeling      =====================
# ====================                     =====================
# ==============================================================
# DB에 있는 데이터 가져오는 작업

class ReviewDao(ReviewDto):

    @classmethod
    def find_all(cls):
        return cls.query.all()

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filer_by(name == name).all()

    @classmethod
    def find_by_id(cls, id):
        return cls.query,filter(ReviewDto.rev_id == id).one()

    @staticmethod
    def save(review):
        Session = openSession()
        session = Session()
        session.add(review)
        session.commit()

    @staticmethod
    def update(review, review_id):
        Session = openSession()
        session = Session()
        session.query(ReviewDto).filter(ReviewDto.rev_id == review.review_id)\
            .update({ReviewDto.review_title: review.review_title,
                        ReviewDto.review_detail: review.review_detail})
        session.commit()

    @classmethod
    def delete(cls, rev_id):
        Session = openSession()
        session = Session()
        cls.query(ReviewDto.rev_id == rev_id).delete()
        session.commit()


class ReviewTF():
    ...
    
class ReviewAi():
    ...
