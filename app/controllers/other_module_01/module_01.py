# -*- coding: utf-8 -*-
# @Time    : 2019/4/18 2:31 PM
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : cms_module_01.py
# @Software: PyCharm

from flask import Blueprint, render_template

route_module_01 = Blueprint('cms_module_01', __name__)


@route_module_01.route('/', methods=["GET", "POST"])
def module_01():
    return '其他业务模块001'


@route_module_01.route('/index', methods=["GET", "POST"])
def module_01_index():
    return render_template('index01.html')
