# -*- coding: utf-8 -*-
# @Time    : 2021/5/29 下午5:47
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : command_register.py
# @Software: PyCharm

import os
import click
import shutil

from common.libs.db import project_db
from ExtendRegister.db_register import db
from app.models.admin.models import Admin, Role, Permission

"""
export FLASK_APP=ApplicationExample.py
"""


def register_commands(app):
    """flask cli"""

    @app.cli.command("hello_world", help='hello-world')
    def hello_world():
        print('hello world')

    @app.cli.command(help='首次进行ORM操作')
    def orm():

        migrations_path = os.getcwd() + "/migrations"

        if os.path.exists(migrations_path):
            shutil.rmtree(migrations_path)
            print(f'>>> migrations 删除: {migrations_path}')
        else:
            print(f'>>> migrations 不存在: {migrations_path}')

        try:
            drop_table_sql = """DROP TABLE IF EXISTS alembic_version;"""
            print(drop_table_sql)
            drop_result = project_db.execute_sql(sql=drop_table_sql)
            print(f'>>> drop_result: {drop_result}')
        except BaseException as e:
            print(f'>>> 删除 alembic_version 失败:{e}')

        try:
            os.system("flask db init")
            os.system("flask db migrate")
            os.system("flask db upgrade")
            print('>>> 创建成功')
        except BaseException as e:
            print(f'>>> 创建失败:{e}')

    @app.cli.command(help='更新表')
    def table():
        try:
            os.system("flask db migrate")
            os.system("flask db upgrade")
            print('>>> 创建成功')
        except BaseException as e:
            print(f'>>> 创建失败:{e}')

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
            print(f'>>> 用户: {username} 已存在')
        else:
            user = Admin(username=username, password=password)
            db.session.add(user)
            db.session.commit()
            print(f'用户: {username} 添加成功')
