# encoding:utf-8
__author__ = 'xyc'

import time,logging
import functools


logger = logging.getLogger(__name__)


def timer(uri='no uri', params="no params"):
  def _time_me(fn):
    @functools.wraps(fn)
    def _wrapper(*args, **kwargs):
      start = time.time()
      fn(*args, **kwargs)
      logger.info("%s %s with %s cost %s second" % (fn.__name__, uri, params, time.time() - start))
    return _wrapper
  return _time_me


def fn_timer(function):
  @functools.wraps(function)
  def function_timer(*args, **kwargs):
    t0 = time.time()
    result = function(*args, **kwargs)
    t1 = time.time()
    print ("Total time running %s: %s seconds" % (function.func_name, str(t1-t0)))
    return result
  return function_timer