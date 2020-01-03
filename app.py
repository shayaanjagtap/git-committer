#!/usr/bin/env python
import json

import committer

from flask import Flask, request, abort

@app.route('/')
def health_check():
    return "I'm healthy, yo!"

@app.route('/update')
def update():

    try:
        data = request.get_json()
    except:
        abort(400)

    try:
        committer.commit(data)
    except:
        abort(500)
