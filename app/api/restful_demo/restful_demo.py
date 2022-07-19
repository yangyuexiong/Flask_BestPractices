# -*- coding: utf-8 -*-
# @Time    : 2021/4/21 下午4:43
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : restful_demo.py
# @Software: PyCharm

from all_reference import *


class RestfulDemoApi(Resource):
    """
    flask restful demo
    """

    def get(self):
        data = {
            'time': time(),
            'datetime': datetime.now(),
            '当前进程id': os.getpid(),
            '父进程id': os.getppid(),
            '线程id': threading.get_ident(),
            'db id': id(db)
        }
        return api_result(code=200, message='flask restful demo', data=data)

    def post(self):
        return api_result(code=200, message='flask restful demo', data=[])


class DemoApi(Resource):
    """
    参数使用:
        url不传参数则使用默认参数 page=1, size=10
    """

    def get(self, page=1, size=10):
        return f'flask restful get 参数{page},{size}'

    def post(self):
        return api_result(code=200, message='flask restful post')

    def put(self):
        return api_result(code=200, message='flask restful put')

    def delete(self):
        return api_result(code=200, message='flask restful delete')
