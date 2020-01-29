# -*- coding: utf-8 -*-
# @Time    : 2019/4/18 11:03 AM
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : __init__.py.py
# @Software: PyCharm

from flask import Blueprint
from flask_restful import Api

from .demo.demo import Index, DemoApi, HttpExceptionTest, CustomExceptionTest, BaseExceptionTest

route_api = Blueprint('api', __name__)
api = Api(route_api)

"""
Resource_demo
"""

api.add_resource(Index, '/', endpoint='index')

# 带参数url 可以写在一起
# 无参数：http://0.0.0.0:9999/api/demo/
# 带参数：http://0.0.0.0:9999/api/demo/1010/2222/
api.add_resource(DemoApi, '/demo/', '/demo/<page>/<size>/', endpoint='demo')

# 测试异常
api.add_resource(HttpExceptionTest, '/h/', endpoint='HttpExceptionTest')
api.add_resource(CustomExceptionTest, '/c/', endpoint='CustomExceptionTest')
api.add_resource(BaseExceptionTest, '/b/', endpoint='BaseExceptionTest')

api.init_app(route_api)
