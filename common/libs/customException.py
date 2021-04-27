# -*- coding: utf-8 -*-
# @Time    : 2019/4/19 2:46 PM
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : customException.py
# @Software: PyCharm


from werkzeug.exceptions import HTTPException

from flask import jsonify, abort, request
import flask_restful

# Common CustomException
EX_TEST = (333, '测试自定义异常')
Bad_Request = (400, '参数类型错误')
NOT_AUTHORIZED = (401, '未登录-认证信息失败-令牌过期')
FORBIDDEN = (403, '无权限')
ServerError = (500, '服务器内部异常')
NOT_TOKEN = (666, '没token玩个毛')
ICU = (996, '没救了')

# Api CustomException
already_regist = (999, '手机号已注册')
tel_length_err = (1000, '手机号应为11位')
not_tel = (1001, '手机号未注册')
psw_length_err = (1002, '密码少于6位')
psw_err = (1003, '密码错误')
psw2_err = (1004, '2次密码不一致')

# CMS CustomException
LOGIN_ERROR = (2001, '登录失败-服务器非常正常-请重试!')

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
    code = data[0]
    msg = data[1]
    req = request.method + ' ' + request.path
    r = {
        "code": code,
        "msg": msg,
        "request": req
    }
    return jsonify(r)


# 修改flask_restful.abort
def custom_abord(http_status_code, *args, **kwargs):
    if http_status_code == 400:
        abort(ab_code_restful(ICU))
    if http_status_code == 333:
        abort(ab_code_restful(EX_TEST))
    return abort(http_status_code)


# 简化 flask_restful.abort
def ab_code_2(code):
    """
    flask_restful 自定义异常
    """
    flask_restful.abort = custom_abord
    flask_restful.abort(code)
