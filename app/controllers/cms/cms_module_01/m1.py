# -*- coding: utf-8 -*-
# @Time    : 2019/4/19 10:31 AM
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : m1.py
# @Software: PyCharm

from flask import request
from common.libs.api_result import api_result


def rule_test01():
    if request.method == 'GET':
        print('get')
    if request.method == 'POST':
        print('post')
    # return 'cms_module_01'
    return api_result(code=200, message='rule_test01', data=[])



