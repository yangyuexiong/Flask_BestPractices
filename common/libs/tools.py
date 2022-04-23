# -*- coding: utf-8 -*-
# @Time    : 2019-05-17 11:29
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : tools.py
# @Software: PyCharm

import json

from flask import request
from loguru import logger


def print_logs():
    """logs"""
    host = request.host
    ip_address = request.headers.get('X-Forwarded-For')
    method = request.method
    path = request.path
    headers = {k: v for k, v in request.headers.items()}
    params = request.args.to_dict()
    form_data = request.form.to_dict()
    logger.info(f"host:{host}")
    logger.info(f"ip_address:{ip_address}")
    logger.info(f"method:{method}")
    logger.info(f"path:{path}")
    logger.info('=== headers ===')
    json_format(headers)
    logger.info('=== params ===')
    json_format(params)
    logger.info('=== data ===')
    json_format(form_data)
    logger.info('=== json ===')
    try:
        json_format(request.get_json())
    except BaseException as e:
        print({})
    logger.info('=== end print_logs ===')


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
