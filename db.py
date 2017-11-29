#-*- coding: utf-8 -*-

import time
import hashlib

from sqlalchemy import Column, String, Integer, Date, TIMESTAMP, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

import sys
reload(sys)
from conf import conf

sys.setdefaultencoding('utf-8')


db_url = 'mysql+mysqlconnector://' + str(conf.db_user) + ':' + conf.db_password + '@' + conf.db_server + ':' + str(conf.db_port) + '/' + conf.db_db

engine = create_engine(db_url, encoding=conf.db_encode)

DBSession = sessionmaker(bind=engine)

from table import *

engine = create_engine(db_url, encoding=conf.db_encode)
DBSession = sessionmaker(bind=engine)

class UserOp():
    def adduser(self, id_, name, password, mobile, email, avatar, city, hometown, gender,     role, money):
        o = User(id_, name, password, mobile, email, avatar, city, hometown, gender, role, money)
        try:
            S = DBSession()
            S.add(o)
            S.commit()
            S.close()
            return True
        except:
            return False
    def query_user(self, name, passwd):
        S = DBSession()
        r = S.query(User).filter(User.name == name).filter(User.password == passwd).all()
        S.close()
        return None if not r else r[0]
        


if __name__ == '__main__':
    u = UserOp()
    r = u.adduser(1, 'tq', '123', '1234567', '', '', 'chengdu', 'mianyang', '1', 0, 0)
    if not r:
        print('add failed')
    else:
        print('add success')
    r = u.query_user('tq', '123')
    if r:
        r.dis()
