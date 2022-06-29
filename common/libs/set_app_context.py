# -*- coding: utf-8 -*-
# @Time    : 2022/5/23 16:15
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : set_app_context.py
# @Software: PyCharm

from functools import wraps


def set_app_context(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except BaseException as e:
            print('=== 测试:{} ==='.format(func.__name__))
            from ApplicationExample import create_app
            app = create_app()
            with app.app_context():
                return func(*args, **kwargs)

    return wrapper
