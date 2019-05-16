# -*- coding: utf-8 -*-
# @Time    : 2019/4/18 11:03 AM
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : __init__.py.py
# @Software: PyCharm

from flask import Blueprint
from flask_restful import Api, Resource
from .user.user import TestApi, UserRegister

route_api = Blueprint('api', __name__)
api = Api(route_api)

api.add_resource(TestApi, '/', endpoint='test')
api.add_resource(UserRegister, '/register', '/register/<user_id>', endpoint='register')

api.init_app(route_api)