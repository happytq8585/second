#-*- coding: utf-8 -*-

import ConfigParser

class Conf():
    def __init__(self, name):
        p = ConfigParser.ConfigParser()
        p.read(name)
        self.port          = p.getint('sys', 'port')

        self.user          = p.get('table', 'user')

        self.db_server     = p.get('mysql', 'db_server')
        self.db_port       = p.getint('mysql', 'db_port')
        self.db_user       = p.get('mysql', 'db_user')
        self.db_password   = p.get('mysql', 'db_password')
        self.db_db         = p.get('mysql', 'db_db')
        self.db_encode     = p.get('mysql', 'db_encode')
    def dis(self):
        print(self.port)

        print(self.user)

        print(self.db_server)
        print(self.db_port)
        print(self.db_user)
        print(self.db_password)
        print(self.db_db)
        print(self.db_encode)

conf = Conf('./conf.txt')

if __name__ == '__main__':
    conf.dis()
