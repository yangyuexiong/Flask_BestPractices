# -*- coding: utf-8 -*-
# @Time    : 2019/4/18 3:15 PM
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : ApiHook.py
# @Software: PyCharm

from flask import request

from app.api import route_api


@route_api.before_request
def before_request_api():
    print('api before_request')
    path = request.path
    print(path)
    if request.method == 'OPTIONS':
        return
    if '/api' in path:
        print('访问api')
        return
