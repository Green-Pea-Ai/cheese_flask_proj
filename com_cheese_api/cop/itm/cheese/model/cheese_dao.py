# from com_cheese_api.cop.chs.model.cheese_dto import CheeseDto
from com_cheese_api.cop.itm.cheese.model.cheese_dto import CheeseDto
from com_cheese_api.cop.itm.cheese.model.cheese_dfo import CheeseDfo
from com_cheese_api.ext.db import url, db, openSession, engine
from com_cheese_api.util.file import FileReader

from sqlalchemy import func
from sqlalchemy import and_, or_

from flask import request
from flask import Response, jsonify
from flask_restful import Resource, reqparse

from sklearn.ensemble import RandomForestClassifier # rforest
from sklearn.tree import DecisionTreeClassifier # dtree
from sklearn.ensemble import RandomForestClassifier # rforest
from sklearn.naive_bayes import GaussianNB # nb
from sklearn.neighbors import KNeighborsClassifier # knn
from sklearn.svm import SVC # svm
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold  # k value is understood as count
from sklearn.model_selection import cross_val_score

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
    # def bulk(cls, CheeseDfo):
    #     cheeseDfo = CheeseDfo()
    #     df = CheeseDfo.new()
    #     print(df.head())
    #     session.bulk_insert_mappings(CheeseDto, df.to_dict(orient="records"))
    #     session.commit()
    #     session.close()


    @staticmethod
    def bulk():
        cheeseDfo = CheeseDfo()
        df = CheeseDfo.new()
        print(df.head())
        session.bulk_insert_mappings(CheeseDto, df.to_dict(orient="records"))
        session.commit()
        session.close()


    # @classmethod
    # def find_all(cls):
    #     return cls.query.all()

    # @classmethod
    # def find_by_name(cls, name):
    #     return cls.query.filter_by(name == name).all()

    # @classmethod
    # def find_by_id(cls, id):
    #     return cls.query.filter_by(id == id).first()


# if __name__ == '__main__':
#     CheeseDao.bulk()