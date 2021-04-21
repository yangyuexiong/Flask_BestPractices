# -*- coding: utf-8 -*-
# @Time    : 2019-05-17 11:29
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : tools.py
# @Software: PyCharm

import json
from datetime import datetime

from flask import request


def print_logs():
    """logs"""
    print(datetime.now())
    host = request.host
    print(host)
    method = request.method
    print(method)
    path = request.path
    print(path)
    print('=== headers ===')
    headers = {k: v for k, v in request.headers.items()}
    json_format(headers)
    print('=== params ===')
    json_format(request.args.to_dict())
    print('=== data ===')
    json_format(request.form.to_dict())
    print('=== json ===')
    json_format(request.get_json())


def check_keys(dic, *keys):
    for k in keys:
        if k not in dic.keys():
            return False
    return True


def json_format(d):
    """json格式打印"""
    try:
        print(json.dumps(d, sort_keys=True, indent=4, separators=(', ', ': '), ensure_ascii=False))
    except BaseException as e:
        print(d)
