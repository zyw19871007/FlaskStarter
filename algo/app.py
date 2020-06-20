# -*- coding: utf8 -*-
import json
import sys
import traceback

from flask import Flask, escape, request, jsonify, Response

from algo import __version__

app = Flask(__name__)

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
    if length == 3:
        arg1, arg2 = sys.argv[1], sys.argv[2]
        print(arg1, arg2)
        app.run(
            host=arg1,
            port=arg2
        )
    elif length == 4:
        arg1, arg2, arg3 = sys.argv[1], sys.argv[2], sys.argv[3]
        print(arg1, arg2, arg3)
        app.run(
            host=arg1,
            port=arg2,
            debug=True
        )
    else:
        app.run(
            host=your_rest_server_ip,
            port=your_rest_server_port,
            # debug=True
        )


if __name__ == '__main__':
    app.run(
        host=your_rest_server_ip,
        port="12322",
        debug=True
    )
