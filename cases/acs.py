# encoding:utf-8
__author__ = 'xyc'

from locust.core import HttpLocust, TaskSet, task

import helper
from measure import timer


class Analysis(TaskSet):

    @task(3)
    def forecast(self):
        dsl = {
                    'uri': "/xxx",
                    'required': {
                        'uid': [4, 10, 119]
                    },
                    'optional': {
                        'group_field': ['LeadSource','kh_Type','kh_Industry','kh_Rating','Type','kh_Name'],
                        'tab' : [0, 1]
                    }
              }

        params = helper.create_request(**dsl)

        @timer(uri=dsl['uri'], params=str(params))
        def request():
            self.client.get(dsl['uri'], params=params)
        request()

    @task(6)
    def performance(self):
        dsl = {
                    'uri': "/xxx",
                    'required': {
                        'uid': [4, 10, 119]
                    },
                    'optional': {
                        'group_field': ['LeadSource','kh_Type','kh_Industry','kh_Rating','Type','kh_Name'],
                        'tab' : [0, 1],
                        'page' : (20, 200),
                        'num' : (20, 40),
                        'time_granule' : ['month', 'quanter']
                    }
                }

        params = helper.create_request(**dsl)

        @timer(uri=dsl['uri'], params=str(params))
        def request():
            self.client.get(dsl['uri'], params=params)
        request()

    @task(1)
    def notice(self):
        dsl = {
                    'uri': "/xxx",
                    'required': {
                        'uid': [4, 10, 119]
                    },
                    'optional': {
                        'ap_id': [101, 1]
                    }
                }

        params = helper.create_request(**dsl)

        @timer(uri=dsl['uri'], params=str(params))
        def request():
            self.client.post(dsl['uri'], data=params)
        request()

    @task(18)
    def filed_values(self):
        dsl = {
            'uri': "/xxx",
            'required': {
                'uid': [4, 10, 119],
                'id': [1,2,4,6,8,10,13,14,15,16,17,18,19,22,23]
            },
        }

        params = helper.create_request(**dsl)

        @timer(uri=dsl['uri'], params=str(params))
        def request():
            self.client.get(dsl['uri'], params=params)
        request()



class Acs(HttpLocust):
    host = 'http://xx.xx.xx.xxx:xx'
    task_set = Analysis
    min_wait = 5000
    max_wait = 9000


if __name__ == '__main__':
    Analysis().forecast()
