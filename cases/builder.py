# encoding:utf-8
__author__ = 'xyc'

import random, json
from abc import ABCMeta, abstractmethod

class AbstractRequestBuilder(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def build_params(self,):
        return NotImplementedError()

    def build_addr(self, ):
        return NotImplementedError()


class URIBuilder(AbstractRequestBuilder):

    def __init__(self, dsl):
        """
    :param:dsl: HTTP请求构造所需参数，必需包含:uri,required，可选包含optional
    :example {'uri':'/example/index/','required':{k:v,...},'optional':{k:v,k:v,...}}
        """
        self.dsl = json.loads(dsl)

    def build_params(self,):
        # 随机生成访问参数
        required = self.dsl["required"] if self.dsl.has_key('required') else {}
        if self.dsl.has_key("optional"):
            optional = self.dsl["optional"]
            for i in range(0, random.randint(0, len(optional))):
                key = random.choice(optional.keys())
                required.update({key: optional[key]})
        return URIBuilder.extract(**required)

    def build_addr(self,):
        if self.dsl.has_key('uri'):
            return self.dsl['uri']
        else:
            raise NameError, "uri is required!"

    @classmethod
    def extract(cls, **kwargs):
        # 随机构造访问参数
        params = {}
        for k, v in kwargs.items():
            if isinstance(v, list):
                params[k] = random.choice(v)
            if isinstance(v, tuple):
                params[k] = random.randint(v[0], v[1])
        return params

    @classmethod
    def is_optional(cls,tup,):
        name, item = tup
        return bool(
            not name.startswith('_')
            and not isinstance(item, str)
            and not isinstance(item, classmethod)
            )

