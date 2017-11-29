#-*- coding: utf-8 -*-

import time
import hashlib

from sqlalchemy import Column, String, Integer, Date, TIMESTAMP, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

import sys
sys.path.append('..')
reload(sys)
from conf import conf

sys.setdefaultencoding('utf-8')

Base = declarative_base()

    
class User(Base):
    __tablename__ = conf.user
    def __init__(self, id_, name, password, mobile, email, avatar, city, hometown, gender, role, money):
        self.id       = id_
        self.name     = name
        self.password = password
        self.mobile   = mobile
        self.email    = email
        self.avatar   = avatar
        self.city     = city
        self.hometown = hometown
        self.gender   = gender
        self.role     = role
        self.money    = money
    id            = Column(Integer, primary_key=True)
    name          = Column(String(64))
    password      = Column(String(16))
    mobile        = Column(String(16))
    email         = Column(String(64))
    avatar        = Column(String(128))
    city          = Column(String(32))
    hometown      = Column(String(32))
    gender        = Column(String(1))
    role          = Column(Integer)
    money         = Column(Integer)

    def dis(self):
        print(self.id)
        print(self.name)
        print(self.password)
        print(self.mobile)
        print(self.email)
        print(self.avatar)
        print(self.city)
        print(self.hometown)
        print(self.gender)
        print(self.role)
        print(self.money)
