# -*- coding: utf-8 -*-
# @Time    : 2019/4/19 12:18 PM
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : excep_register.py
# @Software: PyCharm

import os
import traceback

from flask import request
from loguru import logger
from werkzeug.exceptions import HTTPException

from app.api import restful_api
from common.libs.customException import CustomException
from common.libs.api_result import api_result
from common.libs.tools import print_logs


@restful_api.app_errorhandler(Exception)
def errors(e):
    logger.error('异常:{}'.format(e))
    logger.error('异常类型:{}'.format(type(e)))

    data = request.method + ' ' + request.path

    sw = True if os.environ.get('is_debug') else False

    if isinstance(e, CustomException):
        logger.error('-----CustomException-----')
        code = e.code
        message = f'CustomException:【{str(e.msg)}】' if sw else str(e.msg)

    elif isinstance(e, HTTPException) and (300 <= e.code < 600):
        logger.error('-----HTTPException-----')
        code = e.code
        message = f'HTTPException:【{str(e)}】' if sw else str(e)

    else:
        logger.error('-----Exception-----')
        code = 500
        message = f'Exception:【{str(e)}】' if sw else str(e)

    print_logs()
    traceback.print_exc()
    return api_result(code=code, message=message, data=data)
