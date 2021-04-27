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


def ab_code(data):
    """
    MethodView 自定义异常
    """
    C = custom_resp_dict
    code = data
    msg = C.get(data, 'ERROR')
    raise CustomException(code=code, msg=msg)


def ab_code_restful(data):
    """
    flask_restful 自定义异常
    """
    C = custom_resp_dict
    if C.get(data):
        code = data
        msg = C.get(data)
        req = request.method + ' ' + request.path
        r = {
            "code": code,
            "msg": msg,
            "request": req
        }
        return jsonify(r)
    else:
        return data


# 修改 flask_restful.abort
def custom_abord(http_status_code, *args, **kwargs):
    return abort(ab_code_restful(http_status_code))


# 简化 flask_restful.abort
def ab_code_2(code):
    """
    flask_restful 自定义异常
    """
    flask_restful.abort = custom_abord
    flask_restful.abort(code)
