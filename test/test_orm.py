# -*- coding: utf-8 -*-
# @Time    : 2022/6/29 16:48
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : test_orm.py
# @Software: PyCharm

from app.models.admin.models import Admin
from common.libs.set_app_context import set_app_context


@set_app_context
def main():
    """main"""
    admin = Admin.query.get(1)
    print(admin.to_json())


if __name__ == '__main__':
    # 测试 handle_property 和 hidden_fields
    setattr(Admin, 'handle_property', True)
    setattr(Admin, 'hidden_fields', ['_password'])
    main()
