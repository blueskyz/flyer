#!/usr/bin/env python
# coding: utf-8


from flask import Blueprint, render_template


task = Blueprint('task',
                 __name__,
                 template_folder='templates',
                 url_prefix='/task')

