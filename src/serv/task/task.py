#!/usr/bin/env python
# coding: utf-8


from flask import Blueprint, render_template


task = Blueprint('task', __name__, url_prefix='/task')

@task.route('/test/<value>')
def test(value):
    return 'name: {}, value: {}'.format(__name__, value)
