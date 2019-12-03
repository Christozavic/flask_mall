import uuid
from functools import wraps

from flask import Flask, render_template, flash, redirect, url_for, request, abort, session, g
from flask_sqlalchemy import SQLAlchemy

import constants
from forms import ProductEditForm, LoginForm
from models import db, User

# 引入蓝图
from accounts.view import accounts
from mall.view import mall

app = Flask(__name__)
app.config.from_object('conf.Config')
# 使用 ORM
db.init_app(app)
# 注册蓝图
app.register_blueprint(accounts, url_prefix='/accounts')
app.register_blueprint(mall, url_prefix='/mall')


def login_required(view_func):
    """ 登录验证 """

    @wraps(view_func)
    def wrapper(*args, **kwargs):
        user_id = session.get('user_id', None)
        if not user_id:
            flash('请登录', 'danger')
            return redirect(url_for('accounts.login'))
        return view_func(*args, **kwargs)

    return wrapper


@app.route('/')
def index():
    """ 首页 """
    return render_template('index.html')


@app.before_request
def before_request():
    """ 如果有用户的话，设置到全局对象g """
    user_id = session.get('user_id', None)
    if user_id:
        user = User.query.get(user_id)
        print(user)
        g.user = user


print(app.url_map)


if __name__ == '__main__':
    app.run()
