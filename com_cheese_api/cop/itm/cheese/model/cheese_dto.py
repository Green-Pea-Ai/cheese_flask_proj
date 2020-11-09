from com_cheese_api.ext.db import url, db, openSession, engine
# from com_cheese_api.util.file import FileReader
from com_cheese_api.cmm.utl.file import FileReader

from sqlalchemy import func
from sqlalchemy import and_, or_

from flask import request
from flask import Response, jsonify
from flask_restful import Resource, reqparse

import pandas as pd
import numpy as np
import json
import os
import sys
from typing import List
from pathlib import Path


class CheeseDto(db.Model):
    __tablename__='cheeses'
    __table_args__={'mysql_collate':'utf8_general_ci'}

    cheese_id : str = db.Column(db.String(30), primary_key=True, index=True)
    ranking : int = db.Column(db.Integer)
    category: int = db.Column(db.Integer)
    types : int = db.Column(db.Integer)
    brand : str = db.Column(db.String(30))
    texture : str = db.Column(db.String(30))
    img : str = db.Column(db.String(255))


    # dairy = db.relationship('DiaryDto', lazy='dynamic')
    # orders = db.relationship('OrderDto', back_populates='cheese', lazy='dynamic')
    # prices = db.relationship('PriceDto', back_populates='cheese', lazy='dynamic')

    def __init__(self, cheese_id, ranking, category, types, brand, texture, img): 
        self.cheese_id = cheese_id
        self.ranking = ranking
        self.category = category
        self.types = types
        self.brand = brand
        self.texture = texture
        self.img = img

    def __repr__(self):
        return f'cheese(cheese_id={self.cheese_id}, ranking={self.ranking}, category={self.category}, \
                    types={self.types}, brand={self.brand}, texture={self.texture}, img={self.img})'

    def __str__(self):
        return f'cheese(cheese_id={self.cheese_id}, ranking={self.ranking}, category={self.category}, \
                    types={self.types}, brand={self.brand}, texture={self.texture}, img={self.img})'

    @property
    def json(self):
        return {
            'cheese_id':self.cheese_id, 
            'ranking':self.ranking, 
            'category':self.category,
            'types':self.types,
            'texture':self.types,
            'brand':self.brand,
            'img':self.img
        }

class CheeseVo(object):
    cheese_id : 0
    ranking : 0
    category: 0
    types : 0
    brand : ''
    texture : ''
    img : ''