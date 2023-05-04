# -*- coding: utf-8 -*-
# @Time    : 2022/7/19 11:15
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : test_api.py
# @Software: PyCharm


from all_reference import *
from tasks.celery_tasks.task03 import test_orm


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

        results = test_orm.delay()
        print(results)
        return api_result(code=200, message='操作成功,请前往日志查看执行结果', data=[str(results)])
