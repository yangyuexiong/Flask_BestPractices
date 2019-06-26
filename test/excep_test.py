# -*- coding: utf-8 -*-
# @Time    : 2019-06-25 17:06
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : excep_test.py
# @Software: PyCharm


import requests
from test.test_data import *


def func():
    print('测试:CustomException')
    req = requests.get(cms + 'test_custom_exception')
    print(req.json())
    assert req.json()['code'] == 666

    print('测试:HTTPException:手动抛出')
    req = requests.get(cms + 'test_http_exception')
    print(req.json())
    assert req.json()['code'] == 404

    print('测试:HTTPException:非手动抛出')
    req = requests.get(cms + 'test_http_exception_xxxxxxxxx')
    print(req.json())
    assert req.json()['code'] == 404

    print('测试:Exception')
    req = requests.get(cms + 'test_exception')
    print(req.json())
    assert req.json()['code'] == 500


if __name__ == '__main__':
    pass
    func()
