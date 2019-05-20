# -*- coding: utf-8 -*-
# @Time    : 2019-05-20 17:08
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : demo.py
# @Software: PyCharm


from flask.views import MethodView


class MethodViewTest(MethodView):
    """
    url不传参数则使用默认参数 page=1, size=10

    http://0.0.0.0:9999/cms/test4/99/88/
    """

    def get(self, page=1, size=10):
        return 'MethodView get. 参数{},{}'.format(page, size)

    def post(self, page=1, size=10):
        return 'MethodView post. 参数{},{}'.format(page, size)

    def put(self, page=1, size=10):
        return 'MethodView put. 参数{},{}'.format(page, size)

    def delete(self, page=1, size=10):
        return 'MethodView delete. 参数{},{}'.format(page, size)
