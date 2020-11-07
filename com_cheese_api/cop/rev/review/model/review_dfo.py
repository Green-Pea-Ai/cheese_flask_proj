import pandas as pd

# ==============================================================
# ====================                     =====================
# ====================    Preprocessing    =====================
# ====================                     =====================
# ==============================================================

# 데이터 정제 과정
class ReviewDfo(object):

    def __init__(self):
        ...

    def cheese_df(self):
        cheese_data_frame = pd.read_csv(
            '/home/bitai/Documents/EMP_Team/EMP_Main/Ai/cheese_flask_proj/data_set/cheese2pic_real_part10.csv',
            sep=','
        )

        return cheese_data_frame



    def data_refine(self, cheese_data_frame):

        print(f'[데이터 행과 열 확인] {cheese_data_frame.shape}')
        print(f'[타입 확인] {cheese_data_frame.dtypes}')

        df = pd.DataFrame(cheese_data_frame)

        # '[' 제거
        split = df['review_views'].str.split("[")
        df['review_views'] = split.str.get(1)
        split

        # ']' 제거
        split = df['review_views'].str.split("]")
        df['review_views'] = split.str.get(0)
        split

        # "'" 제거
        split = df['review_views'].str.split("'")
        df['review_views'] = split.str.get(1)
        split

        # "\n" 제거
        split = df['review_detail'].str.split("\n")
        df['review_detail'] = split.str.get(1)
        split

        # 결측값 제거 필요

        # pandas로 가공한 데이터 csv 파일로 다시 저장하기
        # df.to_csv('cheese_review_panda.csv')
        
        return df
