# -*- coding: utf-8 -*-
# @Time    : 2019-05-15 15:56
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : req_test.py
# @Software: PyCharm


import requests

base_url = 'http://0.0.0.0:9999/'
api = base_url + 'api/'
cms = base_url + 'cms/'

r = requests.get(api)
print(r.json())

r1 = requests.get(cms)
print(r1.json())

r2 = requests.get(cms + 'test')
print(r2.url)
print(r2.json())

if __name__ == '__main__':
    pass



