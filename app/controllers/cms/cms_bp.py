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


route_admin.add_url_rule('/test', methods=["GET", "POST"], endpoint='rule_test01', view_func=rule_test01)
route_admin.add_url_rule('/test2', methods=["GET", "POST"], endpoint='rule_test02', view_func=rule_test02)
route_admin.add_url_rule('/test3', methods=["GET", "POST"], endpoint='rule_test03', view_func=rule_test03)
