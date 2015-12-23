# encoding:utf-8
__author__ = 'xyc'

import random

class URLs(object):

    @classmethod
    def parameter(*args):
        # 随机构造访问参数
        params = {}

        def extract(k, v):
            if isinstance(v, list):
                params[k] = random.choice(v)
            if isinstance(v, tuple):
                params[k] = random.randint(min=v[0], max=v[1])

        for arg in args:
            extract(arg[0], arg[1])
        return params

    def cost_time(self):
        pass

    @classmethod
    def is_param(tup):
        name, item = tup
        print type(item)
        return bool(
            not name.startswith('_')
            and not isinstance(item, str)
            )

if __name__ == "__main__":
    print random.randint(URLs.page[0],URLs.page[1])


