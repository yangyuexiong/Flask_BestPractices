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

    hidden_fields = []  # 不需要返回的字段与值
    handle_property = False  # 是否调用 gen_property_fields()

    __abstract__ = True

    id = db.Column(BIGINT(20, unsigned=True), primary_key=True, autoincrement=True, comment='id')
    create_time = db.Column(db.DateTime, server_default=db.func.now(), comment='创建时间(结构化时间)')
    create_timestamp = db.Column(BIGINT(20, unsigned=True), default=int(time.time()), comment='创建时间(时间戳)')
    update_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now, comment='更新时间(结构化时间)')
    update_timestamp = db.Column(BIGINT(20, unsigned=True), onupdate=int(time.time()), comment='更新时间(时间戳)')
    is_deleted = db.Column(BIGINT(20, unsigned=True), default=0, comment='0正常;其他:已删除')
    status = db.Column(TINYINT(1, unsigned=True), server_default=text('1'), comment='状态')

    def __getitem__(self, item):
        return getattr(self, item)

    def get_columns(self):
        """
        返回所有字段对象
        :return:
        """
        return self.__table__.columns

    def get_fields(self):
        """
        返回所有字段
        :return:
        """
        return self.__dict__

    def gen_property_fields(self):
        """
        处理 @property 装修的字段，使其在 to_json() 返回原来的字段与值

        class Order(BaseModel):
            __tablename__ = 'order'
            __table_args__ = {'comment': '订单表'}

            _total_amount = db.Column("total_amount", db.DECIMAL(10, 0), default=0, comment='订单总金额')

            @property
            def total_amount(self):
                return self._total_amount / 100

            @total_amount.setter
            def total_amount(self, value):
                self._total_amount = value * 100

        """

        # for name, obj in vars(self.__class__).items():
        #     if isinstance(obj, property):
        #         print(name, obj)
        #         print({name: self.__getattribute__(name)})

        d = {name: self.__getattribute__(name) for name, obj in vars(self.__class__).items() if
             isinstance(obj, property)}

        return d

    @staticmethod
    def var_format(field):
        """字段值类型格式化,防止json格式化错误"""

        if not field:
            return field
        elif isinstance(field, decimal.Decimal):  # Decimal -> float
            field = round(float(field), 2)
        elif isinstance(field, datetime):  # datetime -> str
            field = str(field)
        else:
            pass  # 其他后续补充
        return field

    def to_json(self, hidden_fields=None):
        """
        Json序列化
        :param hidden_fields: 覆盖类属性 hidden_fields
        :return:
        """

        hf = hidden_fields if hidden_fields and isinstance(hidden_fields, list) else self.hidden_fields

        model_json = {}

        for column in self.get_fields():
            if column not in hf:  # 不需要返回的字段与值
                if hasattr(self, column):
                    field = getattr(self, column)
                    model_json[column] = self.var_format(field=field)

        del model_json['_sa_instance_state']

        if self.handle_property:
            property_dict = self.gen_property_fields()
            if property_dict:
                for key, var in property_dict.items():
                    property_dict[key] = self.var_format(field=var)
            model_json.update(property_dict)
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

    def delete(self):
        """
        逻辑删除
        :return:
        """
        try:
            self.is_deleted = self.id
            db.session.commit()
        except BaseException as e:
            db.session.rollback()
            raise TypeError('delete error {}'.format(str(e)))
