# -*- coding: utf-8 -*-
# @Time    : 2022/7/19 11:34
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : demo_api.py
# @Software: PyCharm

from flask import request

from all_reference import *


class MethodViewParams(MethodView):
    """
    method view 获取get请求传参
    """

    def get(self):
        """获取get请求传参"""

        # 方法一:每个获取
        a = request.args.get('a')
        b = request.args.get('b')
        print(a, b)

        # 方法二:一次性或者再取值
        data = request.args.to_dict()
        print(data)
        return api_result(code=200, message='MethodView获取get请求传参', data=data)


class MethodViewFormData(MethodView):
    """
    method view 获取form-data传参
    """

    def post(self):
        """获取form-data传参"""

        # 方法一:每个获取
        a = request.form.get('a')
        b = request.form.get('b')
        print(a, b)

        # 方法二:一次性或者再取值
        data = request.form.to_dict()
        print(data)
        a = data.get('a')
        b = data.get('b')
        print(a, b)
        return api_result(code=200, message='MethodView获取form-data传参', data=data)


class MethodViewJson(MethodView):
    """
    method view 获取JSON传参
    """

    def post(self):
        """获取JSON传参"""

        data = request.get_json()
        d1 = data.get('d1')
        d2 = data.get('d2')
        d3 = data.get('d3')
        print(d1)
        print(d2)
        print(d3)
        return api_result(code=200, message='MethodView获取JSON传参', data=data)


class MethodViewBytesData(MethodView):
    """
    method view 获取二进制data传参
    """

    def post(self):
        """获取二进制data传参"""

        data = request.get_data()
        return api_result(code=200, message='MethodView获取二进制data传参', data=data)
