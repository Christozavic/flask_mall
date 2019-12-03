from flask import Blueprint, render_template, url_for, flash, session, redirect, g

from forms import LoginForm
from models import User

accounts = Blueprint('accounts', __name__, template_folder='templates', static_folder='static')


@accounts.route('/login', methods=['GET', 'POST'])
def login():
    """ 用户登录 """
    form = LoginForm()
    if form.validate_on_submit():
        # 用户名，密码
        username = form.username.data
        password = form.password.data
        # 查找用户
        user = User.query.filter_by(username=username, password=password).first()
        if user is None:
            flash('用户名或密码错误', 'danger')
        else:
            session['userid'] = user.id
            flash('欢迎回来！', 'success')
            return redirect(url_for('index'))
    return render_template('login.html', form=form)


@accounts.route('/logout')
def logout():
    """ 退出登录 """
    session['user_id'] = None
    g.user = None
    flash('已退出登陆', 'success')
    return redirect(url_for('accounts.login'))
