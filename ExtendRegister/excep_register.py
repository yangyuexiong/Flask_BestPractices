# -*- coding: utf-8 -*-
# @Time    : 2019/4/19 12:18 PM
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : excep_register.py
# @Software: PyCharm

from flask import request
from werkzeug.exceptions import HTTPException
from common.libs.api_result import api_result
import traceback

from app.api import route_api
from common.libs.customException import CustomException


@route_api.app_errorhandler(Exception)
def errors(e):
    print(e)
    print(type(e))

    if isinstance(e, CustomException):
        print('-----CustomException-----')
        return api_result(code=e.code, message=e.msg, data=request.method + ' ' + request.path)

    if isinstance(e, HTTPException) and (300 <= e.code < 600):
        print('-----HTTPException-----')
        traceback.print_exc()
        return api_result(code=e.code, message='HTTPException:【{}】'.format(str(e)),
                          data=request.method + ' ' + request.path)

    else:
        print('-----Exception-----')
        traceback.print_exc()
        return api_result(code=500, message='Exception:【{}】'.format(str(e)), data=request.method + ' ' + request.path)
