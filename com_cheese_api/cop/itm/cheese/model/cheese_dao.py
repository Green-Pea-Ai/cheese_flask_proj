# from com_cheese_api.cop.chs.model.cheese_dto import CheeseDto
from com_cheese_api.cop.itm.cheese.model.cheese_dto import CheeseDto, CheeseVo
from com_cheese_api.cop.itm.cheese.model.cheese_dfo import CheeseDfo
from com_cheese_api.ext.db import url, db, openSession, engine
from com_cheese_api.cmm.utl.file import FileReader

from sqlalchemy import func, and_, or_

from flask import request, Response, jsonify
from flask_restful import Resource, reqparse

import pandas as pd
import numpy as np
import json
import os
import sys
from typing import List
from pathlib import Path


Session = openSession()
session = Session()

class CheeseDao(CheeseDto):

    # @classmethod
    # def bulk(cls, cheese_dfo):
    #     # cheeseDfo = CheeseDfo()
    #     # df = CheeseDfo.new()
    #     dfo = cheese_dfo.create()
    #     print(dfo.head())
    #     session.bulk_insert_mappings(cls, dfo.to_dict(orient="records"))
    #     session.commit()
    #     session.close()

    @staticmethod
    def bulk():
        print("========cheese DAO 1========")
        cheeseDfo = CheeseDfo()
        df = cheeseDfo.cheese_df()
        print("========cheese DAO 2========")
        print(df.head())
        session.bulk_insert_mappings(CheeseDto, df.to_dict(orient="records"))
        session.commit()
        session.close()


    @staticmethod
    def save(cheese):
        Session = openSession()
        session = Session()
        session.add(cheese)
        session.commit()


    @classmethod
    def find_all(cls):
        #cheese = session.query(CheeseVo).all()
        return cls.query.all()

    @classmethod
    def find_one(cls, cheese_id):
        return session.query(cls)\
            .filter(cls.cheese_id == cheese_id).one()

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name == name).all()

    @classmethod
    def find_by_cheese_id(cls, cheese_id):
        return cls.query.filter_by(cheese_id == cheese_id).first()


    @classmethod
    def update(cls, cheese):
        session.query(cls).filter(cls.cheese_id == cheese['cheese_id'])\
            .update({cls.ranking:cheese['ranking'],\
                cls.category:cheese['category'],\
                cls.brand:cheese['brand'],\
                cls.name:cheese['name'],\
                cls.content:cheese['content'],\
                cls.texture:cheese['texture'],\
                cls.types:cheese['types'],\
                cls.price:cheese['price'],\
                cls.img:cheese['img']})
        session.commit()


    @classmethod
    def delete(cls, cheese_id):
        cheese = cls.query.get(cheese_id)
        db.session.delete(cheese)
        db.session.commit()


# if __name__ == '__main__':
#     CheeseDao.bulk()