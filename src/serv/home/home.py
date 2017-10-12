#!/usr/bin/env python
# coding: utf-8


from flask import Blueprint, render_template

from . import home


@home.route('/')
def home_page(page_name=''):
    return render_template('home.html', title='home {}'.format(page_name))
