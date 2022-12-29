# -*- coding: utf-8 -*-
# @Time    : 2021/5/11 下午5:55
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : auth.py
# @Software: PyCharm

import json
import uuid

from config.config import config_obj

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

    def __init__(self):
        self.token = None
        self.mix = "Y"
        self.timeout = 3600 * 24 * 30

    def gen_token(self):
        """
        生成token
        :return:
        """

        token = str(uuid.uuid1()).replace('-', self.mix)
        self.token = token
        return token

    def set_token(self, user_info: dict):
        """
        缓存token
        :param user_info:
        :return:

        1.生成:token
        2.写入:token
        3.写入:user_info

        Redis command
            Input:
                hset user:1-admin "token" "d9d116fcY8671Y11edYa559Yacde48001122"

            Input:
                hset token:d9d116fcY8671Y11edYa559Yacde48001122 "user_info" '{"id":1,"username":"admin"}'
        """

        self.gen_token()
        user_id = user_info.get('id')
        username = user_info.get('username')
        token_key = f"user:{user_id}-{username}"
        user_key = f"token:{self.token}"
        R.hset(name=token_key, mapping={"token": self.token})
        R.hset(name=user_key, mapping={"user_info": json.dumps(user_info, ensure_ascii=False)})
        R.expire(token_key, self.timeout)
        R.expire(user_key, self.timeout)

    @classmethod
    def del_cache(cls, token):
        """
        删除缓存
        :param token:
        :return:

        1.通过token查找user_info
        2.删除token
        3.删除user_info

        Redis command
            Input:
                hget token:d9d116fcY8671Y11edYa559Yacde48001122 user_info

            Output:
                {"id":"1","username":"admin"...}

            Input:
                del user:1-admin

            Input:
                del token:d9d116fcY8671Y11edYa559Yacde48001122

        """

        user_key = f"token:{token}"
        query_user_info = R.hget(user_key, 'user_info')
        if query_user_info:
            user_info = json.loads(query_user_info)
            user_id = user_info.get('id')
            username = user_info.get('username')
            token_key = f"user:{user_id}-{username}"
            R.delete(user_key)
            R.delete(token_key)

    def refresh_cache(self, user_info: dict):
        """
        刷新缓存
        :param user_info:
        :return:

        1.通过用户id-用户名称获取token
        2.删除旧的token与user_info
        3.更新写入token与user_info

        Redis command
            Input:
                hget user:1-admin token

            Output:
                d9d116fcY8671Y11edYa559Yacde48001122
        """

        user_id = user_info.get('id')
        username = user_info.get('username')
        token_key = f'user:{user_id}-{username}'
        old_token = R.hget(token_key, 'token')
        if old_token:
            self.del_cache(token=old_token)  # 删除旧token

        self.set_token(user_info=user_info)  # 生成新的token并写入Redis

    @staticmethod
    def get_user_info(token):
        """
        通过token或用户信息
        :param token:
        :return:
        """

        query_token = R.hget(f"token:{token}", 'user_info')
        if query_token:
            user_info = json.loads(query_token)
            return user_info
        else:
            return None


if __name__ == '__main__':
    t = Token()
    d = {
        "id": 1,
        "is_deleted": 0,
        "code": "00001",
        "status": 1,
        "login_type": None,
        "username": "admin",
        "creator": "shell",
        "create_time": "2021-11-11 11:15:29",
        "nickname": "yyx",
        "creator_id": 0,
        "modifier": "admin",
        "create_timestamp": 1636600147,
        "phone": "15011111111",
        "modifier_id": 1,
        "update_time": "2022-08-17 17:53:07",
        "mail": "yang6333yyx@126.com",
        "remark": "游客",
        "update_timestamp": 1660729764
    }
    t.refresh_cache(user_info=d)
    print(t.token)
    user_info = t.get_user_info(token=t.token)
    print(user_info)
