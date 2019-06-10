# -*- coding: utf-8 -*-
# @Time    : 2019/4/18 1:52 PM
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : cms_bp.py
# @Software: PyCharm

from flask import Blueprint, abort, jsonify
from .cms_module_01.m1 import rule_test01
from .cms_module_02.m2 import rule_test02
from .cms_module_03.m3 import rule_test03
from .demo.demo import MethodViewTest

route_admin = Blueprint('cms', __name__)


def error_test(n):
    '''全局异常测试'''

    '''HTTPException'''
    if n == 1:
        abort(404)

    '''Exception'''
    if n == 2:
        1 / 0

    '''CustomException'''
    if n == 3:
        from common.libs.customException import ab_code
        ab_code(666)


@route_admin.route('/', methods=["GET", "POST"])
def index():
    error_test(1)
    return jsonify('this cms')


"""
route_demo 与 如下 完全一样 该写法为了统一管理url

@route_admin.route('/', methods=["GET", "POST"])
def index():
    return 'hello flask'
    
"""
route_admin.add_url_rule('/test', methods=["GET", "POST"], endpoint='rule_test01', view_func=rule_test01)
route_admin.add_url_rule('/test2', methods=["GET", "POST"], endpoint='rule_test02', view_func=rule_test02)
route_admin.add_url_rule('/test3', methods=["GET", "POST"], endpoint='rule_test03', view_func=rule_test03)

"""
使用类视图:MethodView_demo
"""
# 带参数url需要分开注册否则报错（flask_resful则不用 参照文件:Flask_BestPractices/app/api/__init__.py）
# 无参数: http://0.0.0.0:9999/cms/demo/
# 带参数: http://0.0.0.0:9999/cms/demo/999/888/
route_admin.add_url_rule('/demo/', view_func=MethodViewTest.as_view('demo'))
route_admin.add_url_rule('/demo/<page>/<size>/', view_func=MethodViewTest.as_view('demo_pram'))
