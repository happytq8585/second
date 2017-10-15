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

from table import *

sys.setdefaultencoding('utf-8')

db_url = 'mysql+mysqlconnector://' + str(conf.db_user) + ':' + conf.db_password + '@' + conf.db_server + ':' + str(conf.db_port) + '/' + conf.db_db

engine = create_engine(db_url, encoding=conf.db_encode)

DBSession = sessionmaker(bind=engine)

class User_impl():
    def __init__(self):
        self.S     = DBSession()
    def __del__(self):
        self.S.close()

    #从数据库查看(name, password)是否存在
    def query_user(self, name, password):
        r = self.S.query(User).filter(User.name == name).filter(User.password == password).first()
        return {} if not r else r.dic_return()
    #根据id查看用户
    def query_user_by_id(self, uid):
        r = self.S.query(User).filter(User.id == uid).first()
        return {} if not r else r.dic_return()

    #查询所有信息联络员信息, 供业务维护员使用
    def query_connector(self):
        r = self.__query_role(conf.connector_role)
        return r
    #添加一个信息联络员
    def connector_add(self, city, name, passwd, gender, depart, place, tel, mobile):
        u = User(name, passwd, mobile, tel, '', '', city, depart, place, gender, 1)
        r = self.S.add(u)
        r = self.S.commit()
        return r
    #删除一个信息联络员
    def connector_del(self, uid):
        r = self.S.query(User).filter(User.id == uid).delete(synchronize_session=False)
        r = self.S.commit()
        return r
    #查询所有查询员信息, 供信息联络员使用
    def query_reader(self):
        r = self.__query_role(conf.reader_role)
        return r
    def __query_role(self, role):
        r = self.S.query(User).filter(User.role == role).all()
        return [] if not r else [e.dic_return() for e in r]

class Department_impl():
    def __init__(self):
        self.S    = DBSession()
    def __del__(self):
        self.S.close()
    #查询所有的部门名字
    def query_departments(self):
        r = self.S.query(Department).all()
        return [] if not r else [e.dic_return() for e in r]

class Position_impl():
    def __init__(self):
        self.S    = DBSession()
    def __del__(self):
        self.S.close()
    #查询所有的职称名字
    def query_positions(self):
        r = self.S.query(Position).all()
        return [] if not r else [e.dic_return() for e in r]

class City_impl():
    def __init__(self):
        self.S    = DBSession()
    def __del__(self):
        self.S.close()
    #查询所有的城市名字
    def query_citys(self):
        r = self.S.query(City).all()
        return [] if not r else [e.dic_return() for e in r]

class Auth_impl():
    def __init__(self):
        self.S    = DBSession()
    def __del__(self):
        self.S.close()
    #查询所有的权限名字
    def query_auths(self):
        r = self.S.query(Auth).all()
        return [] if not r else [e.dic_return() for e in r]
    #根据权限名字查询
    def query_auth_by_name(self, name):
        r = self.S.query(Auth).filter(Auth.name == name).first()
        return {} if not r else r.dic_return()
    #根据权限id查询
    def query_auth_by_id(self, aid):
        r = self.S.query(Auth).filter(Auth.id == aid).first()
        return {} if not r else r.dic_return()
    #添加权限 return 1=exist 0=add success
    def add_auth(self, name):
        r = self.query_auth_by_name(name)
        if r:
            return conf.failed
        auth = Auth(name, 0)
        r = self.S.add(auth)
        r = self.S.commit()
        return conf.success

    #根据权限名字删除权限
    def del_auth_by_name(self, name):
        r = self.S.query(Auth).filter(Auth.name == name).delete(synchronize_session=False)
        r = self.S.commit()
        return conf.success

    #根据权限id删除权限
    def del_auth_by_id(self, aid):
        r = self.S.query(Auth).filter(Auth.id == aid).delete(synchronize_session=False)
        r = self.S.commit()
        return conf.success

    #授权
    def auth_by_arr(self, arr):
        if not arr:
            return conf.success
        r  = self.S.query(Auth).all()
        if not r:
            return conf.success
        arr = [int(e) for e in arr]
        for e in r:
            id_ = e.id
            tag = 1 if id_ in arr else 0
            self.S.query(Auth).filter(Auth.id == id_).update({Auth.tag: tag})
        self.S.commit()
        return conf.success

if __name__ == '__main__':
    name = 'admin'
    password = '123'
    u = User_impl()
    r = u.query_user(name, password)
    print(r)
    a = r['place']
    a = a.decode(encoding='utf-8', errors='strict')
    print(a)
