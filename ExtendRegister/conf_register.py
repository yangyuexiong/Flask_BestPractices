# -*- coding: utf-8 -*-
# @Time    : 2019/4/19 11:45 AM
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : conf_register.py
# @Software: PyCharm

from config.config import config_obj


def register_config(app):
    """配置文件"""

    app.config.from_object(config_obj['new'])  # 环境配置
    config_obj['new'].init_app(app)
