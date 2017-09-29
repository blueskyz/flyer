#!/usr/bin/env python
# coding: utf-8


from flask import Blueprint, render_template


schd = Blueprint('schd', __name__, url_prefix='/schd')

@schd.route('/test/<value>')
def test(value):
    return 'name: {}, value: {}'.format(__name__, value)
