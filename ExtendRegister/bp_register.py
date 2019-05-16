# -*- coding: utf-8 -*-
# @Time    : 2019/4/18 10:47 AM
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : bp_register.py
# @Software: PyCharm


from app.api import route_api
from app.controllers.cms.cms_bp import route_admin
from app.controllers.other_module_01.module_01 import route_module_01
from app.controllers.other_module_02.module_02 import route_module_02
from app.controllers.other_module_03.module_03 import route_module_03


def register_bp(app):
    """蓝图注册"""

    """API蓝图注册"""
    app.register_blueprint(route_api, url_prefix="/api")

    """CMS蓝图注册"""
    app.register_blueprint(route_admin, url_prefix="/cms")

    """其他独立蓝图注册"""
    app.register_blueprint(route_module_01, url_prefix="/m1")
    app.register_blueprint(route_module_02, url_prefix="/m2")
    app.register_blueprint(route_module_03, url_prefix="/m3")
