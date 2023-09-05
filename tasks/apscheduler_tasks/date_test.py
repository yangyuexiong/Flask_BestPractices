# -*- coding: utf-8 -*-
# @Time    : 2023/9/5 14:50
# @Author  : yangyuexiong
# @Email   : yang6333yyx@126.com
# @File    : date_test.py
# @Software: PyCharm

import os, sys

sys.path.append(os.path.abspath(os.path.join(os.getcwd(), "..")))

from datetime import datetime

from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler(timezone='Asia/Shanghai')


# date 日期触发任务运行的具体日期
# 2023年9月5日 执行
# @sched.scheduled_job('date', run_date=date(2023, 9, 5), args=['text'])
@sched.scheduled_job('date', run_date=datetime(2023, 9, 5, 10, 31, 5), args=['text'])  # 2023年9月5日 10时31分5秒 执行
def date_and_datetime_task(text):
    print('date/datetime 日期 任务', '参数{}'.format(text))


if __name__ == '__main__':
    print('test date ...')
    print(datetime.now())
    sched.start()
