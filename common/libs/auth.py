# -*- coding: utf-8 -*-
# @Time    : 2021/5/11 下午5:55
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : auth.py
# @Software: PyCharm


import uuid

from flask import g

from config.config import config_obj
from common.libs.customException import ab_code_2

"""
test:

import redis

redis_obj = {
    # 'host': conf.get('redis', 'REDIS_HOST'),
    # 'port': conf.get('redis', 'REDIS_PORT'),
    # 'password': conf.get('redis', 'REDIS_PWD'),
    # 'decode_responses': conf.getboolean('redis', 'DECODE_RESPONSES'),
    # 'db': conf.getint('redis', 'REDIS_DB')

    'host': 'localhost',
    'port': 6379,
    'password': 123456,
    'decode_responses': True,
    'db': 10
}
POOL = redis.ConnectionPool(**redis_obj)
R = redis.Redis(connection_pool=POOL)

"""

R = config_obj['new'].R


class Token:
    """
    Token
    """
    token = None

    @classmethod
    def gen_token(cls):
        """生成token"""
        token = str(uuid.uuid1()).replace('-', 'YYx')
        return token

    @classmethod
    def set_token(cls, user):
        """缓存token"""
        token = cls.gen_token()
        cls.token = token
        R.hmset('user:{}'.format(user), {'token': token})
        R.set('token:{}'.format(token), user)
        R.expire('user:{}'.format(user), 3600 * 24 * 30)
        R.expire('token:{}'.format(token), 3600 * 24 * 30)

    @classmethod
    def del_token(cls, token):
        """删除token"""

        """
        通过token查找user
        Input:
            get token:05885a4aYYxa18aYYx11ebYYxa1f9YYxacde48001122
        Output:
            yangyuexiong
            
        
        获取token
        Input:
            hget user:yangyuexiong token
        Output:
            05885a4aYYxa18aYYx11ebYYxa1f9YYxacde48001122
        """

        user = R.get('token:{}'.format(token))
        kv = 'user:{}'.format(user)
        user_token = R.hget(kv, 'token')

        """
        删除
        del yangyuexiong
        del user:yangyuexiong
        del token:13894378YYxa19bYYx11ebYYxa996YYxacde48001122
        """
        R.delete(user)
        R.delete(kv, 'token')
        R.delete('token:{}'.format(user_token))

    @classmethod
    def check_token(cls, user, user_id):
        """检验token"""

        """
        Input:
            hget user:yangyuexiong token
            
        Output:
            05885a4aYYxa18aYYx11ebYYxa1f9YYxacde48001122
        """
        kv = 'user:{}'.format(user)
        user_token = R.hget(kv, 'token')
        if user_token:
            cls.del_token(token=user_token)  # 删除旧token

        cls.set_token(user=user)  # 生成新的token
        R.set(user, user_id, 3600 * 24 * 30)  # 用户(手机,名称等):id


def check_user(token, model):
    """

    :param token: token
    :param model: 用户模型类
    :return:
    """
    # 通过token获取手机号或者username
    # redis命令: get token:7d86561d3742e605e4c0ee42111995cd
    user = R.get('token:{}'.format(token))
    if not user:  # token错误或者失效
        g.app_user = None
        # ab_code(401)
        ab_code_2(401)
    else:
        user_id = R.get(user)  # 通过手机号或其他字段获取用户id  // redis命令: get yyx
        user = model.query.get(user_id)  # 通过id查询用户->获取用户对象
        g.app_user = user  # 创建全局对象


if __name__ == '__main__':
    """
    [redis]
    REDIS_HOST = localhost
    REDIS_PORT = 6379
    REDIS_PWD = 123456
    REDIS_DB = 1
    DECODE_RESPONSES = True
    """

    t = Token()
    t.check_token(user='yangyuexiong', user_id=33)
    print(t.token)
