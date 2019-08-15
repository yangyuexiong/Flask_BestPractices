# -*- coding: utf-8 -*-
# @Time    : 2019-05-16 17:06
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : BaseModel.py
# @Software: PyCharm

from datetime import datetime

from ExtendRegister.db_register import db


class BaseModel(db.Model):
    """
    status:状态
    create_timestamp:创建时间戳
    create_time:创建时间DateTime
    update_timestamp:更新时间戳
    update_time:更新时间DateTime
    """

    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    _status = db.Column('status', db.Integer, default=1)
    _create_time = db.Column('create_time', db.DateTime, default=datetime.now)
    _create_timestamp = db.Column('create_timestamp', db.String(128), default=int(datetime.now().timestamp()))
    _update_time = db.Column('update_time', db.DateTime, default=datetime.now, onupdate=datetime.now)
    _update_timestamp = db.Column('update_timestamp', db.String(128), server_default='',
                                  onupdate=int(datetime.now().timestamp()))

    def __getitem__(self, item):
        return getattr(self, item)

    def to_json(self):
        dict = self.__dict__
        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]
            del dict["_update_timestamp"]
            del dict["_create_timestamp"]
            del dict["_create_time"]
            del dict["_update_time"]
            del dict["_status"]
        return dict

    def update(self, **kwargs):
        # print(self)
        for attr, value in kwargs.items():
            try:  # 部分属性无法setattr
                setattr(self, attr, value)
            except BaseException as e:
                pass
        return self
