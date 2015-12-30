# encoding:utf-8
__author__ = 'xyc'

import json, logging
from builder import URIBuilder

logger = logging.getLogger(__name__)


def create_request(cls, **kwargs):

        return URIBuilder(json.dumps(kwargs)).build_params()

def print_result(cls, request, *args, **kwargs):
        logger.info("url:%s code:%d result:%s" % (request.url,request.status_code, request.text))