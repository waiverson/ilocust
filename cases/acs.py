# encoding:utf-8
__author__ = 'xyc'

from locust.core import HttpLocust, TaskSet, task

import random

class AcsURI():
    host = '172.20.0.214:16004'
    satisfaction = "/WEBAPI/acs/data/analysis/satisfaction"
    performance = "/WEBAPI/acs/data/analysis/performance"
    time_granule = ['day','month','quarter','year']
    uid = [4,10,119]
    group_field = ['LeadSource','kh_Type','kh_Industry','kh_Rating','Type','kh_Name']
    tab = [0,1]
    page = (20,200)
    num = (20,40)

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

class RestPerformance():
    # def on_start(self):
    #     """ on_start is called when a Locust start before any task is scheduled """
    #     self.login()

    @task(4)
    def satisfaction(self):
        parmas = {'time_granule':'day','app_accts':'1:00528000001EsnhAAC,2:23888217',
                  'user_acct':"2215649033@qq.com",'start_time':'1411367308','biz_model':'1','subtype':'5','end_time':'1442903308'}
        response = self.client.get(AcsURI.satisfaction, params=parmas)

    def forecast(self):
        pass

    @task(2)
    def performance(self):
        def is_optional(tup):
            name, item = tup
            print type(item)
            return bool(
                not name.startswith('_')
                and not isinstance(item, str)
                and not name is not 'uid'
                )
        optional = list(filter(is_optional, vars(AcsURI).items()))
        params = {'uid': AcsURI.uid}
        for i in range(0, random.randint(len(optional))):
            params.update(optional)
        params.update(optional)
        response = self.client.get(AcsURI.performance ,params=params)

    # @task(3)
    # def forecast(self):
    #     pass
    #
    # @task(4)
    # def cache(self):
    #     pass

class Acs(HttpLocust):
    task_set = RestPerformance
    min_wait = 5000
    max_wait = 9000


if __name__ == '__main__':
    RestPerformance().performance()
