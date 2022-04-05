#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import base64
import json
import urllib.parse
from pathlib import Path

import flask
from flask import Flask, CORS, request, jsonify, render_template


__name__ = 'ahid'


def render_html(html_file, **kwargs):
    return Path(html_file).read_text(encoding='utf-8')


app = Flask(__name__, static_folder='./frontend/assets', template_folder='./frontend')

# enable CORS
#CORS(app, resources={r'/*': {'origins': '*'}})


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

@app.route("/", methods=['GET', 'POST'])
def index():
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
        ssl_context=(
            './backend/ssl/cert.pem',
            './backend/ssl/key.pem'
        )
        #ssl_context='adhoc'
    )

