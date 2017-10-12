#!/usr/bin/env python
# encoding: utf-8


from flask import Flask
from flask import redirect
from flask_admin import Admin
from flask_admin import BaseView
from flask_bootstrap import Bootstrap


from home.home import home_page
from home.home import home
from task.task import task
from schd.schd import schd
from user.user import user
from mgr_log.mgr_log import mgr_log


app = Flask(__name__)
Bootstrap(app)

# 添加管理界面
admin = Admin(app, name='管理', template_mode='bootstrap3')


# 注册 blueprint
app.register_blueprint(home)
app.register_blueprint(task)
app.register_blueprint(schd)
app.register_blueprint(user)
app.register_blueprint(mgr_log)


@app.route('/')
def jump_home(page_name=''):
    return redirect('/home/',  code=301)


# print(list(app.url_map.iter_rules()))
# print(app.template_folder)
print(app.blueprints['admin'].template_folder)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8880, debug=True)
