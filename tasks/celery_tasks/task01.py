# -*- coding: utf-8 -*-
# @Time    : 2022/7/19 10:56
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : task01.py
# @Software: PyCharm

import time
from celery_app import cel


@cel.task
def send_email(res):
    time.sleep(5)
    return "完成向%s发送邮件任务" % res
