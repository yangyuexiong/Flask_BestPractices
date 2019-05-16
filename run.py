# -*- coding: utf-8 -*-
# @Time    : 2019-05-15 15:52
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : run.py
# @Software: PyCharm


from ApplicationExample import create_app
import os
import threading
from ExtendRegister.hook_register import *  # 导入拦截器
from ExtendRegister.excep_register import *  # 导入异常处理器

app = create_app()


def main(n):
    # 终端
    if n == 'ter':
        app.run(host=app.config['RUN_HOST'], port=app.config['RUN_PORT'])

    # Pycharm
    if n == 'pyc':
        app.run(debug=True, host='0.0.0.0', port=9999)


if __name__ == '__main__':
    pass
    """
    # 设置环境
    export FLASK_ENV=development
    export FLASK_ENV=production
    """
    # print(threading.get_ident())
    print('<', '-' * 66, '>')
    print('起始路径:{}'.format(os.getcwd()))
    print('当前环境:{}'.format(os.environ.get('FLASK_ENV')))
    print('<', '-' * 66, '>')
    # main('ter')
    main('pyc')
