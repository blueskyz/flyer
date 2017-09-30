#!/usr/bin/env python
# coding: utf-8


from flask import Blueprint, render_template


home = Blueprint('home', __name__, url_prefix='/home')
