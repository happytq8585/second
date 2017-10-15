#-*- coding: utf-8 -*-

import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.options
import hashlib
import os.path
import json
import time
import datetime
import re

from tornado.web import StaticFileHandler
from tornado.options import define, options

define("port", default=8000, help="run on the given port", type=int)

from conf import conf
from session import Session
from data import *

userop         = UserOp()
departmentop   = DepartmentOp()
positionop     = PositionOp()
cityop         = CityOp()
authop         = AuthOp()

class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_cookie(conf.xr_cookie)

class IndexHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    @tornado.gen.engine
    def get(self):
        session      = Session(self, time.time() + conf.expires)
        if session[conf.login_status]:
            role = session[conf.role]
            connectors, depnames, posnames, auths, citys = yield tornado.gen.Task(self.__fetch_data)
            data = {'departments':depnames, 'positions': posnames, 'role': role, 'conf':conf, 
                    'citys':citys, 'connectors':connectors, 'auths':auths}
            print(auths)
            self.render(conf.main_tpl, data=data)
        else:
            self.render(conf.login_tpl, conf=conf)
    @tornado.gen.coroutine
    def __fetch_data(self):
            connectors = userop.list_connectors()
            depnames = departmentop.list_departments()
            posnames = positionop.list_positions()
            auths    = authop.list_auths()
            citys    = cityop.list_citys()
            return connectors, depnames, posnames, auths, citys


class LoginHandler(tornado.web.RequestHandler):
    def get(self):
        self.render(conf.login_tpl, conf=conf)
    @tornado.web.asynchronous
    @tornado.gen.engine
    def post(self):
        if conf.debug:
            print('LoginHandler post')
        name     = self.get_argument(conf.username, None)
        passwd   = self.get_argument(conf.password, None)
        if name and passwd:
            r    = yield tornado.gen.Task(self.__check_user, name, passwd)
            if r:
                session      = Session(self, time.time() + conf.expires)
                session[conf.username] = name
                session[conf.role]     = r.get('role', 0)
                session[conf.login_status] = True
                self.write(conf.succmsgcode)
                if conf.debug:
                    print(conf.succmsgcode)
            else:
                self.write(conf.errmsgcode)
                if conf.debug:
                    print(conf.errmsgcode)
        self.finish()
    @tornado.gen.coroutine
    def __check_user(self, name, passwd):
        r    = userop.check(name, passwd)
        return r

class AddConnectorHandler(BaseHandler):
    #添加信息联络员
    @tornado.web.authenticated
    @tornado.web.asynchronous
    @tornado.gen.engine
    def post(self):
        city           = self.get_argument('city', '')
        name           = self.get_argument('name', '')
        passwd         = self.get_argument('password', '')
        depart         = self.get_argument('department', '')
        place          = self.get_argument('place', '')
        telephone      = self.get_argument('telephone', '')
        mobile         = self.get_argument('mobile', '')
        gender         = self.get_argument('gender', '')
        print(city, name, passwd, depart, place, telephone, mobile, gender)
        r = yield tornado.gen.Task(self.__write_conn, city, name, passwd, depart, place, telephone, mobile, gender)
        if r == 0:
            self.write(conf.succmsgcode)
        else:
            self.write(conf.errmsgcode)
        self.finish()
    @tornado.gen.coroutine
    def __write_conn(self, ci, na, pa, de, pl, te, mo, ge):
        r = userop.connector_add(ci, na, pa, ge, de, pl, te, mo)
        return r

class DelConnectorHandler(BaseHandler):
    #删除信息联络员
    @tornado.web.authenticated
    @tornado.web.asynchronous
    @tornado.gen.engine
    def post(self):
        uid        = self.get_argument('uid', None)
        if not uid:
            self.write(conf.failed)
        else:
            r = yield tornado.gen.Task(self.__del_user, uid)
            if r == conf.success:
                self.write(conf.succmsgcode)
            else:
                self.write(conf.errmsgcode)
        self.finish()
    @tornado.gen.coroutine
    def __del_user(self, uid):
        r = userop.connector_del(uid)
        return r

class AddAuthHandler(BaseHandler):
    #添加权限
    @tornado.web.authenticated
    @tornado.web.asynchronous
    @tornado.gen.engine
    def post(self):
        name      = self.get_argument('name', None)
        if not name:
            self.write(conf.errmsgcode)
        else:
            r     = yield tornado.gen.Task(self.__add_auth, name)
            if r == conf.success:
                self.write(conf.succmsgcode)
            else:
                self.write(conf.errmsgcode)
        self.finish()
    @tornado.gen.coroutine
    def __add_auth(self, name):
        r = authop.add_auth(name)
        return r

class DelAuthHandler(BaseHandler):
    #删除权限
    @tornado.web.authenticated
    @tornado.web.asynchronous
    @tornado.gen.engine
    def post(self):
        aid      = self.get_argument('aid', None)
        if not aid:
            self.write(conf.errmsgcode)
        else:
            r     = yield tornado.gen.Task(self.__del_auth, aid)
            if r == conf.success:
                self.write(conf.succmsgcode)
            else:
                self.write(conf.errmsgcode)
        self.finish()
    @tornado.gen.coroutine
    def __del_auth(self, aid):
        r = authop.del_auth_by_id(aid)
        return r

class AuthHandler(BaseHandler):
    @tornado.web.authenticated
    @tornado.web.asynchronous
    @tornado.gen.engine
    def post(self):
        data      = self.get_argument('data', None)
        if not data:
            self.write(conf.errmsgcode)
        else:
            arr   = data.split(',')
            r     = yield tornado.gen.Task(self.__auth, arr)
            if r == conf.success:
                self.write(conf.succmsgcode)
            else:
                self.write(conf.errmsgcode)
        self.finish()

    @tornado.gen.coroutine
    def __auth(self, arr):
        r = authop.auth_by_arr(arr)
        return r

class LogoutHandler(tornado.web.RequestHandler):
    def get(self):
        self.clear_cookie(conf.xr_cookie)
        self.redirect('/')

if __name__ == "__main__":
    tornado.options.parse_command_line()
    settings = {
        "template_path": os.path.join(os.path.dirname(__file__), "templates"),
        "static_path": os.path.join(os.path.dirname(__file__), "static"),
        "cookie_secret": "cZJc2sWbQLKos6GkHn/QB9oXwQt8p0R0kRvJ5+xJ89E=",
        "xsrf_cookies": True,
        "login_url": "/login",
        "debug":True}
    handler = [
               (r"/static/(.*)", StaticFileHandler, {"path": "static"}),  
               (r"/css/(.*)", StaticFileHandler, {"path": "static/css"}),  
               (r"/js/(.*)", StaticFileHandler, {"path": "static/js"}),  
               (r"/image/(.*)", StaticFileHandler, {"path": "static/image"}), 
               (r'/', IndexHandler),
               (r'/login', LoginHandler),
               (r'/logout', LogoutHandler),
               (r'/addconnector', AddConnectorHandler),
               (r'/delconnector', DelConnectorHandler),
               (r'/addauth', AddAuthHandler),
               (r'/delauth', DelAuthHandler),
               (r'/authorize', AuthHandler),
              ]
    application = tornado.web.Application(handler, **settings)
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
