# -*- coding: utf-8 -*-
# @Time    : 2019-07-01 16:46
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : main.py
# @Software: PyCharm

from time import sleep

from celery import Celery

BROKER_URL = 'redis://root:123456@localhost:6379/7'
CELERY_RESULT_BACKEND = 'redis://root:123456@localhost:6379/8'

app = Celery('main', broker=BROKER_URL, backend=CELERY_RESULT_BACKEND)


@app.task(name='test')
def add(x, y):
    print('......')
    return x + y


@app.task(name='send_mail')
def send_mail(mail):
    print('发送邮件到:{}'.format(mail))
    # 模拟耗时
    # sleep(3)
    return '发送成功'


if __name__ == '__main__':
    pass
    # 相关资料参考网址
    'https://blog.51cto.com/steed/2292346?source=dral'
    'https://www.cnblogs.com/276815076/p/9954049.html'

    """
    执行:
        前台执行:
            celery -A main worker --loglevel=info
            
        后台执行:
            celery multi start w1 -A  main -l info
        
        停止:
        异步关闭 立即返回
            celery multi stop w1 -A  main -l info
        
        等待关闭操作完成
            celery multi stopwait w1 -A  main -l info
    """
