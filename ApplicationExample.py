# -*- coding: utf-8 -*-
# @Time    : 2019-05-15 15:52
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : ApplicationExample.py
# @Software: PyCharm

import os

from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate

from ExtendRegister.command_register import register_commands  # commands
from ExtendRegister.conf_register import register_config  # 配置
from ExtendRegister.excep_register import errors  # 全局异常注册
from ExtendRegister.hook_register import register_hook  # 拦截器注册
from ExtendRegister.bp_register import register_bp  # 蓝图
from ExtendRegister.db_register import register_db, db  # db
from ExtendRegister.model_register import *  # models

template_folder = os.getcwd() + '/app/templates'
static_folder = os.getcwd() + '/app/static'


def create_app():
    """应用实例"""

    app = Flask(__name__, template_folder=template_folder, static_folder=static_folder)  # 实例
    CORS(app, supports_credentials=True)  # 跨域
    register_commands(app)  # flask cli 注册
    register_config(app)  # 配置注册
    register_hook(app)  # 拦截器注册(需要在蓝图之前)
    register_bp(app)  # 蓝图注册
    register_db(app)  # db注册
    Migrate(app, db)  # ORM迁移
    return app
