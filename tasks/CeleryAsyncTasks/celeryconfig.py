# -*- coding: utf-8 -*-
# @Time    : 2019-06-28 17:42
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : celeryconfig.py
# @Software: PyCharm


'''
CELERY_DEFAULT_QUEUE：默认队列                                       BROKER_URL = 'redis://root:123456@localhost:6379/7'
BROKER_URL  : 代理人的网址                                           CELERY_RESULT_BACKEND = 'redis://root:123456@localhost:6379/8'
CELERY_RESULT_BACKEND：结果存储地址                                  CELERY_TASK_SERIALIZER = 'msgpack'
CELERY_TASK_SERIALIZER：任务序列化方式                               CELERY_RESULT_SERIALIZER = 'msgpack'
CELERY_RESULT_SERIALIZER：任务执行结果序列化方式                      CELERY_RESULT_SERIALIZER = 'msgpack'
CELERY_TASK_RESULT_EXPIRES：任务过期时间                            CELERY_TASK_RESULT_EXPIRES = 60 * 60 * 24  # 任务过期时间
CELERY_ACCEPT_CONTENT：指定任务接受的内容序列化类型(序列化)，一个列表；  CELERY_ACCEPT_CONTENT = ["msgpack"]  # 指定任务接受的内容类型
'''
