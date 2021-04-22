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
import datetime

from ApplicationExample import create_app
from ExtendRegister.hook_register import *  # 导入拦截器
from ExtendRegister.excep_register import *  # 导入异常处理器

app = create_app()


def main():
    """启动"""

    # Linux服务器启动
    if platform.system() == 'Linux':
        app.run(host=app.config['RUN_HOST'], port=app.config['RUN_PORT'])

    else:
        # app.run(debug=True, host='0.0.0.0', port=9999)
        app.run(debug=app.config.get('DEBUG'), host=app.config.get('RUN_HOST'), port=app.config.get('RUN_PORT'))


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
    print('<', '-' * 66, '>')
    print('github-地址:https://github.com/yangyuexiong/Flask_BestPractices')
    print('gitee-地址:https://gitee.com/yangyuexiong/Flask_BestPractices')
    print('时间:{}'.format(datetime.datetime.now()))
    print('操作系统:{}'.format(platform.system()))
    print('项目路径:{}'.format(os.getcwd()))
    print('当前环境:{}'.format(flask_env))
    print('父进程id:{}'.format(os.getppid()))
    print('子进程id:{}'.format(os.getpid()))
    print('线程id:{}'.format(threading.get_ident()))
    print('<', '-' * 66, '>')
    main()
