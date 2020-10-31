from typing import List
from flask import request
from flask_restful import Resource, reqparse
from sklearn.ensemble import RandomForestClassifier # rforest
from sklearn.tree import DecisionTreeClassifier # dtree
from skelarn.ensemble import RandomForestClassifier # rforest
from sklearn.naive_bayes import GaussianNB # nb
from sklearn.neighbors import KNeighborsClassifier # knn
from sklearn.svm import SVC # svm
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold # k value is understood as count
from sklearn.model_selection import cross_val_score
from sqlalchemy import func
from pathlib import Path
from sqlalchemy import and_, or_
from com_cheese_api.util.file import FileReader
from flask import jsonify
from com_cheese_api.ext.db import db, openSession

import json
import pandas as pd
import json
import os
import numpy as np


"""
context: /Users/bitcamp/cheese_emp
fname: 
PassengerId
Survived: The answer that a machine learning model should match 
Pclass: Boarding Pass 1 = 1st-class seat, 2 = 2nd, 3 = 3rd,
Name,
Sex,
Age,
SibSp accompanying brothers, sisters, spouses
Parch accompanying parents, children,
Ticket : Ticket Number
Fare : Boarding Charges
Cabin : Room number
Embarked : a Port Name on Board C = Cherbourg, Q = Queenstown, S = Southhampton
"""
# ==============================================================
# ====================                     =====================
# ====================    Preprocessing    =====================
# ====================                     =====================
# ==============================================================

class UserDf(object):
    def __init__(self):
        self.fileReader = FileReader()
        self.data = os.path.join(os.path.abspath(os.path.dirname(__file__))+'\\data')
        self.odf = None

    def new(self):
        train = 'train.csv'
        test = 'test.csv'
        this = self.fileReader
        this.train = self.new_model(train) # payload
        this.test = self.new_model(test) # payload

        '''
        Original Model Generation
        '''  
        self.odf = pd.DataFrame(

            {
                'user_id' : this.train.PassengerId,
                'password' : '1',
                'name' : this.train.Name
            }
        )

        this.id = this.test['PassengerId'] # This becomes a question.
        # print(f'Preprocessing Train Variable : {this.train.columns}')
        # print(f'Preprocessing Train Variable : {this.test.columns}')
        this = self.drop_feature(this, 'Cabin')
        this = self.drop_feature(this, 'Ticket')
        # print(f'Post-Drop Variable : {this.train.columns}')
        this = self.embarked_nominal(this)
        # print(f'Preprocessing Embarked Variable : {this.train.head()}')
        this = self.title_nominal(this)
        # print(f'Preprocessing Train Variable : {this.train.head()}')
        '''
        The name is unnecessary because we extracted the Title from the name variable.
        '''
        this = self.drop_feature(this, 'Name')
        this = self.drop_feature(this, 'PassengerId')
        this = self.age_ordinal(this)
        # print(f'Preprocessing Age Variable : {this.train.head()}')
        this = self.drop_feature(this, 'SibSp')
        this = self.sex_nominal(this)
        # print(f'Preprocessing Sex Variable : {this.train.head()}')
        this = self.fareBand_nominal(this)
        # print(f'Preprocessing Fare Variable : {this.train.head()}')
        this = self.drop_feature(this, 'Fare')
        # print(f'Preprocessing Train Result : {this.train.head()}')
        # print(f'Preprocessing Test Result : {this.test.head()}')
        # print(f'Train NA Check : {this.train.isnull().sum()}')
        # print(f'Test NA Check : {this.test.isnull().sum()}')
        this.label = self.create_label(this) # payload
        this.train = self.create_train(this) # payload
        # print(f'Train Variable : {this.test.isnull().sum()}')
        # print(f'Test Variable : {this.test.isnull().sum()}')
        clf = RandomForestClassifier()
        clf.fit(this.train, this.label)
        prediction = clf.predict(this.test)

        # print(this)
        df = pd.DataFrame(

            {
                'pclass': this.train.Pclass,
                'gender': this.train.Sex,
                'age_group': this.train.AgeGroup,
                'embarked': this.train.
            }
        )








