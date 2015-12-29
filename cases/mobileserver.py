# encoding:utf-8
__author__ = 'xyc'

from locust.core import HttpLocust, TaskSet, task

import json
from measure import timer
from builder import URIBuilder


class Mobile(TaskSet):

    header = {'IF-VERSION': '1.0'}

    @classmethod
    def create_request(cls, **kwargs):

        return URIBuilder(json.dumps(kwargs)).build_params()

    def on_start(self):

        """ on_start is called when a Locust start before any task is scheduled """
        dsl = {
                    'uri': "/WEBAPI/auth/accessToken/",
                    'required': {
                    'user':'2215649033@qq.com','password':'123456@a','domain':'987654321','platform':'mobile'
                    },
        }
        if not Mobile.header.has_key('SESSION-TOKEN'):
            params = Mobile.create_request(**dsl)
            r = self.client.post(dsl['uri'], data=params)
            self.header['SESSION-TOKEN'] = json.loads(r.text)['result']['token']

    @task(1)
    def app_account(self):
        dsl = {
                'uri': "/WEBAPI/appserver/app-account/",
        }

        params = Mobile.create_request(**dsl)

        @timer(uri=dsl['uri'], params=str(params))
        def request():
            self.client.get(dsl['uri'], headers=Mobile.header, params=params)
        request()

    @task(1)
    def view_list(self):
        dsl = {
                'uri': "/WEBAPI/appserver/view/list",
                'optional': {
                            'view_type': 'Sales'
                        }
        }

        params = Mobile.create_request(**dsl)

        @timer(uri=dsl['uri'], params=str(params))
        def request():
            self.client.get(dsl['uri'], headers=Mobile.header, params=params)
        request()

    @task(1)
    def me(self):
        dsl = {
                'uri': "/WEBAPI/appserver/me/",
        }

        params = Mobile.create_request(**dsl)

        @timer(uri=dsl['uri'], params=str(params))
        def request():
            self.client.get(dsl['uri'], headers=Mobile.header, params=params)
        request()

    @task(1)
    def fetchall(self):
        dsl = {
                'uri': "/WEBAPI/appserver/me/fetchall",
        }

        params = Mobile.create_request(**dsl)

        @timer(uri=dsl['uri'], params=str(params))
        def request():
            self.client.get(dsl['uri'], headers=Mobile.header, params=params)
        request()

    @task(1)
    def contact(self):
        dsl = {
                'uri': "/WEBAPI/appserver/org/contact",
        }

        params = Mobile.create_request(**dsl)

        @timer(uri=dsl['uri'], params=str(params))
        def request():
            self.client.get(dsl['uri'], headers=Mobile.header, params=params)
        request()

    @task(1)
    def filter(self):
        dsl = {
                'uri': "/WEBAPI/appserver/view/filter",
                'optional': {
                                'xt_view_id': 1
                            }
        }

        params = Mobile.create_request(**dsl)

        @timer(uri=dsl['uri'], params=str(params))
        def request():
            self.client.get(dsl['uri'], headers=Mobile.header, params=params)
        request()

    @task(15)
    def field_values(self):
        dsl = {
                'uri': "/WEBAPI/appserver/view/fieldvalues",
                'optional': {
                                'id': 1
                            }
        }

        params = Mobile.create_request(**dsl)

        @timer(uri=dsl['uri'], params=str(params))
        def request():
            self.client.get(dsl['uri'], headers=Mobile.header, params=params)
        request()

    @task(3)
    def performance(self):
        dsl = {
                'uri': "/WEBAPI/appserver/data/analyses/performance",
                'optional': {
                        'group_field': ['LeadSource','kh_Type','kh_Industry','kh_Rating','Type','kh_Name'],
                        'tab' : [0, 1],
                        'page' : (20, 200),
                        'num' : (20, 40),
                        'time_granule' : ['month','quanter']
                }
        }

        params = Mobile.create_request(**dsl)

        @timer(uri=dsl['uri'], params=str(params))
        def request():
            self.client.get(dsl['uri'], headers=Mobile.header, params=params)
        request()

    @task(3)
    def forecast(self):
        dsl = {
                'uri': "/WEBAPI/appserver/data/analyses/forecast",
                'optional': {
                        'group_field': ['LeadSource','kh_Type','kh_Industry','kh_Rating','Type','kh_Name'],
                        'tab' : [0, 1]
                }
        }

        params = Mobile.create_request(**dsl)

        @timer(uri=dsl['uri'], params=str(params))
        def request():
            self.client.get(dsl['uri'], headers=Mobile.header, params=params)
        request()

    @task(1)
    def info(self):
        dsl = {
                'uri': "/WEBAPI/appserver/view/info",
                'optional': {
                        'xt_view_id': [1, 2],
                }
        }

        params = Mobile.create_request(**dsl)

        @timer(uri=dsl['uri'], params=str(params))
        def request():
            self.client.get(dsl['uri'], headers=Mobile.header, params=params)
        request()

class Portal(HttpLocust):
    host = 'http://172.20.0.214:16001'
    task_set = Mobile
    min_wait = 5000
    max_wait = 9000

if __name__ == '__main__':
    Mobile().app_account()