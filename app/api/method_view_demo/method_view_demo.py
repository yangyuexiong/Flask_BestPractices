# -*- coding: utf-8 -*-
# @Time    : 2021/4/21 下午5:37
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : method_view_demo.py
# @Software: PyCharm

from app.all_reference import *


class MethodViewDemo(MethodView):
    """
    method view demo
    """

    def get(self, page=1, size=10):
        return api_result(code=200, message='MethodView get. 参数{},{}'.format(page, size))

    def post(self):
        return api_result(code=200, message='MethodView post')

    def put(self):
        return api_result(code=200, message='MethodView put')

    def delete(self):
        return api_result(code=200, message='MethodView delete')



