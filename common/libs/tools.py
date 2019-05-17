# -*- coding: utf-8 -*-
# @Time    : 2019-05-17 11:29
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : tools.py
# @Software: PyCharm


def check_keys(dic, *keys):
    for k in keys:
        if k not in dic.keys():
            return False
    return True
