# -*- coding: utf-8 -*-
# @Time    : 2019/4/18 4:02 PM
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : config.py
# @Software: PyCharm

import os
import configparser
from datetime import timedelta

import redis


def get_config():
    """获取配置文件"""
    conf = configparser.ConfigParser()
    flask_env = os.environ.get('FLASK_ENV')
    base_path = os.getcwd().split('Flask_BestPractices')[0] + 'Flask_BestPractices/config/'

    default_env = {
        'config_path': base_path + 'dev.ini',
        'msg': '本地配置文件:{}'.format(base_path + 'dev.ini'),
    }

    env_path_dict = {
        'default': default_env,
        'production': {
            'config_path': base_path + 'pro.ini',
            'msg': 'prod配置文件:{}'.format(base_path + 'pro.ini')
        },
    }
    env_obj = env_path_dict.get(flask_env, default_env)
    msg = env_obj.get('msg')
    config_path = env_obj.get('config_path')
    print(msg)
    conf.read(config_path)
    return conf


def app_conf():
    """
    # 设置环境
    export FLASK_ENV=development
    export FLASK_ENV=production

    PS:
    * 由于使用PyCharm直接运行时无法通过os.environ.get('FLASK_ENV')获取到系统变量,所以export FLASK_ENV=='环境'之后FLASK_ENV依然为None。
    ** 在Flask中FLASK_ENV==None 会默认使用production作为环境。
    *** 需要使用终端python run.py执行。os.environ.get('FLASK_ENV')才会生效获取到设置的环境。
    **** 为了方便使用PyCharm进行开发调试:添加使用以下代码将production覆盖。
    解决方法:
    (1)使用以下代码覆盖 //部署生产环境时注释以下代码(不建议使用)
        if not os.environ.get('FLASK_ENV'):
            config_key = 'default'
            print('Pycharm开发环境:%s' % config_key)
            return config_key
    (2)在PyCharm设置变量FLASK_ENV=development
    """
    config_key = 'development'

    if os.environ.get('FLASK_ENV') == 'development':
        config_key = 'development'
        # print('开发环境:%s' % config_key)
        return config_key

    elif os.environ.get('FLASK_ENV') == 'production':
        config_key = 'production'
        # print('生产环境:%s' % config_key)
        return config_key
    else:
        config_key = 'production'
        # print('生产环境:%s' % config_key)
        return config_key


class BaseConfig:
    """配置基类"""
    # SECRET_KEY = os.urandom(24)
    SECRET_KEY = 'ShaHeTop-Almighty-ares'  # session加密
    PERMANENT_SESSION_LIFETIME = timedelta(days=30)  # 设置session过期时间
    DEBUG = True
    # SERVER_NAME = 'example.com'
    RUN_HOST = '0.0.0.0'
    RUN_PORT = 9999

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(BaseConfig):
    """开发环境"""

    """Mysql"""
    HOSTNAME = '127.0.0.1'
    PORT = '3306'
    USERNAME = 'root'
    PASSWORD = '12345678'
    DATABASE = 'Flask_BestPractices'
    # &autocommit=true
    DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(
        USERNAME,
        PASSWORD,
        HOSTNAME,
        PORT,
        DATABASE)
    SQLALCHEMY_DATABASE_URI = DB_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    """Redis"""
    # host是redis主机，需要redis服务端和客户端都起着 redis默认端口是6379
    REDIS_PWD = 123456
    POOL = redis.ConnectionPool(host='localhost', port=6379, password=REDIS_PWD, decode_responses=True, db=1)
    R = redis.Redis(connection_pool=POOL)


class ProductionConfig(BaseConfig):
    """生产环境"""
    DEBUG = False
    RUN_PORT = 5000

    """Mysql"""
    HOSTNAME = '127.0.0.1'
    PORT = '3306'
    USERNAME = 'root'
    PASSWORD = ''
    DATABASE = 'Flask_BestPractices'
    # &autocommit=true
    DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(
        USERNAME,
        PASSWORD,
        HOSTNAME,
        PORT,
        DATABASE)
    SQLALCHEMY_DATABASE_URI = DB_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    """Redis"""
    # host是redis主机，需要redis服务端和客户端都起着 redis默认端口是6379
    REDIS_PWD = 123456
    POOL = redis.ConnectionPool(host='localhost', port=6379, password=REDIS_PWD, decode_responses=True, db=1)
    R = redis.Redis(connection_pool=POOL)


class NewConfig(BaseConfig):
    """区分配置文件"""

    conf = get_config()  # 根据环境变量获取对应的配置文件

    # base
    SECRET_KEY = conf.get('base', 'SECRET_KEY')  # session加密
    PERMANENT_SESSION_LIFETIME = timedelta(days=30)  # 设置session过期时间
    DEBUG = conf.getboolean('base', 'DEBUG')
    RUN_HOST = conf.get('base', 'RUN_HOST')
    RUN_PORT = conf.getint('base', 'RUN_PORT')

    # mysql
    DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(
        conf.get('mysql', 'USERNAME'),
        conf.get('mysql', 'PASSWORD'),
        conf.get('mysql', 'HOSTNAME'),
        conf.getint('mysql', 'PORT'),
        conf.get('mysql', 'DATABASE')
    )
    SQLALCHEMY_DATABASE_URI = DB_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # redis
    redis_obj = {
        'host': conf.get('redis', 'REDIS_HOST'),
        'port': conf.get('redis', 'REDIS_PORT'),
        'password': conf.get('redis', 'REDIS_PWD'),
        'decode_responses': conf.getboolean('redis', 'DECODE_RESPONSES'),
        'db': conf.getint('redis', 'REDIS_DB')
    }
    POOL = redis.ConnectionPool(**redis_obj)
    R = redis.Redis(connection_pool=POOL)


config_obj = {
    'production': ProductionConfig,
    'development': DevelopmentConfig,
    'default': DevelopmentConfig,
    'new': NewConfig
}

if __name__ == '__main__':
    print(config_obj['default'].DB_URI)
    cof = app_conf()
    print(cof)

    print(config_obj['default'].DB_URI)
    print(config_obj['new'].DB_URI)
    print(config_obj['default'].R)
    print(config_obj['new'].R)

    print(config_obj['new'].RUN_HOST)
    print(config_obj['new'].RUN_PORT)
    print(config_obj['new'].DEBUG)
