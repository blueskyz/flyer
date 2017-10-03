#!/usr/bin/env python
# coding: utf-8


from flask import Blueprint, render_template


schd = Blueprint('schd',
                 __name__,
                 template_folder='templates',
                 url_prefix='/schd')
