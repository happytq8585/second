#-*- coding: utf-8 -*-
import hashlib
import time

from conf import conf

container = {}

class Session():
    def __init__(self, handler, expires):
        '''
        handler:      RequestHandler
        expire:       cookie expired time in seconds
        '''
        self.handler      = handler
        self.expires      = expires
        self.random_str   = None

    def __gen_random(self):
        obj = hashlib.md5()
        t   = self.handler.request.remote_ip
        obj.update(t)
        random_str = obj.hexdigest()
        return random_str

    def __setitem__(self, k, v):
        if not self.random_str:
            random_str      = self.handler.get_cookie(conf.xr_cookie)
            if not random_str:
                random_str  = self.__gen_random()
                container[random_str] = {}
            else:
                if random_str in container.keys():
                    pass
                else:
                    random_str = self.__gen_random()
                    container[random_str] = {}
            self.random_str = random_str
        container[self.random_str][k] = v
        container[self.random_str][conf.session_time] = int(time.time())
        self.handler.set_cookie(conf.xr_cookie, self.random_str, expires=None)

    def __getitem__(self, k):
        random_str       = self.handler.get_cookie(conf.xr_cookie)
        if not random_str:
            return None
        user_info_dict   = container.get(random_str, None)
        if not user_info_dict:
            return None
        t                = user_info_dict.get(conf.session_time, None)
        if not t:
            del container[random_str]
            self.handler.clear_cookie(conf.xr_cookie)
            return None
        now              = int(time.time())
        if t + self.expires < now:
            del container[random_str]
            self.handler.clear_cookie(conf.xr_cookie)
            return None
        v                = user_info_dict.get(k, None)
        return v    
