#!/usr/bin/env python
# coding: utf-8


from flask import Blueprint, render_template


admin = Blueprint('admin', __name__, url_prefix='/admin')

