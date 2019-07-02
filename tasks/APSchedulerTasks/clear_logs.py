# -*- coding: utf-8 -*-
# @Time    : 2019-06-28 09:33
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : clear_logs.py
# @Software: PyCharm


"https://my.oschina.net/sharesuiyue/blog/1601614"

import time
import os
from datetime import date, datetime
from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

'''
# 添加任务方法一
def my_job01():
    print('任务一', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))


sched.add_job(my_job01, 'interval', seconds=5)


# 添加任务方法二
@sched.scheduled_job('interval', seconds=5)
def my_job02():
    print('任务二', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))


'''
logs_path = os.getcwd() + '/test.log'
# print(logs_path)
with open(logs_path, 'w+') as f:
    f.write('--->>>测试清理日记先写入一些东西' + str(datetime.now()))


# interval 间隔：触发任务运行的时间间隔
# 表示每隔1天0时0分0秒执行一次任务 (从2019-07-01 00:00:00～2019-08-01 00:00:00生效:不设置则不限制)
@sched.scheduled_job('interval', days=1, hours=0, minutes=0, seconds=0, start_date='2019-06-01 00:00:00',
                     end_date='2019-08-01 00:00:00', id='okc')
def interval_task():
    '''
    清空日志例子
    :return:
    '''
    with open(logs_path, 'r+') as f:
        f.truncate()
    print('interval 间隔 任务', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

    sched.remove_job('id_1')


# cron 周期：触发任务运行的周期(某时间段～某时间段 执行此任务)
# 表示从 2019-7-1～2019-12-31 的 周一到周五 的 早上6点01分01秒执行
@sched.scheduled_job('cron', start_date='2019-7-1',
                     end_date='2019-12-31', day_of_week='mon-fri', hour=6, minute=1, second=1)
def cron_task():
    '''
    清空日志例子
    :return:
    '''
    print('cron 周期 任务', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    with open(logs_path, 'r+') as f:
        f.truncate()


# date 日期：触发任务运行的具体日期
# 在2019年6月28日 执行
# @sched.scheduled_job('date', run_date=date(2019, 6, 28), args=['text'])
@sched.scheduled_job('date', run_date=datetime(2019, 6, 28, 10, 31, 0), args=['text'])  # 在2019年6月28日 10时31分0秒 执行
def date_and_datetime_task(text):
    print('date/datetime 日期 任务', '参数{}'.format(text))


if __name__ == '__main__':
    sched.start()
