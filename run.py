# -*- coding: utf-8 -*-
# @Time    : 2019-05-15 15:52
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : run.py
# @Software: PyCharm


from ApplicationExample import create_app
import os
import platform
import threading
from ExtendRegister.hook_register import *  # 导入拦截器
from ExtendRegister.excep_register import *  # 导入异常处理器

app = create_app()


def main():

    # Linux服务器启动
    if platform.system() == 'Linux':
        app.run(host=app.config['RUN_HOST'], port=app.config['RUN_PORT'])

    # 终端
    if os.environ.get('STARTUP_MODE') == 'ter':
        app.run(host=app.config['RUN_HOST'], port=app.config['RUN_PORT'])

    # Pycharm
    if os.environ.get('STARTUP_MODE') == 'pyc':
        app.run(debug=True, host='0.0.0.0', port=9999)

    else:
        print('Error:未找到启动项目方式的变量,如需了解配置\n可查阅:https://github.com/yangyuexiong/Flask_BestPractices ')


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
    # print(threading.get_ident())
    print('<', '-' * 66, '>')
    print('操作系统:{}'.format(platform.system()))
    print('项目路径:{}'.format(os.getcwd()))
    print('当前环境:{}'.format(os.environ.get('FLASK_ENV')))
    print('启动方式:{}'.format(os.environ.get('STARTUP_MODE')))
    print('<', '-' * 66, '>')
    main()
