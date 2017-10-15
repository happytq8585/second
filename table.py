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
    def __init__(self, name, pwd, mb, tel, email, ava, city, depart, place, gender, role):
        self.name               = name
        self.password           = pwd
        self.mobile             = mb
        self.telephone          = tel
        self.email              = email
        self.avatar             = ava
        self.city               = city
        self.department         = depart
        self.place              = place
        self.gender             = gender
        self.role               = role
    def dic_return(self):
        return {'id':        self.id,
                'name':      '' if not self.name          else str(self.name),
                'password':  '' if not self.password      else str(self.password),
                'mobile':    '' if not self.mobile        else str(self.mobile),
                'telephone': '' if not self.telephone     else str(self.telephone), 
                'email':     '' if not self.email         else str(self.email),
                'avatar':    '' if not self.avatar        else str(self.avatar),
                'city':      '' if not self.city          else str(self.city),
                'department':'' if not self.department    else str(self.department),
                'place':     '' if not self.place         else str(self.place),
                'gender':    '男' if self.gender == 0 else '女' if self.gender == 1 else 'unknown',
                'role':      self.role}
    id            = Column(Integer, primary_key=True)
    name          = Column(String(64))
    password      = Column(String(512))
    mobile        = Column(String(16))
    telephone     = Column(String(16))
    email         = Column(String(16))
    avatar        = Column(String(512))
    department    = Column(String(64))
    city          = Column(String(32))
    place         = Column(String(128))
    gender        = Column(Integer)
    role          = Column(Integer)

class Department(Base):
    __tablename__ = conf.department
    def __init__(self, name):
        self.name = name
    id            = Column(Integer, primary_key=True)
    name          = Column(String(128))
    def dic_return(self):
        return {'id': self.id,
                'name': '' if not self.name else str(self.name)}

class Position(Base):
    __tablename__ = conf.position
    def __init__(self, name):
        self.name = name
    id            = Column(Integer, primary_key=True)
    name          = Column(String(128))
    def dic_return(self):
        return {'id': self.id,
                'name': '' if not self.name else str(self.name)}

class City(Base):
    __tablename__ = conf.city
    def __init__(self, name):
        self.name = name
    id            = Column(Integer, primary_key=True)
    name          = Column(String(128))
    def dic_return(self):
        return {'id': self.id,
                'name': '' if not self.name else str(self.name)}

class Auth(Base):
    __tablename__ = conf.auth
    def __init__(self, name, tag):
        self.name = name
        self.tag  = tag
    id            = Column(Integer, primary_key=True)
    name          = Column(String(32))
    tag           = Column(Integer)
    def dic_return(self):
        return {'id':   self.id,
                'name': '' if not self.name else str(self.name),
                'tag':  self.tag}

if __name__ == '__main__':
    u   = User('tq', '123', '123123', '', '', '', 'chengdu', '', 0, 2)
    print(u.dic_return())
