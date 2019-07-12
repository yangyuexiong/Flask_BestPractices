# Flask_BestPractices
## <Flask最佳实践>
##### 包含前后端分离/与不分离模版渲染


---------->>>>>>持续更新<<<<<<----------

后续会使用此结构加上Vue与React实现一套前后分离的博客前后台。

可能会再出Tornado，Sanic，Django等最佳实践。

点个星可好！

如有发现问题 issues

Flask官方文档
http://flask.pocoo.org/docs/1.0/

Flask中文文档
https://dormousehole.readthedocs.io/en/latest/

```
Flask_BestPractices
├── ApplicationExample.py   ----------------------->应用实例
├── ExtendRegister          ----------------------->扩展统一注册
│   ├── __init__.py
│   ├── bp_register.py      ------------>蓝图
│   ├── conf_register.py    ------------>配置文件
│   ├── db_register.py      ------------>数据库
│   ├── excep_register.py   ------------>异常统一捕获         
│   └── hook_register.py    ------------>拦截器
├── Pipfile --------------------------------------->项目环境
├── Pipfile.lock
├── README.md
├── app ------------------------------------------->应用
│   ├── __init__.py
│   ├── api --------------------------->前台接口/模块
│   │   ├── __init__.py --------------->Api url注册与管理
│   │   └── demo        --------------->例子模块
│   │       ├── __init__.py
│   │       └── demo.py --------------->flask resful demo
│   ├── controllers ------------------->管理后台接口/模块/其他业务模块
│   │   ├── __init__.py
│   │   ├── cms     ------------------->后台接口/模块
│   │   │   ├── __init__.py
│   │   │   ├── cms_bp.py  ------------>cms蓝图实例(子模块统一在这个文件注册url)与管理
│   │   │   ├── cms_module_01  ------------>管理后台模块子模块
│   │   │   │   ├── __init__.py
│   │   │   │   └── m1.py
│   │   │   ├── cms_module_02  ------------>管理后台模块子模块
│   │   │   │   ├── __init__.py
│   │   │   │   └── m2.py
│   │   │   ├── cms_module_03  ------------>管理后台模块子模块
│   │   │   │   ├── __init__.py
│   │   │   │   └── m3.py
│   │   │   └── demo
│   │   │       ├── __init__.py
│   │   │       └── demo.py  ------------>MethodView demo
│   │   ├── other_module_01  ------------>其他独立模块/独立的蓝图
│   │   │   ├── __init__.py
│   │   │   └── module_01.py
│   │   ├── other_module_02  ------------>其他独立模块/独立的蓝图
│   │   │   ├── __init__.py
│   │   │   └── module_02.py
│   │   └── other_module_03  ------------>其他独立模块/独立的蓝图
│   │       ├── __init__.py
│   │       └── module_03.py
│   ├── models  ----------------------------------->模型(表)
│   │   ├── __init__.py
│   │   └── admin  -------------------------------->admin模型
│   │       └── models.py
│   ├── static  ----------------------------------->静态文件(Js,Css,Img)
│   └── templates  -------------------------------->模版文件(HTML)用于模版渲染(前后分离一般不是哟噶这里只作为一个例子)
│       ├── index01.html
│       ├── index02.html
│       └── index03.html
├── common  --------------------------------------->公共文件分类
│   ├── __init__.py
│   ├── interceptors  ----------------------------->拦截器(钩子函数分类)
│   │   ├── ApiHook.py  ------------->前台应用拦截处理器(即:访问api开头的url时做的逻辑处理)
│   │   ├── AppHook.py  ------------->占位
│   │   ├── CmsHook.py  ------------->管理后台拦截处理器(即:访问cms开头的url时做的逻辑处理)
│   │   └── __init__.py
│   └── libs  ------------------------------------->自定义封装的方法
│       ├── BaseModel.py  ------------->模型基类(封装了一些模型(表)必须要的字段以及方法)(在创建模型时导入并继承即可:例子:/models/admin/models.py)
│       ├── __init__.py
│       ├── api_result.py ------------->统一返回json格式规范
│       ├── customException.py  ------->自定义异常处理
│       └── tools.py      ------------->工具
├── config  -------------------------------------->配置文件
│   ├── __init__.py
│   └── config.py
├── logs  ---------------------------------------->日志文件
│   ├── __init__.py
│   └── tb.log
├── manage.py  ----------------------------------->脚本命令文件(初始化迁移环境,迁移数据库,映射数据库等一系列的操作)
├── migrations ----------------------------------->数据迁移文件(会在初始化迁移环境后生成)
│   ├── README
│   ├── alembic.ini
│   ├── env.py
│   ├── script.py.mako
│   └── versions
│       └── 0e756d5e6363_.py
├── p1.png
├── p2.png
├── run.py  ------------------------------------>项目启动文件
├── tasks   ------------------------------------>定时任务/异步任务
│   ├── APSchedulerTasks  ---------------------->定时任务
│   │   ├── clear_logs.py ---------------------->使用/任务/启动方式/例子/解释
│   │   └── test.log
│   ├── CeleryAsyncTasks  ---------------------->异步任务
│   │   ├── __init__.py
│   │   ├── celeryconfig.py
│   │   ├── main.py       ---------------------->使用/任务/启动方式/例子/解释
│   │   ├── w1-1.log      ---------------------->异步任务后台启动日志文件启动后自动生成/停止后自动删除主进程文件即:w1.log
│   │   ├── w1-2.log
│   │   ├── w1-3.log
│   │   ├── w1-4.log
│   │   └── w1.log        ---------------------->主进程文件记录进程的PID
│   └── __init__.py
├── test    ------------------------------------>测试文件(测试数据文件,单元测试等等)
│   ├── __init__.py
│   ├── excep_test.py  ------------------------->测试异常
│   ├── req_test.py    ------------------------->测试接口
│   ├── test_celery.py ------------------------->测试异步任务调用
│   └── test_data.py  -------------------------->测试的数据
└── test_run.py  ------------------------------->调试启动文件(可以忽略或者删除)

```
### 【使用】
1. 环境配置
    * 安装Python3.7+
    * 安装pip3
    * 安装pipenv
        ```
        pip3 install pipenv
        ```
    * 进入根目录安装项目环境(即:所有使用到的python库)
        ```
        pipenv install
        ```
    * 查看虚拟环境路径
        ```
        pipenv shell
        pipenv --venv
        ```

    * pycharm配置pipenv环境

        pycharm添加

        ![image](/p1.png)
        
        ![image](/p2.png)


    * 配置Pycharm的Flask变量(因为Pycharm运行项目不会读取系统变量所有要配置在Pycharm中)

        ![image](/p7.png)
        ![image](/p8.png)
        ![image](/p9.png)

        这样Pycharm运行就有了环境变量

    * 配置Flask系统变量(原本操作系统中是没有FLASK_ENV变量的所以flask启动的时候默认为production,为了区分开发/生产需要通过一下方式配置)(以下配置只能在终端启动项目生效在Pycharm不生效)
        
        方法一(这种方法在每次启动项目前都必须设置一次,因为不会保存在操作系统中):
            在终端键入(属于临时变量使用之后就会失效)

            ```
            开发环境:
                export FLASK_ENV=development
            生成环境:                
                export FLASK_ENV=production
            ```
        方法二(直接把变量写在操作系统中):

        Windows系统(一般用于开发环境,所有配置为开发的变量:development):        

        ![image](/p3.png)

        变量名填入:FLASK_ENV

        变量值填入:development

        MacOS系统(同样也配置为开发环境,所有配置为开发的变量:development):

        打开文件找到 .bash_profile文件(如果没看到这个文件 按: shift按键+command按键+ . 按键。就会显示隐藏文件因为隐藏文件一般不显示/需要使其隐藏 再按一次 shift按键+command按键+ . 按键)

        或者可以在终端键入 : vim ~/.bash_profile 添加完 保存。键入:sourec ~/.bash_profile 生效配置文件。

        如果想切换生产环境则修改配置环境即可。

        ![image](/p4.png)

        ![image](/p5.png)

        Linux系统(一般使用为生产环境,所有配置为生产的变量:production)
        
        与MacOS系统类似只是文件名称有些区别: vim ~/.bashrc 添加完 保存。键入:sourec ~/.bashrc 生效配置文件。

        ![image](/p6.png)

2. 尝试启动项目:

    ide运行:
    * 更换注释-使用run.py中的:

        ```
        main('pyc')
        ```

    * Pycharm启动项目(因为已经配置好了pipenv与FLASK_ENV)所以可以直接运行run.py文件

    终端运行:
    * 更换注释-使用run.py下的
        ```
        main('ter')
        ```
    * 进入到项目根目录
        ```
        进入虚拟环境:
            pipenv shell
        启动:
            python3 run.py
        ```

3. 访问例子(注意在url末尾要加上'/'否则会出现308报错,或者在定义url时不在末尾加上'/')

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
        http://0.0.0.0:9999/cms/test1/
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

4. 修改config.py文件
    * 数据库部分(先创建好数据库)
    * 其他配置根据需要修改/增加


5. 创建表(这里我提供了一套简单的后台权限管理:model/admin,可以自己设计你自己的权限管理 和 manage shell) 

    * manage.py文件中已经定义好初始化数据,创建表等方法(根据需要自定义其他方法,详细例子:manage.py文件)
        ```
        查看所有方法:
        pipenv run python3 manage.py
        ```

    * 首次!首次!首次! 创建表时执行(注意需要在虚拟环境中执行:即 pipenv shell)

        ```
        pipenv run python3 manage.py orm
        ```
    * 每次！每次！每次！新增modle表后在manage.py导入后执行(区别在于没有初始化:python3 manage.py db init)
        ```
        pipenv run python3 manage.py table
        ```

6. 业务实现
    * 前台业务 app/api/下根据需要创建模块在<Flask_BestPractices/app/api/__init__.py>中注册url即可。
    例子: /app/api/__init__.py
    * 后台业务 app/controllers/cms下根据需要创建模块在<Flask_BestPractices/app/controllers/cms/cms_bp.py>注册url即可。
    * 其他分类 app/controllers下根据需要创建模块在<Flask_BestPractices/ExtendRegister/bp_register.py>中注册。
    例子: /app/controllers/cms/cms_bp.py


7. 钩子函数(拦截器)使用:
    * 拿其中一个举例:<Flask_BestPractices/common/interceptors/ApiHook.py>业务逻辑根据自己需要编写
    
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
                    <Flask_BestPractices/app/api/demo/demo.py>中的
                    ```
                    class CustomExceptionTest(Resource):

                        def get(self):
                            """
                            测试自定义异常

                            :return:
                            """
                            ab_code(333)
                    ```
                例子文件
                    <Flask_BestPractices/app/controllers/cms/cms_bp.py>中的
                    ```
                    @route_admin.route('/test_custom_exception', methods=["GET", "POST"])
                    def t_custom_exc():
                        """测试自定义异常"""
                        ab_code(666)
                    ```
                使用:
                    from common.libs.customException import ab_code
                    ab_code(666)
            
        ```
9. 任务
    * 异步任务
    ```
    注意:配置好redis,如果使用MQ等其他需要对应修改配置后在启动
    启动celery例子(必须要在/CeleryAsyncTasks目录下启动以及配置好redis):
        /CeleryAsyncTasks/main.py里面含有启动/停止等命令例子,模拟邮件发送任务例子.

    调用任务例子:
        启动后调用任务例子:
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