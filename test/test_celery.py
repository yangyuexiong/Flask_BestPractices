# -*- coding: utf-8 -*-
# @Time    : 2019-06-28 15:02
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : test_celery.py
# @Software: PyCharm

from time import sleep

from tasks.CeleryAsyncTasks.main import add, send_mail

r = add.delay(10, 20)

"""
state: 返回任务状态；
task_id: 返回任务id；
result: 返回任务结果，同get()方法；
ready(): 判断任务是否以及有结果，有结果为True，否则False；
info(): 获取任务信息，默认为结果；
wait(t): 等待t秒后获取结果，若任务执行完毕，则不等待直接获取结果，若任务在执行中，则wait期间一直阻塞，直到超时报错；
successful(): 判断任务是否成功，成功为True，否则为False；
"""

print('任务名称', r.name)
print('返回任务id', r.task_id)
print('返回任务结果，同get()方法', r.result)
print('get()方法', r.get(timeout=3))
print('判断任务是否以及有结果，有结果为True，否则False', r.ready())
# print(r.info())
print('等待t秒后获取结果，若任务执行完毕，则不等待直接获取结果，若任务在执行中，则wait期间一直阻塞，直到超时报错', r.wait())
print('判断任务是否成功', r.successful())
print('返回任务状态:', r.state)

r1 = send_mail.delay('test@gmail.com')

sleep(2)
if r1.ready():
    print(r1.result)
    print(r1.get(timeout=3))

if __name__ == '__main__':
    pass
