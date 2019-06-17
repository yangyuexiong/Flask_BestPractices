# -*- coding: utf-8 -*-
# @Time    : 2019/4/18 3:15 PM
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : ApiHook.py
# @Software: PyCharm

from flask import request, g, jsonify, abort

from app.controllers.cms.cms_bp import route_admin


@route_admin.before_request
def before_request_cms():
    print('cms before_request')
    path = request.path
    print(path)
    if request.method == 'OPTIONS':
        return
    if '/cms' in path:
        print('访问cms')
        return
