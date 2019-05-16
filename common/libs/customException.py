# -*- coding: utf-8 -*-
# @Time    : 2019/4/19 2:46 PM
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : customException.py
# @Software: PyCharm


from flask import request, json
from werkzeug.exceptions import HTTPException

Bad_Request = (400, '参数类型错误')
NOT_AUTHORIZED = (401, '未登录-认证信息失败-令牌过期')
FORBIDDEN = (403, '无权限')
ServerError = (500, '服务器内部异常')
not_token = (666, '没token玩个毛')
already_regist = (999, '手机号已注册')
tel_length_err = (1000, '手机号应为11位')
not_tel = (1001, '手机号未注册')
psw_length_err = (1002, '密码少于6位')
psw_err = (1003, '密码错误')
psw2_err = (1004, '2次密码不一致')
database_err = (1066, '数据库异常')


class CustomException(HTTPException):
    code = 500
    error_code = 999
    msg = '服务器在路上'

    def __init__(self, msg=None, code=None, error_code=None,
                 headers=None):
        if code:
            self.code = code
        if error_code:
            self.error_code = error_code
        if msg:
            self.msg = msg
        super(CustomException, self).__init__(self.msg, None)

    def get_body(self, environ=None):
        body = dict(
            msg=self.msg,
            error_code=self.error_code,
            request=request.method + ' ' + self.get_url_no_param()
        )
        text = json.dumps(body)
        return text

    def get_headers(self, environ=None):
        return [('Content-Type', 'application/json')]


class AbortCode(CustomException):
    code = 999
    msg = '未设置自定义的异常消息'
    error_code = 1006


def ab_code(data):
    C = {
        400: Bad_Request,
        401: NOT_AUTHORIZED,
        403: FORBIDDEN,
        500: ServerError,
        666: not_token
    }
    code = C.get(data)[0]
    msg = C.get(data)[1]
    raise AbortCode(code=code, msg=msg)
