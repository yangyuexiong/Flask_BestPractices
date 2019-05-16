# -*- coding: utf-8 -*-
# @Time    : 2019/4/18 2:31 PM
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : cms_module_03.py
# @Software: PyCharm

from flask import Blueprint, render_template

route_module_03 = Blueprint('cms_module_03', __name__)


@route_module_03.route('/', methods=["GET", "POST"])
def module_03():
    return '其他业务模块003'


@route_module_03.route('/index', methods=["GET", "POST"])
def module_03_index():
    return render_template('index03.html')
