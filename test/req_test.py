# -*- coding: utf-8 -*-
# @Time    : 2019-05-15 15:56
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : req_test.py
# @Software: PyCharm


import requests

base_url = 'http://0.0.0.0:9999/'
cms = base_url + 'cms'

resp1 = requests.get(url=cms + "/mv_params")
print(resp1.json())

resp2 = requests.post(url=cms + "/mv_json", json={"a": "123"})
print(resp2.json())

resp3 = requests.post(url=cms + "/mv_form_data", data={"a": "123"})
print(resp3.json())

resp4 = requests.post(url=cms + "/mv_bytes_data", data=b'{"a":"123"}')
print(resp4.json())

if __name__ == '__main__':
    pass
