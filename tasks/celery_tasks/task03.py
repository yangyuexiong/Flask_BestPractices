# -*- coding: utf-8 -*-
# @Time    : 2022/7/19 10:56
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : task01.py
# @Software: PyCharm

from celery_app import cel
from app.models.admin.models import Admin


@cel.task
def test_orm():
    admin = Admin.query.get(1)
    print(admin.to_json())
    return admin.to_json()
