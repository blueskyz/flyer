#!/usr/bin/env python
# coding: utf-8


from flask import Blueprint, render_template


mgr_log = Blueprint('mgr_log', __name__, url_prefix='/mgrlog')

@mgr_log.route('/test/<value>')
def test(value):
    return 'name: {}, value: {}'.format(__name__, value)
