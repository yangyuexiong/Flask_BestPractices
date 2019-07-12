# -*- coding: utf-8 -*-
# @Time    : 2019-06-25 17:06
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : excep_test.py
# @Software: PyCharm


import requests
from test.test_data import *


def func():
    print('-' * 20, 'cms', '-' * 20)
    print('测试cms:CustomException')
    req = requests.get(cms + 'test_custom_exception')
    print(req.json())
    assert req.json()['code'] == 666

    print('测试cms:HTTPException:手动抛出')
    req = requests.get(cms + 'test_http_exception')
    print(req.json())
    assert req.json()['code'] == 404

    print('测试cms:HTTPException:非手动抛出')
    req = requests.get(cms + 'test_http_exception_xxxxxxxxx')
    print(req.json())
    assert req.json()['code'] == 404

    print('测试cms:Exception')
    req = requests.get(cms + 'test_exception')
    print(req.json())
    assert req.json()['code'] == 500
    print('-' * 20, 'end-cms', '-' * 20)

    print('=' * 200)

    print('-' * 20, 'api', '-' * 20)
    print('测试api:CustomException')
    req = requests.get(api + 'c/')
    print(req.json())
    assert req.json()['code'] == 333

    print('测试api:HTTPException:手动抛出')
    req = requests.get(api + 'h/')
    print(req.json())
    assert req.json()['code'] == 404

    print('测试api:Exception')
    req = requests.get(api + 'b/')
    print(req.json())
    assert req.json()['code'] == 500
    print('-' * 20, 'end-api', '-' * 20)


if __name__ == '__main__':
    pass
    func()
