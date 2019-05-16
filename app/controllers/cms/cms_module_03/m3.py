# -*- coding: utf-8 -*-
# @Time    : 2019/4/19 10:31 AM
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : m1.py
# @Software: PyCharm

from flask import request


def rule_test03():
    if request.method == 'GET':
        print('get')
    if request.method == 'POST':
        print('post')
    return 'cms_module_03'
