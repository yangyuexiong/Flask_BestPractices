# -*- coding: utf-8 -*-
# @Time    : 2019/4/19 11:45 AM
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : conf_register.py
# @Software: PyCharm


def register_config(app):
    """配置文件"""

    """
    暂时兼容旧注册配置文件,后续废除。
    """
    # 旧注册配置文件
    from config.config import config_obj, app_conf
    app.config.from_object(config_obj[app_conf()])  # 环境配置
    config_obj[app_conf()].init_app(app)

    # 新注册配置文件
    # config_obj['new'].init_app(app)
