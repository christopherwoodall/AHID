#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import base64
from pathlib import Path
import json
import urllib.parse

import flask
from flask import Flask, request, jsonify, render_template


def render_html(html_file, **kwargs):
    return Path(html_file).read_text(encoding='utf-8')

app = Flask(__name__, static_folder='./html/assets', template_folder='./html')

@app.route("/", methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        post_data = json.loads(request.data)
        image_data = post_data['image']
        image_decoded = urllib.parse.unquote(image_data)
        image_bytes = base64.urlsafe_b64decode(image_decoded)
        #Path('test.png').write_bytes(image_bytes)
        from stream import DetectFaces
        d = DetectFaces(image_bytes)

        return base64.urlsafe_b64encode(d.frame_targets).decode('utf-8')
    else:
        return render_html('./html/index.html')


if __name__ == '__main__':
    app.run(
        debug = True,
        host="0.0.0.0",
        ssl_context=('./ssl/cert.pem', './ssl/key.pem')
        #ssl_context='adhoc'
    )

