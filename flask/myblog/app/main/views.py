from datetime import datetime
from flask import request, make_response, redirect, render_template, session, url_for, flash, abort, current_app
from flask_login import login_required, current_user
from .forms import EditProfileForm, EditProfileAdminForm, PostForm
from . import main
from .. import db
from ..models import User, Role, Permission, Post
from ..decorators import admin_required, permission_required


@main.route('/', methods=['GET', 'POST'])
def index():
    """
    处理博客文章的首页路由
    :return:
    """
    form = PostForm()
    # 在发布新文章之前，要检查当前用户是否有写文章的权限。
    if current_user.can(Permission.WRITE) and form.validate_on_submit():
        # 注意，新文章对象的 author 属性值为表达式 current_user._get_current_object() 。
        post = Post(body=form.body.data, author=current_user._get_current_object())
        db.session.add(post)
        return redirect(url_for('.index'))
    # 按发布时间降序排列出文章。
    # 分页处理paginate()方法
    page = request.args.get('page', 1, type=int)
    pagination = Post.query.order_by(Post.timestamp.desc()).paginate(page=page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'], error_out=False)
    posts = pagination.items
    return render_template('index.html', form=form, posts=posts, pagination=pagination)


@main.route('/user/<username>')
def user(username):
    """
    用户资料页面的路由
    :param username: 用户名
    :return:
    """
    us = User.query.filter_by(username=username).first()
    if us is None:
        abort(404)
    page = request.args.get('page', 1, type=int)
    pagination = us.posts.order_by(Post.timestamp.desc()).paginate(page=page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'], error_out=False)
    posts = pagination.items
    return render_template('user.html', user=us, posts=posts, pagination=pagination)


@main.route('/edit-profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    """
    编辑用户资料路由
    :return:
    """
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.name = form.name.data
        current_user.location = form.location.data
        current_user.about_me = form.about_me.data
        db.session.add(current_user)
        db.session.commit()
        flash('用户资料已更新。')
        return redirect(url_for('.user', username=current_user.username))  # 重定向到用户资料路由，注意指定username参数值
    form.name.data = current_user.name
    form.location.data = current_user.location
    form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', form=form)


@main.route('/edit-profile/<int:user_id>', methods=['GET', 'POST'])
@login_required
@admin_required
def edit_profile_admin(user_id):
    """
    Admin编辑用户资料路由
    :return:
    """
    us = User.query.get_or_404(user_id)
    form = EditProfileAdminForm(user=us)
    if form.validate_on_submit():
        us.email = form.email.data
        us.username = form.username.data
        us.confirmed = form.confirmed.data
        us.role = Role.query.get(form.role.data)  # 根据角色id获取角色对象
        us.name = form.name.data
        us.location = form.location.data
        us.about_me = form.about_me.data
        db.session.add(us)
        db.session.commit()
        flash('用户资料已经更新。')
        return redirect(url_for('.user', username=us.username))  # 重定向到用户资料路由，注意指定username参数值
    form.email.data = us.email
    form.username.data = us.username
    form.confirmed.data = us.confirmed
    form.role.data = us.role_id
    form.name.data = us.name
    form.location.data = us.location
    form.about_me.data = us.about_me
    return render_template('edit_profile.html', form=form, user=us)


@main.route('/post/<int:id>')
def post(id):
    """
    分享文章链接
    :param id: 文章ID
    :return:
    """
    pt = Post.query.get_or_404(id)
    return render_template('post.html', posts=[pt])


@main.route('/edit-post/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_post(id):
    """
    编辑文章路由
    :param id: 文章ID
    :return:
    """
    pt = Post.query.get_or_404(id)
    # 文章的作者编辑文章，但管理员例外，管理员能编辑所 有用户的文章。
    if current_user != pt.author and not current_user.can(Permission.ADMIN):
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        pt.body = form.body.data
        db.session.add(pt)
        flash('文章已更新。')
        return redirect(url_for('.post', id=pt.id))
    form.body.data = pt.body
    return render_template('edit_post.html', form=form)


@main.route('/follow/<username>')
@login_required
@permission_required(Permission.FOLLOW)
def follow(username):
    us = User.query.filter_by(username=username).first()
    if us is None:
        flash('无效用户。')
        return redirect(url_for('.index'))
    if current_user.is_following(us):
        flash('您已经关注了此用户。')
        return redirect(url_for('.user', username=username))
    current_user.follow(us)
    db.session.commit()
    flash('您关注用户[%s]成功。' % username)
    return redirect(url_for('.user', username=username))


@main.route('/unfollow/<username>')
@login_required
@permission_required(Permission.FOLLOW)
def unfollow(username):
    us = User.query.filter_by(username=username).first()
    if us is None:
        flash('无效用户。')
        return redirect(url_for('.index'))
    if not current_user.is_following(us):
        flash('您还没关注此用户。')
        return redirect(url_for('.user', username=username))
    current_user.unfollow(us)
    db.session.commit()
    flash('您取消关注用户[%s]成功。' % username)
    return redirect(url_for('.user', username=username))


@main.route('/followers/<username>')
def followers(username):
    us = User.query.filter_by(username=username).first()
    if us is None:
        flash('无效用户。')
        return redirect(url_for('.index'))
    page = request.args.get('page', 1, type=int)
    pagination = us.followers.paginate(page, per_page=current_app.config['FLASKY_FOLLOWERS_PER_PAGE'], error_out=False)
    follows = [{'user': item.follower, 'timestamp': item.timestamp} for item in pagination.items]
    return render_template('followers.html', user=us, title="关注的人列表", endpoint='.followers',
                           pagination=pagination, follows=follows)


@main.route('/followed_by/<username>')
def followed_by(username):
    us = User.query.filter_by(username=username).first()
    if us is None:
        flash('Invalid user.')
        return redirect(url_for('.index'))
    page = request.args.get('page', 1, type=int)
    pagination = us.followed.paginate(page, per_page=current_app.config['FLASKY_FOLLOWERS_PER_PAGE'], error_out=False)
    follows = [{'user': item.followed, 'timestamp': item.timestamp} for item in pagination.items]
    return render_template('followers.html', user=us, title="被关注人列表", endpoint='.followed_by',
                           pagination=pagination, follows=follows)
