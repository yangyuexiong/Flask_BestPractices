# -*- coding: utf-8 -*-
# @Time    : 2019-05-16 17:06
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : BaseModel.py
# @Software: PyCharm

import json
import decimal
import warnings
import time
from datetime import datetime

from sqlalchemy import text
from sqlalchemy.dialects.mysql import BIGINT, TINYINT

from ExtendRegister.db_register import db


class BaseModel(db.Model):
    """
    id:id
    create_timestamp:创建时间戳
    create_time:创建时间DateTime
    update_timestamp:更新时间戳
    update_time:更新时间DateTime
    is_deleted:是否删除
    status:状态
    """

    __abstract__ = True

    id = db.Column(BIGINT(20, unsigned=True), primary_key=True, autoincrement=True, comment='id')
    create_time = db.Column(db.DateTime, server_default=db.func.now(), comment='创建时间(结构化时间)')
    create_timestamp = db.Column(BIGINT(20, unsigned=True), default=int(time.time()), comment='创建时间(时间戳)')
    update_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now, comment='更新时间(结构化时间)')
    update_timestamp = db.Column(BIGINT(20, unsigned=True), onupdate=int(time.time()), comment='更新时间(时间戳)')
    is_deleted = db.Column(TINYINT(3, unsigned=True), server_default=text('0'), comment='0正常;其他:已删除')
    status = db.Column(TINYINT(3, unsigned=True), server_default=text('1'), comment='状态')

    def keys(self):
        """
        返回所有字段对象
        :return:
        """
        return self.__table__.columns

    def __getitem__(self, item):
        return getattr(self, item)

    def to_json(self, *args):
        """
        json转化
        :param args: 不需要返回的字段列表
        :return:
        """

        model_json = {}
        __dict = self.__dict__

        for column in self.keys():
            field = __dict.get(column.name)  # 获取字段名称
            # print(column, type(column), type(field))
            if isinstance(field, decimal.Decimal):  # Decimal -> float
                field = round(float(field), 2)
            elif isinstance(field, datetime):  # datetime -> str
                field = str(field)
            else:
                pass
            model_json.update({column.name: field})

        if args:
            for skip_field in args:
                if model_json.get(skip_field):
                    del model_json[skip_field]

        return model_json

    def save(self):
        """
        新增
        :return:
        """
        try:
            db.session.add(self)
            db.session.commit()
        except BaseException as e:
            db.session.rollback()
            raise TypeError('save error {}'.format(str(e)))

    @staticmethod
    def save_all(model_list):
        """
        批量新增
        :param model_list:
        :return:
        """
        try:
            db.session.add_all(model_list)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise TypeError('save_all error {}'.format(str(e)))

    def update(self, *args, **kwargs):
        """
        更新
        :param args: 不需要更新的字段列表 demo -> update(*["password"]) ...
        :param kwargs: {字段:值} demo -> update(**{"name":"yyx"}) ...
        :return:
        """
        if args:
            args = list(args) + ['id', 'create_time']
        else:
            args = ['id', 'create_time']

        for attr, value in kwargs.items():
            # print(self, "【{}:{}】-【{}:{}】".format(attr, type(attr), value, type(value)))
            if attr in self.__dict__.keys():
                if attr not in args:
                    new_value = json.dumps(value, ensure_ascii=False) if isinstance(value, dict) else str(value)
                    setattr(self, attr, new_value)
            else:
                pass
        try:
            db.session.commit()
        except BaseException as e:
            db.session.rollback()
            raise TypeError('update error {}'.format(str(e)))

    def delete(self):
        """
        逻辑删除
        :return:
        """
        try:
            self.is_deleted = 2
            db.session.commit()
        except BaseException as e:
            db.session.rollback()
            raise TypeError('delete error {}'.format(str(e)))
