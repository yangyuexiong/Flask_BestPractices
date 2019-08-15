import os

from flask import Flask as _Flask
from flask.json import JSONEncoder as _JSONEncoder
from flask_cors import CORS

from ExtendRegister.bp_register import register_bp  # 蓝图
from ExtendRegister.conf_register import register_config  # 配置
from ExtendRegister.db_register import db  # db

"""
os.getcwd():
    /Users/yangyuexiong/Desktop/Flask_BestPractices
"""


class JSONEncoder(_JSONEncoder):
    """重写flask序列化"""

    def default(self, o):
        if hasattr(o, 'keys') and hasattr(o, '__getitem__'):
            return dict(o)
        from datetime import date
        if isinstance(o, date):
            return o.strftime('%Y-%m-%d %H:%M:%S')
        else:
            return 'error'


class Flask(_Flask):
    """重写注册"""

    json_encoder = JSONEncoder


def create_app():
    app = Flask(
        __name__,
        template_folder=os.getcwd() + '/app/templates',
        static_folder=os.getcwd() + '/app/static',
    )  # 实例
    CORS(app, supports_credentials=True)  # 跨域
    register_config(app)
    register_bp(app)
    db.init_app(app)
    return app
