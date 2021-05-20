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
    is_deleted = db.Column(TINYINT(3, unsigned=True), server_default=text('1'), comment='1正常;2已删除')
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

    def update(self, **kwargs):
        """
        更新
        :param kwargs:
        :return:
        """

        warnings.warn('该方法存在安全隐患,使用不当会导致数据错乱,建议停止使用')
        for attr, value in kwargs.items():
            print(self, attr, type(attr), value, type(value))
            try:  # 部分属性无法setattr
                setattr(self, attr, json.dumps(value, ensure_ascii=False) if isinstance(value, dict) else str(value))
            except BaseException as e:
                raise TypeError('update error {}'.format(str(e)))

    def delete(self):
        """
        逻辑删除
        :return:
        """
        self.is_deleted = 2
        db.session.commit()
