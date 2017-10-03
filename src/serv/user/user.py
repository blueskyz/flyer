#!/usr/bin/env python
# coding: utf-8


from flask import Blueprint, render_template

from . import user


@user.route('/test/<value>')
def test(value):
    return 'name: {}, value: {}'.format(__name__, value)


@user.route('/testtpl/<value>')
def testtpl(value):
    return render_template('user.html')
