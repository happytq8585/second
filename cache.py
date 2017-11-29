#-*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import redis

from db import *

class A():
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def dis(self):
        print(self.a)
        print(self.b)

class Cache():
    def __init__(self):
        self.inst  = redis.Redis(host='localhost', port=6379, db=0)
    def set(self, k, v):
        self.inst.set(k, v)
    def get(self, k):
        r = self.inst.get(k)
        return r


if __name__ == '__main__':
    c = Cache()
    a = A(1,2)
    r = c.set('tq', a)
    r = c.get('tq')
    r.dis()
