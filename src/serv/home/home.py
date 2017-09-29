#!/usr/bin/env python
# coding: utf-8


from flask import Blueprint, render_template


home = Blueprint('home', __name__)


@home.route('/test/<value>')
def test(value):
    return 'name: {}, value: {}'.format(__name__, value)
