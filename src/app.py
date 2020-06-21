# -*- coding: utf8 -*-
import json
import sys
import traceback
import src.common.util as util

from flask import Flask, escape, request, jsonify, Response

from src import __version__

app = Flask(__name__)
args = util.arg_conf()

your_rest_server_ip = "0.0.0.0"
your_rest_server_port = "5000"


@app.route('/')
def index():
    return 'hello'


@app.route('/hello', methods=['GET', 'POST'])
def hello():
    name = request.args.get("name", "World")
    return f'Hello-1, {escape(name)}!'


@app.errorhandler(Exception)
def handle_error(error):
    print(error, 'error')
    trace = traceback.format_exc()
    print(trace)
    msg = ('%s' % error)
    return jsonify(code=-1, message='error', data=msg, trace=trace)


def run():
    print('version:' + __version__)
    length = len(sys.argv)
    app.run(
        host=args.bind,
        port=args.ip,
        debug=args.debug
    )


if __name__ == '__main__':
    app.run(
        host=your_rest_server_ip,
        port="12322",
        debug=True
    )
