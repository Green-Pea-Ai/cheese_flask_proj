from com_cheese_api.ext.db import db

'''
결과물
'''

# 설명

# 웹크롤링, 텍스트 마이닝 -> 데이터 마이닝



# 마일드 스톤(미국 도로보면 지역의 경계에 웰컴 어디어디 지역명 적어놓은것)
# ==============================================================
# ====================                     =====================
# ====================         KDD         =====================
# ====================                     =====================
# ==============================================================

class CheeseKdd(object):
    ...



# ==============================================================
# ====================                     =====================
# ====================    Preprocessing    =====================
# ====================                     =====================
# ==============================================================

class CheeseDf(object):
    ...



# ==============================================================
# ====================                     =====================
# ====================       Modeling      =====================
# ====================                     =====================
# ==============================================================

class CheeseDto(db.Model):
    ...

class CheeseVo(object):
    ...

class CheeseDao(CheeseDto):
    ...

class CheeseTF(object):
    ...

class CheeseAi(object):
    ...

# ==============================================================
# ====================                     =====================
# ====================      Resourcing     =====================
# ====================                     =====================
# ==============================================================

# Api가 될 녀석
# 외부에 공표될 부분
class Cheese(Resource):
    ...
