# -*- coding: utf-8 -*-
# @Time    : 2019/4/18 10:44 AM
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : manage.py
# @Software: PyCharm

import os

from flask_script import Manager, Server, Command
from flask_migrate import Migrate, MigrateCommand

from ApplicationExample import create_app
from ExtendRegister.db_register import db
from app.models.admin import models as cms_models

app = create_app()  # 实例
manager = Manager(app)  # 绑定
Migrate(app, db)
manager.add_command('db', MigrateCommand)  # 添加命令

# CMS
CMSUser = cms_models.CMSUser
CMSRole = cms_models.CMSRole
CMSPermission = cms_models.CMSPersmission


# 自定义命令一：
class Hello(Command):
    'hello world'

    def run(self):
        print('hello world')


class TableCreateFirst(Command):
    """首次映射并且创建表"""

    def run(self):
        try:
            os.system("python3 manage.py db init")
            os.system("python3 manage.py db migrate")
            os.system("python3 manage.py db upgrade")
            print('创建成功')
        except BaseException as e:
            print('创建失败:{}'.format(str(e)))


class TableCreate(Command):
    """增加表"""

    def run(self):
        try:
            os.system("python3 manage.py db migrate")
            os.system("python3 manage.py db upgrade")
            print('创建成功')
        except BaseException as e:
            print('创建失败:{}'.format(str(e)))


# 添加命令
manager.add_command('hello', Hello())
manager.add_command('orm', TableCreateFirst())
manager.add_command('table', TableCreate())


# CMS权限
@manager.command
def create_role():
    """创建后台管理角色"""
    # 1. 酱油小伙子
    visitor = CMSRole(name='酱油小伙子', desc='Lv===1')
    visitor.permissions = CMSPermission.VISITOR

    # 2. 普通管理员（修改个人个人信息，管理帖子，管理评论，管理前台用户）
    operator = CMSRole(name='运营', desc='Lv===33')
    operator.permissions = CMSPermission.VISITOR | CMSPermission.POSTER | CMSPermission.CMSUSER | CMSPermission.COMMENTER | CMSPermission.FRONTUSER

    # 3. 管理员（拥有绝大部分权限）
    admin = CMSRole(name='管理员', desc='Lv===88')
    admin.permissions = CMSPermission.VISITOR | CMSPermission.POSTER | CMSPermission.CMSUSER | CMSPermission.COMMENTER | CMSPermission.FRONTUSER | CMSPermission.BOARDER

    # 4. 博主
    developer = CMSRole(name='博主', desc='Lv===99')
    developer.permissions = CMSPermission.ALL_PERMISSION

    db.session.add_all([visitor, operator, admin, developer])
    db.session.commit()
    print('角色创建完成')


@manager.option('-u', '--username', dest='username')
@manager.option('-p', '--password', dest='password')
def create_cms_user(username, password):
    """创建后台管理用户"""
    user = CMSUser(username=username, password=password)
    db.session.add(user)
    db.session.commit()
    print('cms用户添加成功')


# 赋予用户权限
@manager.option('-u', '--username', dest='username')
@manager.option('-n', '--name', dest='name')
def add_user_to_role(username, name):
    """为角色添加权限"""
    user = CMSUser.query.filter_by(username=username).first()
    if user:
        role = CMSRole.query.filter_by(name=name).first()
        if role:
            role.users.append(user)
            db.session.commit()
            print('用户添加到角色成功！')
        else:
            print('没有这个角色：%s' % role)
    else:
        print('用户:%s不存在!' % username)


# 自定义命令二：
# web server
manager.add_command("runserver",
                    Server(
                        host='0.0.0.0',
                        port=7777,
                        use_debugger=True,
                        use_reloader=True
                    ))


def main():
    manager.run()


if __name__ == '__main__':
    try:
        import sys

        sys.exit(main())
    except Exception as e:
        import traceback

        traceback.print_exc()

    '''
    数据库
    在pipenv环境中在每个命令前加上 pipenv run
    如:pipenv run python3 manage.py 
    '''
    # 初始化迁移环境:python3 manage.py db init
    # 迁移数据库:python3 manage.py db migrate
    # 映射数据库:python3 manage.py db upgrade
    # 回滚:
    #   ps:先备份数据
    #       python3 manage.py db history
    #       python3 manage.py db downgrade id
    '''CMS角色'''
    # 创建后台管理角色:python3 manage.py create_role
    '''CMS用户'''
    # 创建后台管理用户:python3 manage.py create_cms_user -u yyx -p 666666
    '''权限'''
    # 为角色添加权限:python3 manage.py add_user_to_role -u yyx -n 博主
    '''测试'''
    # 测试权限控制:python3 manage.py test_permission
