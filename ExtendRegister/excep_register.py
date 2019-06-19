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
import datetime
from app.api import route_api
from common.libs.customException import CustomException
from config.config import config_obj
import os


def tb(excep):
    logs_path = os.getcwd() + '/logs/tb.log'
    # print(logs_path)
    print(os.environ.get('FLASK_ENV'))
    if not os.environ.get('FLASK_ENV'):
        traceback.print_exc()
        print('1')
    """
    开发环境:
    直接在控制台显示
    并且写入日记文件
    """
    if config_obj[os.environ.get('FLASK_ENV')].DEBUG:
        with open(logs_path, 'a+') as f:
            f.write('\n' + '--->>>' + str(datetime.datetime.now()) + '\n' + excep + '\n')
        traceback.print_exc(file=open(logs_path, 'a+'))
        traceback.print_exc()
    else:
        """
        生产环境:
        只写入日志文件
        """
        with open(logs_path, 'a+') as f:
            f.write('\n' + '--->>>' + str(datetime.datetime.now()) + '\n' + excep + '\n')
        traceback.print_exc(file=open(logs_path, 'a+'))


@route_api.app_errorhandler(Exception)
def errors(e):
    print('异常:', e)
    print('异常类型:', type(e))

    if isinstance(e, CustomException):
        print('-----CustomException-----')
        tb('-----CustomException-----')
        return api_result(code=e.code, message=e.msg, data=request.method + ' ' + request.path)

    if isinstance(e, HTTPException) and (300 <= e.code < 600):
        print('-----HTTPException-----')
        tb('-----HTTPException-----')
        return api_result(code=e.code, message='HTTPException:【{}】'.format(str(e)),
                          data=request.method + ' ' + request.path)

    else:
        print('-----Exception-----')
        tb('-----Exception-----')
        return api_result(code=500, message='Exception:【{}】'.format(str(e)), data=request.method + ' ' + request.path)
