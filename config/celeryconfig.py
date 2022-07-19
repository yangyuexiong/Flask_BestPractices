# -*- coding: utf-8 -*-
# @Time    : 2022/7/19 10:51
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : celeryconfig.py
# @Software: PyCharm

broker_url = 'redis://:123456@127.0.0.1:6379/2'

result_backend = 'redis://:123456@127.0.0.1:6379/3'

# 时区
timezone = 'Asia/Shanghai'

# 是否使用UTC
enable_utc = False

# include_list = [
#     'tasks.celery_tasks.task01',
#     'tasks.celery_tasks.task02'
# ]

imports = (
    'tasks.celery_tasks.task01',
    'tasks.celery_tasks.task02',
    'tasks.celery_tasks.task03'
)
