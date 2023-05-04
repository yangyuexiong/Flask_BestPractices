# -*- coding: utf-8 -*-
# @Time    : 2019-05-15 15:52
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : run.py
# @Software: PyCharm

import os
import platform
import threading
import datetime

from ApplicationExample import create_app

app = create_app()


def show():
    flask_env = os.environ.get('FLASK_ENV')
    print('<', '-' * 66, '>')
    print('时间:{}'.format(datetime.datetime.now()))
    print('操作系统:{}'.format(platform.system()))
    print('项目路径:{}'.format(os.getcwd()))
    print('当前环境:{}'.format(flask_env))
    print('父进程id:{}'.format(os.getppid()))
    print('子进程id:{}'.format(os.getpid()))
    print('线程id:{}'.format(threading.get_ident()))
    # print(app.url_map)
    print('<', '-' * 66, '>')


def main():
    """启动"""

    host = app.config['RUN_HOST']
    port = app.config['RUN_PORT']
    debug = app.config['DEBUG']

    # Linux服务器启动
    if platform.system() == 'Linux':
        app.run(host=host, port=port)

    else:
        # app.run(debug=True, host='0.0.0.0', port=9999)
        os.environ['is_debug'] = "is_debug"
        app.run(debug=debug, host=host, port=port)


if __name__ == '__main__':
    """
    # 设置环境
    export FLASK_ENV='development'
    export FLASK_ENV='production'
    export FLASK_ENV='docker_production'
    """

    show()
    main()
