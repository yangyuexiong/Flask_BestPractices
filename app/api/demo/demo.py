# -*- coding: utf-8 -*-
# @Time    : 2019-05-20 17:05
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : demo.py
# @Software: PyCharm

from flask_restful import Resource


class DemoApi(Resource):
    """
        url不传参数则使用默认参数 page=1, size=10

        """

    def get(self, page=1, size=10):
        return 'flask resful get 参数{},{}'.format(page, size)

    def post(self, page=1, size=10):
        return 'flask resful post 参数{},{}'.format(page, size)

    def put(self, page=1, size=10):
        return 'flask resful put 参数{},{}'.format(page, size)

    def delete(self, page=1, size=10):
        return 'flask resful delete 参数{},{}'.format(page, size)
