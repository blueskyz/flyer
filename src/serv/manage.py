#!/usr/bin/env python
# encoding: utf-8


from flask import Flask


from home.home import home
from task.task import task
from schd.schd import schd
from admin.admin import admin
from mgr_log.mgr_log import mgr_log


app = Flask(__name__)

# 注册 blueprint
app.register_blueprint(home)
app.register_blueprint(task)
app.register_blueprint(schd)
app.register_blueprint(admin)
app.register_blueprint(mgr_log)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8880)
