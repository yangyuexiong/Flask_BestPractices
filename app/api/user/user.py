# -*- coding: utf-8 -*-
# @Time    : 2019/4/18 2:59 PM
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : user.py
# @Software: PyCharm

from flask_restful import Resource, marshal_with, fields
from flask import request, g, abort
from common.libs.customException import ab_code


class TestApi(Resource):
    def get(self):
        '''全局异常测试'''

        '''HTTPException'''
        # abort(404)

        '''Exception'''
        # 1 / 0

        '''CustomException'''
        # ab_code(666)
        return 'this api'


# demo可删除
class UserRegister(Resource):
    user_fields = {
        'user_id': fields.String(attribute='id'),
        'tel': fields.String,
        'nickname': fields.String,
        'level': fields.String,
        'money': fields.String(default='9999999999999999'),
    }

    @marshal_with(user_fields, envelope='data')
    def get(self):
        return '1'

    def post(self):
        return

    def delete(self):
        return
