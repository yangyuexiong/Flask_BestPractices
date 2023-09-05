# -*- coding: utf-8 -*-
# @Time    : 2023/9/5 14:42
# @Author  : yangyuexiong
# @Email   : yang6333yyx@126.com
# @File    : interval_test.py
# @Software: PyCharm

import os, sys

sys.path.append(os.path.abspath(os.path.join(os.getcwd(), "..")))

from datetime import datetime

from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler(timezone='Asia/Shanghai')


# interval 间隔触发任务运行的时间间隔 (从2023-1-1 00:00:00～2033-1-1 00:00:00生效:不设置则不限制)
# minutes 分钟
# seconds 秒
@sched.scheduled_job('interval', start_date='2023-1-1', end_date='2033-1-1', seconds=3)
def interval_task():
    print(f'开始执行:{datetime.now()}')
    print('每3秒执行一次任务...')
    print(f'执行完毕:{datetime.now()}\n')


if __name__ == '__main__':
    print('test interval ...')
    print(datetime.now())
    sched.start()
