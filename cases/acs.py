# encoding:utf-8
__author__ = 'xyc'

from locust.core import HttpLocust, TaskSet, task

from config import Global
class Config(Global):
    pass

satisfaction_url = "/WEBAPI/acs/data/analysis/satisfaction"
performance_url = "/WEBAPI/acs/data/analysis/performance"



class RestPerformance(TaskSet):
    # def on_start(self):
    #     """ on_start is called when a Locust start before any task is scheduled """
    #     self.login()

    @task(4)
    def satisfaction(self):
        parmas = {'time_granule':'day','app_accts':'1:00528000001EsnhAAC,2:23888217',
                  'user_acct':"2215649033@qq.com",'start_time':'1411367308','biz_model':'1','subtype':'5','end_time':'1442903308'}
        response = self.client.get(satisfaction_url,params=parmas)

    @task(2)
    def performance(self):
        params = {'time_granule':'month','uid':"4",'group_field':'kh_Industry','fiscal_year':'2013'}
        response = self.client.get(performance_url ,params=params)

    # @task(3)
    # def forecast(self):
    #     pass
    #
    # @task(4)
    # def cache(self):
    #     pass

class ACSUser(HttpLocust):
    task_set = RestPerformance
    min_wait = 5000
    max_wait = 9000

