# -*- coding: utf-8 -*-
# @Time    : 2022/7/19 10:48
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : celery_app.py
# @Software: PyCharm


from celery import Celery
from ApplicationExample import app


def create_celery(app):
    """

    :param app: Flask应用实例
    :return:
    """

    my_celery = Celery(app.import_name)

    """
    配置方式
    一、直接配置
    
        my_celery.conf.timezone = 'Asia/Shanghai'
    
    二、先加载配置文件，这里是config目录下的celeryconfig.py文件，传递参数时，不用带后缀名
    
        my_celery.config_from_object("config.celeryconfig")
        
    三、加载Flask应用实例的配置文件，这里有个坑，在flask配置文件里写的celery配置得用小写名
    
        my_celery.conf.update(app.config)
    """
    my_celery.config_from_object("config.celeryconfig")

    # 将flask上下文对象加入celery，后续定义任务时，可以使用flask的orm模型
    class ContextTask(my_celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    my_celery.Task = ContextTask
    return my_celery


cel = create_celery(app)

"""
前台执行:
    celery --app=celery_app.cel worker -l INFO

后台执行:
    celery -A celery_app.cel multi start worker --pidfile="$HOME/run/celery/%n.pid" --logfile="$HOME/log/celery/%n%I.log"
    
重启并后台执行:
    celery -A celery_app.cel multi restart worker --pidfile="$HOME/run/celery/%n.pid" --logfile="$HOME/log/celery/%n%I.log"

异步关闭(立即返回):
    celery multi stop worker --pidfile="$HOME/run/celery/%n.pid"

等待关闭(操作完成):
    celery multi stopwait worker --pidfile="$HOME/run/celery/%n.pid"
"""
