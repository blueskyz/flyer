#!/usr/bin/env python
# encoding: utf-8


from flask import Flask
from flask_admin import Admin as fAdmin


from home.home import home
from task.task import task
from schd.schd import schd
from user.user import user
from mgr_log.mgr_log import mgr_log


app = Flask(__name__)

admin = fAdmin(app, name='microblog', template_mode='bootstrap3')


# 注册 blueprint
app.register_blueprint(home)
app.register_blueprint(task)
app.register_blueprint(schd)
app.register_blueprint(user)
app.register_blueprint(mgr_log)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8880, debug=True)
