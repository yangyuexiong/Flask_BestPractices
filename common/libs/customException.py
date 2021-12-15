# -*- coding: utf-8 -*-
# @Time    : 2019/4/19 2:46 PM
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : customException.py
# @Software: PyCharm


from werkzeug.exceptions import HTTPException

from flask import jsonify, abort, request
import flask_restful

custom_resp_dict = {
    333: '测试自定义异常',
    400: '参数类型错误',
    401: '未登录_认证信息失败_令牌过期',
    403: '无权限',
    500: '服务器异常',
    666: 'Token?',
    996: '没救了'
}


class CustomException(HTTPException):
    code = None
    msg = None

    def __init__(self, code=None, msg=None):
        if code:
            self.code = code

        if msg:
            self.msg = msg
        super(CustomException, self).__init__(self.code, self.msg)


def method_view_ab_code(code):
    """MethodView 自定义异常"""
    msg = custom_resp_dict.get(code, 'ERROR')
    raise CustomException(code=code, msg=msg)


def flask_restful_ab_code(code):
    """Flask Restful 自定义异常"""

    message = custom_resp_dict.get(code)

    if message:
        req = request.method + ' ' + request.path
        result = {
            "code": code,
            "message": message,
            "request": req
        }
        result = jsonify(result)

    else:
        result = code

    # 修改、简化 flask_restful.abort
    flask_restful.abort = abort(result)
    flask_restful.abort(code)
