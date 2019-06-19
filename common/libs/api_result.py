# -*- coding: utf-8 -*-
# @Time    : 2019/4/19 12:00 PM
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : api_result.py
# @Software: PyCharm


from flask import jsonify, abort


# 返回格式
def api_result(code=None, message=None, data=None, details=None, status=None):
    result = {
        "code": code,
        "message": message,
        "data": data,
    }

    if not result['data']:
        result.pop('data')
        return jsonify(result)
    return jsonify(result)


