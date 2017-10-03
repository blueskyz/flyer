#!/usr/bin/env python
# coding: utf-8


from flask import Blueprint, render_template

from . import home


@home.route('/test/<value>')
def test(value):
    return render_template('home.html')
