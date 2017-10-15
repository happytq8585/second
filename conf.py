#-*- coding: utf-8 -*-

import ConfigParser

class Conf():
    def __init__(self, name):
        p = ConfigParser.ConfigParser()
        p.read(name)
        self.cache         = p.getint('sys', 'cache')
        self.debug         = p.getint('sys', 'debug')
        self.errcode      = p.getint('sys', 'errcode')
        self.errmsgcode    = p.get('sys', 'errmsgcode')
        self.success       = p.getint('sys', 'success')
        self.failed        = p.getint('sys', 'failed')
        self.succmsgcode   = p.get('sys', 'succmsgcode')

        self.index_title   = p.get('tpl', 'index_title')
        self.main_tpl      = p.get('tpl', 'main_tpl')
        self.login_tpl     = p.get('tpl', 'login_tpl')
        self.index_tpl     = p.get('tpl', 'index_tpl')

        self.xr_cookie     = p.get('session', 'xr_cookie')
        self.expires       = p.getint('session', 'expires')
        self.login_status  = p.get('session', 'login_status')
        self.session_time  = p.get('session', 'session_time')

        self.username      = p.get('client', 'username')
        self.password      = p.get('client', 'password')
        self.role          = p.get('client', 'role')
        self.maintain_role = p.getint('client', 'maintain_role')
        self.connector_role= p.getint('client', 'connector_role')
        self.reader_role   = p.getint('client', 'reader_role')

        self.user          = p.get('table', 'user')
        self.department    = p.get('table', 'department')
        self.position      = p.get('table', 'position')
        self.city          = p.get('table', 'city')
        self.auth          = p.get('table', 'auth')

        self.db_server     = p.get('mysql', 'db_server')
        self.db_port       = p.getint('mysql', 'db_port')
        self.db_user       = p.get('mysql', 'db_user')
        self.db_password   = p.get('mysql', 'db_password')
        self.db_db         = p.get('mysql', 'db_db')
        self.db_encode     = p.get('mysql', 'db_encode')
    def display(self):
        print('cache=%d' % self.cache)
        print('debug=%d' % self.debug)

        print('login_tpl=%s' % self.login_tpl)
        print('index_tpl=%s' % self.index_tpl)

        print('xr_cookie=%s' % self.xr_cookie)
        print('expires=%d' % self.expires)
        print('login_status=%s' % self.login_status)

conf = Conf('./conf.txt')

if __name__ == '__main__':
    conf.display()
