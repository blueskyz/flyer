#!/usr/bin/env python
# coding: utf-8


from flask import Blueprint, render_template

from . import mgr_log


@mgr_log.route('/test/<value>')
def test(value):
    return 'name: {}, value: {}'.format(__name__, value)
