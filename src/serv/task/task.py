#!/usr/bin/env python
# coding: utf-8


from flask import Blueprint, render_template

from . import task


@task.route('/')
def tasks():
    return render_template('tasks.html', title='task list')


@task.route('/<taskid>')
def task_detail(taskid):
    if not taskid.isdigit():
        raise Exception('taskid error {}'.format(taskid))

    return render_template('tasks.html', title='task detail')


@task.route('/test/<value>')
def test(value):
    return render_template('task.html',
                           title='hello task {}'.format(value))

