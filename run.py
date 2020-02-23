# -*- coding: utf-8 -*-
# @Time    : 2019-05-15 15:52
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : run.py
# @Software: PyCharm

import os
import warnings
import platform
import threading

from ApplicationExample import create_app
from ExtendRegister.hook_register import *  # 导入拦截器
from ExtendRegister.excep_register import *  # 导入异常处理器

app = create_app()


def run_tips(x):
    msg = ''
    if x == 'FLASK_ENV':
        msg = '\n\nTips:未找到Flask环境变量 "FLASK_ENV" 请配置!如需了解配置可查阅:https://github.com/yangyuexiong/Flask_BestPractices\n\n'
    if x == 'STARTUP_MODE':
        msg = '\n\nTips:未找到启动项目方式变量 "STARTUP_MODE" 请配置!如需了解配置可查阅:https://github.com/yangyuexiong/Flask_BestPractices\n\n'

    print("\033[31m{}\033[0m".format(msg))


def check_env(*args):
    """检查环境变量"""
    for i in args:
        if not os.environ.get(str(i)):
            run_tips(str(i))


def main():
    """启动"""
    # 必须变量
    check_env('FLASK_ENV')

    # Linux服务器启动
    if platform.system() == 'Linux':
        app.run(host=app.config['RUN_HOST'], port=app.config['RUN_PORT'])

    check_env('STARTUP_MODE')

    # 终端
    if os.environ.get('STARTUP_MODE') == 'ter':
        app.run(host=app.config['RUN_HOST'], port=app.config['RUN_PORT'])

    # Pycharm
    if os.environ.get('STARTUP_MODE') == 'pyc':
        app.run(debug=True, host='0.0.0.0', port=9999)

    else:
        pass


if __name__ == '__main__':
    pass
    """
    # 设置环境
    export FLASK_ENV=development
    export FLASK_ENV=production
    
    export STARTUP_MODE=pyc
    export STARTUP_MODE=ter
    
    # 调试
    os.environ.get('FLASK_ENV')
    os.environ.get('STARTUP_MODE')
    """

    flask_env = os.environ.get('FLASK_ENV')
    startup_mode = os.environ.get('STARTUP_MODE')
    print('<', '-' * 66, '>')
    print('时间:{}'.format(datetime.datetime.now()))
    print('操作系统:{}'.format(platform.system()))
    print('项目路径:{}'.format(os.getcwd()))
    print('当前环境:{}'.format(flask_env))
    print('启动方式:{}'.format(startup_mode))
    print('threading:', threading.get_ident())
    print('当前进程id:', os.getpid())
    print('父进程id:', os.getppid())
    print('<', '-' * 66, '>')
    main()
