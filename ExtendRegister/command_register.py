# -*- coding: utf-8 -*-
# @Time    : 2021/5/29 下午5:47
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : command_register.py
# @Software: PyCharm

import os
import click

from ExtendRegister.db_register import db
from app.models.admin.models import Admin, Role, Permission


def register_commands(app):
    @app.cli.command("hello_world", help='hello-world')
    def hello_world():
        print('hello world')

    @app.cli.command(help='首次进行ORM操作')
    def orm():
        try:
            os.system("flask db init")
            os.system("flask db migrate")
            os.system("flask db upgrade")
            print('创建成功')
        except BaseException as e:
            print('创建失败:{}'.format(str(e)))

    @app.cli.command(help='更新表')
    def table():
        try:
            os.system("flask db migrate")
            os.system("flask db upgrade")
            print('创建成功')
        except BaseException as e:
            print('创建失败:{}'.format(str(e)))

    @app.cli.command(help='创建用户角色权限')
    def crm():
        try:
            user = Admin.query.filter_by(username='admin').first()
            if user:
                pass
            else:
                user = Admin(username='admin', password='123456')
                db.session.add(user)
                db.session.commit()
                print('cms用户添加成功')
            for r in range(1, 5):
                role_obj = Role(name='角色{}'.format(str(r)))
                db.session.add(role_obj)
            db.session.commit()
            print('cms角色添加成功')

            for p in range(1, 5):
                permission_obj = Permission(name='权限{}'.format(str(p)))
                db.session.add(permission_obj)
            db.session.commit()
            print('cms权限添加成功')
        except BaseException as e:
            print('出错:{}'.format(str(e)))

    @app.cli.command("create_user", help="创建用户")
    @click.option("--username", help="用户名", type=str)
    @click.option("--password", help="密码", type=str)
    def create_user(username, password):
        """
        command: flask create-user --username yyx --password 123456
        """

        query_user = Admin.query.filter_by(username=username).first()
        if query_user:
            print('用户:{}'.format(username))
        else:
            user = Admin(username=username, password=password)
            db.session.add(user)
            db.session.commit()
            print('用户: {} 添加成功'.format(username))
