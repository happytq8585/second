#-*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from db import *

class UserOp():
    def __init__(self):
        self.impl    = User_impl()
    #return None or dict
    def check(self, name, passwd):
        r  = self.impl.query_user(name, passwd)
        return r
    def check_id(self, uid):
        r  = self.impl.query_user_by_id(uid)
        return r

    #所有信息联络员的信息
    def list_connectors(self):
        r  = self.impl.query_connector()
        return r

    #return 1=exists (name, passwd)   0=add successful
    def connector_add(self, city, name, passwd, gender, depart, place, tel, mobile):
        r  = self.check(name, passwd)
        if r:
            return conf.failed 
        r  = self.impl.connector_add(city, name, passwd, gender, depart, place, tel, mobile)
        return conf.success

    #return 1=exists (name, passwd) 0=del successful
    def connector_del(self, uid):
        r = self.check_id(uid)
        if not r:
            return conf.failed
        r = self.impl.connector_del(uid)
        return conf.success
        
class DepartmentOp():
    def __init__(self):
        self.impl     = Department_impl()
    def list_departments(self):
        r = self.impl.query_departments()
        a = [e.get('name') for e in r if e.get('name', None)]
        return a

class PositionOp():
    def __init__(self):
        self.impl     = Position_impl()
    def list_positions(self):
        r = self.impl.query_positions()
        a = [e.get('name') for e in r if e.get('name', None)]
        return a

class CityOp():
    def __init__(self):
        self.impl     = City_impl()
    def list_citys(self):
        r = self.impl.query_citys()
        a = [e.get('name') for e in r if e.get('name', None)]
        return a

class AuthOp():
    def __init__(self):
        self.impl     = Auth_impl()
    def list_auths(self):
        r = self.impl.query_auths()
        return r
    #return conf.success  conf.failed
    def add_auth(self, name):
        r = self.impl.add_auth(name)
        return r
    def del_auth_by_name(self, name):
        r = self.impl.del_auth_by_name(name)
        return r
    def del_auth_by_id(self, aid):
        r = self.impl.del_auth_by_id(aid)
        return r
    #授权
    def auth_by_arr(self, arr):
        r = self.impl.auth_by_arr(arr)
        return r

if __name__ == '__main__':
    d = DepartmentOp()
    p = PositionOp()

    r = d.list_departments()
    print(r)
    r = p.list_positions()
    print(r)
