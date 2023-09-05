# -*- coding: utf-8 -*-
# @Time    : 2023/9/5 14:42
# @Author  : yangyuexiong
# @Email   : yang6333yyx@126.com
# @File    : cron_test.py
# @Software: PyCharm

import os, sys

sys.path.append(os.path.abspath(os.path.join(os.getcwd(), "..")))

from datetime import datetime

from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler(timezone='Asia/Shanghai')


# cron 周期触发任务运行的周期(某时间段～某时间段 执行此任务)
# 表示从 2023-1-1～2023-12-31 的 周一到周五 的 早上6点01分01秒执行
@sched.scheduled_job('cron', start_date='2023-1-1', end_date='2023-12-31', day_of_week='mon-fri', hour=6, minute=1, second=1)
def cron_task():
    print(f'开始执行:{datetime.now()}')
    print('执行任务...')
    print(f'执行完毕:{datetime.now()}\n')


if __name__ == '__main__':
    print('test cron ...')
    print(datetime.now())
    sched.start()
