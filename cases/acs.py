# encoding:utf-8
__author__ = 'xyc'

from locust.core import HttpLocust, TaskSet, task

import json
from measure import timer
from builder import URIBuilder


class Analysis(TaskSet):

    # def on_start(self):
    #     """ on_start is called when a Locust start before any task is scheduled """
    #     self.login()

    @classmethod
    def create_request(cls, builder):

        return (builder.build_addr(), builder.build_params())

    @task(5)
    def forecast(self):
        dsl = {
                    'uri': "/WEBAPI/acs/data/analysis/forecast",
                    'required': {
                        'uid': [4, 10, 119]
                    },
                    'optional': {
                        'group_field': ['LeadSource','kh_Type','kh_Industry','kh_Rating','Type','kh_Name'],
                        'tab' : [0, 1]
                    }
              }

        uri, params = Analysis.create_request(URIBuilder(json.dumps(dsl)))

        @timer(uri=uri, params=str(params))
        def request():
            self.client.get(uri, params=params)
        request()

    @task(5)
    def performance(self):
        dsl = {
                    'uri': "/WEBAPI/acs/data/analysis/performance",
                    'required': {
                        'uid': [4, 10, 119]
                    },
                    'optional': {
                        'group_field': ['LeadSource','kh_Type','kh_Industry','kh_Rating','Type','kh_Name'],
                        'tab' : [0, 1],
                        'page' : (20, 200),
                        'num' : (20, 40)
                    }
                }

        uri, params = Analysis.create_request(URIBuilder(json.dumps(dsl)))

        @timer(uri=uri, params=str(params))
        def request():
            self.client.get(uri, params=params)
        request()

class Acs(HttpLocust):
    task_set = Analysis
    min_wait = 5000
    max_wait = 9000


if __name__ == '__main__':
    Analysis().forecast()
