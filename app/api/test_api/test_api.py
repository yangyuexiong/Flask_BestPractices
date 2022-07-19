# -*- coding: utf-8 -*-
# @Time    : 2022/7/19 11:15
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : test_api.py
# @Software: PyCharm


from all_reference import *


class TestMethodView(MethodView):
    """
    测试 view demo
    """

    def get(self):
        """测试内部异常"""
        print(1 / 0)  #
        return

    def post(self):
        """测试自定义异常"""
        return ab_code(666)


class TestRestful(Resource):
    """
    测试 restful demo
    """

    def get(self):
        """测试内部异常"""
        print(1 / 0)
        return

    def post(self):
        """测试自定义异常"""
        return ab_code_2(666)


class TestCeleryTask(MethodView):
    """
    测试异步任务
    """

    def get(self):
        """测试异步任务"""
        from tasks.celery_tasks.task03 import test_orm
        test_orm.delay()
        return 'ok'
