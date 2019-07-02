# Flask_BestPractices
## <Flask最佳实践>
#### 包含前后端分离/与不分离模版渲染

---------->>>>>>持续更新<<<<<<----------

后续会使用此结构加上Vue与React实现一套前后分离的博客前后台。

可能会再出Tornado，Sanic，Django等最佳实践。

点个星可好！

Flask官方文档
http://flask.pocoo.org/docs/1.0/

Flask中文文档
https://dormousehole.readthedocs.io/en/latest/

``` 
Flask_BestPractices
    ├── ApplicationExample.py ----------------------->应用实例
    ├── ExtendRegister        ----------------------->扩展统一注册    
    │   ├── __init__.py     
    │   ├── bp_register.py    ------------>蓝图
    │   ├── conf_register.py  ------------>配置文件
    │   ├── db_register.py    ------------>异常处理
    │   ├── excep_register.py ------------>数据库
    │   └── hook_register.py  ------------>拦截器
    ├── Pipfile ------------------------------------->项目环境
    ├── Pipfile.lock
    ├── README.md
    ├── app ----------------------------------------->应用
    │   ├── __init__.py
    │   ├── api -------------------------->前台接口/模块
    │   │   ├── __init__.py -------------->Api url注册与管理
    │   │   └── user
    │   │   │   ├── __init__.py
    │   │   │   └── user.py
    │   │   └── demo
    │   │   │   ├── __init__.py
    │   │   │   └── demo.py -------------->flask resful demo
    │   ├── controllers ------------------>后台接口/模块
    │   │   ├── __init__.py
    │   │   ├── cms     ----------------------------->后台接口/模块
    │   │   │   ├── __init__.py   
    │   │   │   ├── cms_bp.py     ------------>cms蓝图实例(子模块统一在这个文件加入url)与管理
    │   │   │   ├── cms_module_01 ------------>管理后台模块子模块
    │   │   │   │   ├── __init__.py
    │   │   │   │   └── m1.py
    │   │   │   ├── cms_module_02 ------------>管理后台模块子模块
    │   │   │   │   ├── __init__.py
    │   │   │   │   └── m2.py
    │   │   │   └── cms_module_03 ------------>管理后台模块子模块
    │   │   │   │   ├── __init__.py
    │   │   │   │   └── m3.py
    │   │   │   └── demo
    │   │   │   ├── __init__.py
    │   │   │   └── demo.py -------------->MethodView demo
    │   │   ├── other_module_01 --------->其他独立模块独立的蓝图
    │   │   │   ├── __init__.py
    │   │   │   └── module_01.py 
    │   │   ├── other_module_02 --------->其他独立模块独立的蓝图
    │   │   │   ├── __init__.py
    │   │   │   └── module_02.py
    │   │   └── other_module_03 --------->其他独立模块独立的蓝图
    │   │       ├── __init__.py
    │   │       └── module_03.py
    │   ├── models --------------------------------->模型(表)
    │   │   ├── __init__.py
    │   │   ├── admin
    │   │   │   └── models.py
    │   │   └── user
    │   ├── static --------------------------------->静态文件(Js,Css,Img)
    │   └── templates ------------------------------>模版文件(HTML)
    │       ├── index01.html
    │       ├── index02.html
    │       └── index03.html
    ├── common ------------------------------------->公共文件分类
    │   ├── __init__.py
    │   ├── interceptors ------------------------>拦截器(钩子函数分类)
    │   │   ├── ApiHook.py ------------->前台应用拦截处理器
    │   │   ├── AppHook.py ------------->管理后台截处理器
    │   │   ├── CmsHook.py ------------->占位
    │   │   └── __init__.py
    │   └── libs -------------------------------->自定义封装的方法
    │       ├── __init__.py
    │       ├── api_result.py ------------->统一返回json格式
    │       ├── BaseModel.py  ------------->封装的Model基类
    │       ├── tools.py      ------------->工具
    │       └── customException.py -------->自定义flask_restful异常
    ├── config  ------------------------------------>配置文件
    │   ├── __init__.py
    │   └── config.py
    ├── logs    ------------------------------------>日志文件
    │   └── __init__.py
    ├── manage.py ---------------------------------->脚本命令文件
    ├── migrations --------------------------------->数据迁移文件
    │   ├── README
    │   ├── alembic.ini
    │   ├── env.py
    │   ├── script.py.mako
    │   └── versions
    │       └── c53b9b89b620_.py
    ├── run.py   ---------------------------------->启动文件
    ├── tasks    ---------------------------------->定时任务/异步任务
    │   └── __init__.py
    │   └── APSchedulerTasks    ---------------------------------->定时任务
    │       └── clear_logs.py   ---------------------------------->使用/任务/启动方式/例子/解释
    │   └── CeleryAsyncTasks    ---------------------------------->异步任务
    │       └── main.py     ---------------------------------->使用/任务/启动方式/例子/解释
    ├── test     ---------------------------------->测试文件(测试数据文件,单元测试等等)
    │   ├── __init__.py
    │   ├── excep_test.py
    │   ├── test_data.py
    │   └── req_test.py
    │   └── test_celery.py
    └── test_run.py ------------------------------->启动文件

```
### 【使用】
1. 环境配置
    * 安装Python3.6+
    * 安装pip
    * 安装pipenv
        ```
        pip3 install pipenv
        ```
    * 进入根目录安装项目环境(即:所有使用到的python库)
        ```
        pipenv install
        ```
    * pycharm配置pipenv环境

        查看虚拟环境路径
        ```
        pipenv shell
        pipenv --venv
        ```

        pycharm添加

        ![image](/p1.png)
        
        ![image](/p2.png)

        
2. 修改config.py文件
    * 数据库部分(先创建好数据库)
    * 其他配置根据需要修改/增加

3. 创建表(这里我提供了一套简单的后台权限管理:model/admin,可以自己设计你自己的权限管理 和 manage shell) 

    * manage.py文件中已经定义好初始化数据,创建表等方法(根据需要自定义其他方法,详细例子:manage.py文件)
        ```
        查看所有方法:
        pipenv run python3 manage.py
        ```

    * 如直接使用(注意需要在虚拟环境中执行:即 pipenv shell)

        ```
        pipenv run python3 manage.py orm
        ```
    * 新增modle表manage.py导入后再次执行(区别在于没有初始化:python3 manage.py db init)
        ```
        pipenv run python3 manage.py table
        ```

4. 业务实现
    * 前台业务 app/api/下根据需要创建模块在<Flask_BestPractices/app/api/__init__.py>中注册url即可。
    * 后台业务 app/controllers/cms下根据需要创建模块在<Flask_BestPractices/app/controllers/cms/cms_bp.py>注册url即可。
    * 其他分类 app/controllers下根据需要创建模块在<Flask_BestPractices/ExtendRegister/bp_register.py>中注册。

        ```
            假如说我现在需要实现一个前台登录接口:
            1.在<app/models>下创建user表。
            2.manqge.py中导入此表
            3.执行:python3 manage.py table创建该表
                初次创建使用:python3 manage.py orm
            4.<app/api>创建模块和接口并在<app/api/__init__.py>注册
                例子文件:
                    <app/api/user/user.py>
                    <app/api/__init__.py>
            5.实现登录业务
        ```

5. 启动项目

    * Pycharm与终端启动的一些问题--->详细说明在--->config/config.py中

    * 使用Pycharm启动 
        * 使用run.py中的:

        ```
        main('pyc')
        ```
        * ide直接启动

    * 终端启动(如同生产环境)
    * 设置环境(注意也是需要在虚拟环境下执行 即:pipenv shell)
         * 开发环境
        ```
        export FLASK_ENV=development
        ```
        * 生产环境
        ```
        export FLASK_ENV=production
        ```

        * 使用run.py下的
        ```
        main('ter')
        ```
    * 启动
        ```
        pipenv run python3 run.py
        ```
    
6. 访问例子(注意在url末尾要加上'/'否则会出现308报错,或者在定义url时不在末尾加上'/'):

    * api:
        ```
        http://0.0.0.0:9999/api/
        ```
    * cms:
        ```
        http://0.0.0.0:9999/cms/
        ```
    * cms子模块:
        ```
        http://0.0.0.0:9999/cms/test/
        http://0.0.0.0:9999/cms/test2/
        http://0.0.0.0:9999/cms/test3/
        ```
    * 其他业务模块:
        ```
        http://0.0.0.0:9999/m1/
        http://0.0.0.0:9999/m2/
        http://0.0.0.0:9999/m3/

        渲染HTML例子
        http://0.0.0.0:9999/m1/index/
        http://0.0.0.0:9999/m2/index/
        http://0.0.0.0:9999/m3/index/
        ```

7. 钩子函数(拦截器)使用:
    * 拿其中一个举例:<Flask_BestPractices/common/interceptors/ApiHook.py>
    
        ```
        from flask import request, g, jsonify, abort
        from app.api import route_api

        @route_api.before_request
        def before_request_api():
            print('api before_request')
            path = request.path
            print(path)
            if '/api' in path:
                print('访问api')
                return 
        ```

8. 自定义异常添加使用:
    * 在<Flask_BestPractices/common/libs/customException.py>添加
        ```
            1.在文件中添加元组变量 例如
                ServerError = (500, '服务器内部异常')

            2.在下方ab_code方法中的字典 C 中添加key:value 例如
                def ab_code(data):
                    C = {
                        400: Bad_Request,
                        401: NOT_AUTHORIZED,
                        403: FORBIDDEN,
                        500: ServerError,
                        666: not_token
                    }
                    code = C.get(data)[0]
                    msg = C.get(data)[1]
                    raise CustomException(code=code, msg=msg)

            3.调用非常的简单
                例子文件
                    <Flask_BestPractices/app/api/user/user.py>
                例子文件
                    <Flask_BestPractices/app/controllers/cms/cms_bp.py>
                使用:
                    from common.libs.customException import ab_code
                    ab_code(666)
            
        ```
9. 任务
    * 异步任务
    ```
    启动celery例子(必须要在/CeleryAsyncTasks目录下启动):
        /CeleryAsyncTasks/main.py里面含有启动/停止等命令例子,模拟邮件发送任务例子.

    调用任务例子:
        启动后调用任务例子(注意配置好redis,如果使用MQ等其他需要对应修改配置后在启动):
        调用任务例子: /test/test_celery.py
    ```

    * 定时任务
    ```
    使用例子:
        /tasks/APSchedulerTasks/clear_log.py文件中包含3钟常用方法,以清除日子为例子
    启动:
        /APSchedulerTasks目录下直接执行clear_log.py文件
    ```

10. 部署(2019-06-18更新):
    * 我掘金的一篇文章
    
        https://juejin.im/post/5d08574351882563f967d5b9

11. 代码中可能存在大量打印调试代码语句(print('xxxx'))可以将其注释或者删除。

12. 快试试快速实现你业务需求吧！！！嘻嘻！！！