#!/usr/bin/env python
# coding: utf-8


from flask import Blueprint, render_template


home = Blueprint('home',
                 __name__,
                 template_folder='templates',
                 url_prefix='/home')
