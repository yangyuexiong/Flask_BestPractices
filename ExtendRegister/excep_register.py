# -*- coding: utf-8 -*-
# @Time    : 2019/4/19 12:18 PM
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : excep_register.py
# @Software: PyCharm

import os
import json
import datetime
import platform
import traceback

from flask import request
from werkzeug.exceptions import HTTPException

from app.api import route_api
from common.libs.customException import CustomException
from common.libs.api_result import api_result
from config.config import config_obj


def json_format(d):
    """json格式打印"""
    try:
        print(json.dumps(d, sort_keys=True, indent=4, separators=(', ', ': '), ensure_ascii=False))
    except BaseException as e:
        print(d)


def print_req_logs():
    """请求日志输出"""
    print('=== url ===')
    print(request.url)
    print('=== headers ===')
    headers_list = [{i[0]: i[1]} for i in request.headers.items()]
    headers_dict = {}
    for h in headers_list:
        headers_dict.update(h)
    json_format(headers_dict)
    print('=== method ===')
    print(request.method)
    print('=== form data ===')
    json_format(request.args.to_dict())
    print('=== form data ===')
    json_format(request.form.to_dict())
    print('=== json data ===')
    json_format(request.get_json())


def tb(excep):
    if platform.system() == 'Windows':
        logs_path = os.getcwd() + '\\logs\\tb.log'
    else:
        logs_path = os.getcwd() + '/logs/tb.log'
    # print(logs_path)
    print(os.environ.get('FLASK_ENV'))
    if not os.environ.get('FLASK_ENV'):
        traceback.print_exc()
    """
    开发环境:
    直接在控制台显示
    并且写入日记文件
    """
    print_req_logs()
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
        return api_result(code=e.code, message='CustomException:【{}】'.format(str(e.msg)),
                          data=request.method + ' ' + request.path)

    if isinstance(e, HTTPException) and (300 <= e.code < 600):
        print('-----HTTPException-----')
        tb('-----HTTPException-----')
        return api_result(code=e.code, message='HTTPException:【{}】'.format(str(e)),
                          data=request.method + ' ' + request.path)

    else:
        print('-----Exception-----')
        tb('-----Exception-----')
        return api_result(code=500, message='Exception:【{}】'.format(str(e)), data=request.method + ' ' + request.path)


if __name__ == '__main__':
    logs_path = os.getcwd() + '/logs/tb.log'
    print(logs_path)
