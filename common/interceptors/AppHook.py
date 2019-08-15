# -*- coding: utf-8 -*-
# @Time    : 2019/4/18 3:15 PM
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : ApiHook.py
# @Software: PyCharm

from flask import request

from ApplicationExample import create_app

app = create_app()


@app.before_request
def before_request_api():
    print('app app app app')
    path = request.path
    print(path)
    return
