# encoding:utf-8
__author__ = 'xyc'

from locust.core import HttpLocust, TaskSet, task

class UserBehavior(TaskSet):
    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        self.login()

    @task(2)
    def acs(self):
        parmas = {'time_granule':'day','app_accts':'1:00528000001EsnhAAC,2:23888217',
                  'user_acct':"2215649033@qq.com",'start_time':'1411367308','biz_model':'1','subtype':'5','end_time':'1442903308'}
        response = self.client.get("/WEBAPI/acs/data/analysis/satisfaction",params=parmas)

    def login(self):
        print "ready to request acs server"

    @task(1)
    def profile(self):
        params = {'time_granule':'month','uid':"4",'group_field':'kh_Industry','fiscal_year':'2013'}
        response = self.client.get("/WEBAPI/acs/data/analysis/performance",params=params)

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000

