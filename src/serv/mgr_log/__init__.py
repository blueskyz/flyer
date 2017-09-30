#!/usr/bin/env python
# coding: utf-8


from flask import Blueprint, render_template


mgr_log = Blueprint('mgr_log', __name__, url_prefix='/mgr_log')

