# -*- coding: utf-8 -*-
# @Time    : 2019/4/18 3:15 PM
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : ApiHook.py
# @Software: PyCharm


import time

import shortuuid
from loguru import logger
from flask import request, g

from common.libs.tools import print_logs


def api_before_request():
    g.log_uuid = "{}_{}".format(str(int(time.time())), shortuuid.uuid())
    logger.info('api_before_request')
    logger.info('request log_uuid:{}'.format(g.log_uuid))
    print_logs()

    if '/api' in request.path:
        print('访问api')
        return


def api_after_request(response):
    logger.info('api_after_request')
    logger.info('response log_uuid:{}'.format(g.log_uuid))
    logger.info('=== response ===')
    response.headers['log_uuid'] = g.log_uuid
    return response
