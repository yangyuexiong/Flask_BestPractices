# -*- coding: utf-8 -*-
# @Time    : 2019-05-15 15:40
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : test_run.py
# @Software: PyCharm


from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9999)

