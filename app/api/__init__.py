# -*- coding: utf-8 -*-
# @Time    : 2019/4/18 11:03 AM
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : __init__.py.py
# @Software: PyCharm

from flask import Blueprint
from flask_restful import Api

from .restful_demo.restful_demo import RestfulDemoApi, DemoApi
from .method_view_demo.method_view_demo import MethodViewDemo
from .demo_api.demo_api import MethodViewParams, MethodViewJson, MethodViewFormData, MethodViewBytesData
from .route_demo.route_demo import module_01_index
from .test_api.test_api import TestRestful, TestMethodView, TestCeleryTask

method_view_api = Blueprint('cms', __name__)
restful_api = Blueprint('api', __name__)
api = Api(restful_api)

"""
flask restful 路由注册
带参数url 可以一起注册
无参数：http://0.0.0.0:9999/api/demo
带参数：http://0.0.0.0:9999/api/demo/123/456
api.add_resource(DemoApi, '/demo', '/demo/<page>/<size>', endpoint='demo')
"""
api.add_resource(DemoApi, '/demo', '/demo/<page>/<size>', endpoint='demo')
api.add_resource(RestfulDemoApi, '/', endpoint='restful_demo_api')
api.init_app(restful_api)

"""
Method View 类视图路由注册
带参数 url 需要分开注册
无参数: http://0.0.0.0:9999/cms/demo
带参数: http://0.0.0.0:9999/cms/demo/999/888
"""

method_view_api.add_url_rule('/', view_func=MethodViewDemo.as_view('demo_get'))
method_view_api.add_url_rule('/demo', view_func=MethodViewDemo.as_view('demo_post'))
method_view_api.add_url_rule('/demo/<page>/<size>/', view_func=MethodViewDemo.as_view('demo_pram'))

"""
获取请求参数例子(与上述的flask_restful一致,这里只用 MethodView 作为例子)
"""
method_view_api.add_url_rule('/mv_params', view_func=MethodViewParams.as_view('mv_params'))
method_view_api.add_url_rule('/mv_json', view_func=MethodViewJson.as_view('mv_json'))
method_view_api.add_url_rule('/mv_form_data', view_func=MethodViewFormData.as_view('mv_form_data'))
method_view_api.add_url_rule('/mv_bytes_data', view_func=MethodViewBytesData.as_view('mv_bytes_data'))

"""
路由注册

@method_view_api.route('/', methods=["GET", "POST"])
def index():
    return jsonify('this cms')

上面方式等价于以下方式(统一管理路由):

def index():
    return jsonify('this cms')
    
route_admin.add_url_rule('/index', methods=["GET", "POST"], endpoint='index', view_func=index)

"""
method_view_api.add_url_rule('/m1', methods=["GET", "POST"], endpoint='module_01_index', view_func=module_01_index)

"""
静态文件处理/访问方式
http://0.0.0.0:9999/static/flask.jpg
http://0.0.0.0:9999/static/images/flask.jpg
"""

"""
测试全局异常
"""
api.add_resource(TestRestful, '/test_restful_ex', endpoint='test_restful_ex')
method_view_api.add_url_rule('/test_mv_ex', view_func=TestMethodView.as_view('test_mv_ex'))
method_view_api.add_url_rule('/test_celery', view_func=TestCeleryTask.as_view('test_celery'))


@method_view_api.route('/<path:path>/images')
def static_file(path):
    return method_view_api.send_static_file(path)
