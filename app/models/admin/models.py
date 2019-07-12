# -*- coding: utf-8 -*-
# @Time    : 2019/4/23 9:44 AM
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : models.py
# @Software: PyCharm

from ExtendRegister.db_register import db
from common.libs.BaseModel import BaseModel
from werkzeug.security import generate_password_hash, check_password_hash


# 权限
class CMSPersmission(object):
    # 255的二进制方式来表示 1111 1111
    ALL_PERMISSION = 0b11111111
    # 1. 访问者权限
    VISITOR = 0b00000001
    # 2. 管理帖子权限
    POSTER = 0b00000010
    # 3. 管理评论的权限
    COMMENTER = 0b00000100
    # 4. 管理板块的权限
    BOARDER = 0b00001000
    # 5. 管理前台用户的权限
    FRONTUSER = 0b00010000
    # 6. 管理后台用户的权限
    CMSUSER = 0b00100000
    # 7. 管理后台管理员的权限
    ADMINER = 0b01000000


cms_role_user = db.Table(
    'cms_role_user',  # 表名
    # 字段名:cms_role_id,
    # 类型
    # 外键:cms_role.id,
    # 设置为主键
    db.Column('cms_role_id', db.Integer, db.ForeignKey('cms_role.id'), primary_key=True),
    db.Column('cms_user_id', db.Integer, db.ForeignKey('cms_user.id'), primary_key=True)
)


# CMS角色
class CMSRole(BaseModel):
    __tablename__ = 'cms_role'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    desc = db.Column(db.String(200), nullable=True)
    # create_time = db.Column(db.DateTime, default=datetime.now)
    permissions = db.Column(db.Integer, default=CMSPersmission.VISITOR)

    # 引用模型:CMSUser
    # 中间表:cms_role_user
    # 通过CMSUser反向引用:roles
    users = db.relationship('CMSUser', secondary=cms_role_user, backref='roles')


# CMS用户
class CMSUser(BaseModel):
    __tablename__ = 'cms_user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False)
    _password = db.Column(db.String(100), nullable=False)

    # join_time = db.Column(db.DateTime, server_default=db.func.now())

    def __init__(self, username, password):
        self.username = username
        self.password = password

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw_password):
        self._password = generate_password_hash(raw_password)

    def check_password(self, raw_password):
        result = check_password_hash(self.password, raw_password)
        return result

    @property
    def permissions(self):
        if not self.roles:
            return 0
        all_permissions = 0
        for role in self.roles:
            permissions = role.permissions
            all_permissions |= permissions  # 整合该用户所有权限
            # print('权限包含：', all_permissions)
        return all_permissions

    # 是否拥有权限
    def has_permission(self, permission):
        # all_permissions = self.permissions
        # result = all_permissions&permission == permission
        # return result
        return self.permissions & permission == permission

    # 开发者
    @property
    def is_developer(self):
        return self.has_permission(CMSPersmission.ALL_PERMISSION)

    def __repr__(self):
        return '<admin: 用户名 %s 密码 %s  >' % (
            self.username,
            self.password,
        )
