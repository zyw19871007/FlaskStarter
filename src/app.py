# -*- coding: utf8 -*-
import os
import sys
import traceback

from flask import Flask, escape, request, jsonify
from flask_admin import Admin, BaseView, expose
from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import SQLAlchemy

import src.common.util as util
from src import __version__

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)

# set optional bootswatch theme
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
app.config['SECRET_KEY'] = '123456'
admin = Admin(app, name='zyw-shadow', template_mode='bootstrap3')


# Flask-SQLAlchemy initialization here
# 配置数据库连接的对象
class Config(object):
    """配置参数"""
    # sqlalchemy的配置参数
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')

    # 设置sqlalchemy自动更跟踪数据库（数据库表手动更新是同步跟新到对象）
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # 查询时会显示原始SQL语句
    SQLALCHEMY_ECHO = True


# 加载数据库配置对象
app.config.from_object(Config)

# 创建数据库sqlalchemy工具对象
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = "user"  # 将要创建的表名
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    extend_one = db.Column(db.String(81), unique=False)
    extend_two = db.Column(db.String(80), unique=False)
    note = db.Column(db.String(255), unique=False)

    def __repr__(self):
        return '<%s %s>' % (self.name, self.email)


class UserStock(db.Model):
    __tablename__ = "user_stock"  # 将要创建的表名
    id = db.Column(db.Integer, primary_key=True)
    stock_code = db.Column(db.String(80), db.ForeignKey('stock.code'), nullable=False)
    user_name = db.Column(db.String(80), db.ForeignKey('user.name'), nullable=False)
    # user = db.relationship('User', backref=db.backref('stocks', lazy='dynamic'))
    user = db.relationship('User')
    stock = db.relationship('Stock')
    extend_one = db.Column(db.String(80), unique=False)
    extend_two = db.Column(db.String(80), unique=False)
    note = db.Column(db.String(255), unique=False)


class Stock(db.Model):
    __tablename__ = "stock"  # 将要创建的表名
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(80), unique=True, nullable=False)
    name = db.Column(db.String(80), unique=False, nullable=False)
    listing_date = db.Column(db.String(80), unique=False)  # 上市日期
    hit_new_date = db.Column(db.String(80), unique=False)  # 打新日期
    second_bord = db.Column(db.String(80), unique=False)
    extend_one = db.Column(db.String(80), unique=False)
    extend_two = db.Column(db.String(80), unique=False)
    note = db.Column(db.String(255), unique=False)

    def __repr__(self):
        return '<%s %s 上市日期%s>' % (self.code, self.name, self.listing_date)


admin.add_view(ModelView(UserStock, db.session))
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Stock, db.session))


# Add administrative views here
class MyView(BaseView):
    @expose('/')
    def index(self):
        return self.render('index.html')


admin.add_view(MyView(name='Hello'))

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
    args = util.arg_conf()
    print('version:' + __version__)
    length = len(sys.argv)
    app.run(
        host=args.bind,
        port=args.port,
        debug=args.debug
    )


if __name__ == '__main__':
    run()
