from functools import wraps

from flask import Blueprint, render_template, redirect, url_for, flash, abort, request, session

# from app import login_required
from forms import ProductEditForm
from models import Product, db

mall = Blueprint('mall', __name__, template_folder='templates', static_folder='static')


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


@mall.route('/product/list/<int:page>')
# @login_required
def product_list(page):
    """ 商品列表 """
    # flash('成功', 'success')
    # flash('警告', 'warning')
    # flash('提示', 'info')
    # flash('错误', 'danger')

    page_size = 5
    # 搜索条件的查询
    name = request.args.get('name', '')
    print('name--- ', name)
    if name:
        page_data = Product.query.filter(Product.name.contains(name), Product.is_valid==True).paginate(page=page, per_page=page_size)
    else:
        page_data = Product.query.filter(Product.is_valid==True).paginate(page=page, per_page=page_size)
    return render_template('product_list.html', page_data=page_data)


@mall.route('/product/detail/<uid>')
def product_detail(uid):
    """ 商品详情页 """
    prod_obj = Product.query.filter_by(uid=uid).first_or_404()
    print(prod_obj)
    return render_template('product_detail.html', prod_obj=prod_obj)


@mall.route('/product/add', methods=['GET', 'POST'])
def product_add():
    """ 商品添加 """
    form = ProductEditForm()
    if form.validate_on_submit():
        # 保存到数据库
        print(form.data)
        prod_obj = Product(
            name=form.data['name'],
            content=form.data['content'],
            desc=form.data['desc'],
            types=form.data['types'],
            price=form.data['price'],
            origin_price=form.data['origin_price'],
            img='xxx.jpg',
            channel=form.data['channel'],
            buy_link=form.data['buy_link'],
            status=form.data['status'],
            sku_count=form.data['sku_count'],
            remain_count=form.data['remain_count'],
            view_count=form.data['view_count'],
            score=form.data['score'],
            is_valid=form.data['is_valid'],
            reorder=form.data['reorder'],
        )
        db.session.add(prod_obj)
        db.session.commit()
        # 消息提示
        flash('新增商品成功', 'success')
        # 跳转到商品列表中去
        return redirect(url_for('mall.product_list', page=1))
    else:
        # 消息提示
        flash('请修改页面中的页面错误，然后提交', 'warning')
        print(form.errors)
    return render_template('product_add.html', form=form)


@mall.route('/product/edit/<uid>', methods=['GET', 'POST'])
def product_edit(uid):
    """ 商品编辑 """
    # 查询商品信息
    prod_obj = Product.query.filter_by(uid=uid, is_valid=True).first()
    print(prod_obj)
    if prod_obj is None:
        abort(404)
    form = ProductEditForm(obj=prod_obj)
    if form.validate_on_submit():
        prod_obj.name = form.name.data
        prod_obj.content = form.data['content']
        prod_obj.desc = form.data['desc']
        prod_obj.types = form.data['types']
        prod_obj.price = form.data['price']
        prod_obj.origin_price = form.data['origin_price']
        prod_obj.img = 'xxx.jpg'
        prod_obj.channel = form.data['channel']
        prod_obj.buy_link = form.data['buy_link']
        prod_obj.status = form.data['status']
        prod_obj.sku_count = form.data['sku_count']
        prod_obj.remain_count = form.data['remain_count']
        prod_obj.view_count = form.data['view_count']
        prod_obj.score = form.data['score']
        prod_obj.is_valid = form.data['is_valid']
        prod_obj.reorder = form.data['reorder']
        db.session.add(prod_obj)
        db.session.commit()
        flash('修改成功', 'success')
        return redirect(url_for('mall.product_list', page=1))
    else:
        print(form.errors)
    return render_template('product_edit.html', form=form, prod_obj=prod_obj)


@mall.route('/product/delete/<uid>', methods=['GET', 'POST'])
def product_delete(uid):
    """ 商品的删除 """
    prod_obj = Product.query.filter_by(uid=uid, is_valid=True).first()
    if prod_obj is None:
        return 'No'
    prod_obj.is_valid = False
    db.session.add(prod_obj)
    db.session.commit()
    return 'DELETED!'