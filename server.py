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
from conf import conf

define("port", default=conf.port, help="run on the given port", type=int)


class LoginHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    @tornado.gen.engine
    def post(self):
        name   = self.get_argument('name', None)
        passwd = self.get_argument('passwd', None)
        if not name and not passwd:
            self.write({'code':'-1', 'msg':''})
        else:
            pass
if __name__ == "__main__":
    tornado.options.parse_command_line()
    settings = {
        "cookie_secret": "cZJc2sWbQLKos6GkHn/QB9oXwQt8p0R0kRvJ5+xJ89E=",
        "xsrf_cookies": True,
        "debug":False}
    handler = [
               (r'/login', LoginHander),
              ]
    application = tornado.web.Application(handler, **settings)
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
