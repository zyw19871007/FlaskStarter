from flask import Flask, escape, request
import sys

app = Flask(__name__)


@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'


@app.route('/getQCQty')
def getQCQty():
    name = request.args.get("name", "World")
    # todo 调用算法

    return f'Hello, {escape(name)}!'


def run():
    print(len(sys.argv))
    if len(sys.argv) == 3:
        arg1, arg2 = sys.argv[1], sys.argv[2]
        print(arg1,arg2)
        app.run(
            host=arg1,
            port=arg2
        )
    else:
        app.run()


if __name__ == '__main__':
    app.run()
