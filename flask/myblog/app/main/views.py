from datetime import datetime
from flask import request, make_response, redirect, render_template, session, url_for, flash, abort, current_app
from flask_login import login_required, current_user
from .forms import EditProfileForm, EditProfileAdminForm, PostForm, CommentForm
from . import main
from .. import db
from ..models import User, Role, Permission, Post, Comment
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
    show_followed = False
    if current_user.is_authenticated:
        show_followed = bool(request.cookies.get('show_followed', ''))
    # 是否过滤关注者文章
    if show_followed:
        query = current_user.followed_posts
    else:
        query = Post.query
    pagination = query.order_by(Post.timestamp.desc()).paginate(page=page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'], error_out=False)
    posts = pagination.items
    return render_template('index.html', form=form, posts=posts, show_followed=show_followed, pagination=pagination)


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
        db.session.add(current_user._get_current_object())
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


@main.route('/post/<int:id>', methods=['GET', 'POST'])
def post(id):
    """
    1、分享文章链接
    2、文章评论提交路由
    :param id: 文章ID
    :return:
    """
    pt = Post.query.get_or_404(id)
    form = CommentForm()
    if form.validate_on_submit():
        comment = Comment(body=form.body.data, author=current_user._get_current_object(), post=pt)
        db.session.add(comment)
        db.session.commit()
        flash('评论成功。')
        # 把 page 设为 -1 ，这是个特殊的页数，用来请求评论的最后一页，所以刚提交的评论才会出现在页面中。
        return redirect(url_for('.post', id=pt.id, page=-1))
    page = request.args.get('page', 1, type=int)
    if page == -1:
        page = (pt.comments.count() - 1) // current_app.config['FLASKY_COMMENTS_PER_PAGE'] + 1
    pagination = pt.comments.order_by(Comment.timestamp.asc()).paginate(page=page, per_page=current_app.config['FLASKY_COMMENTS_PER_PAGE'], error_out=False)
    comments = pagination.items
    return render_template('post.html', posts=[pt], form=form, comments=comments, pagination=pagination)


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
    """
    关注路由
    :param username: 用户名
    :return:
    """
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
    """
    取消关注路由
    :param username: 用户名
    :return:
    """
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
    """
    关注他人路由
    :param username: 用户名
    :return:
    """
    us = User.query.filter_by(username=username).first()
    if us is None:
        flash('无效用户。')
        return redirect(url_for('.index'))
    page = request.args.get('page', 1, type=int)
    # 关注他人分页统计
    pagination = us.followers.paginate(page, per_page=current_app.config['FLASKY_FOLLOWERS_PER_PAGE'], error_out=False)
    # 字典类型的列表提供前端展示
    follows = [{'user': item.follower, 'timestamp': item.timestamp} for item in pagination.items]
    return render_template('followers.html', user=us, title="粉丝", endpoint='.followers',
                           pagination=pagination, follows=follows)


@main.route('/followed_by/<username>')
def followed_by(username):
    """
    被他人关注路由
    :param username: 用户名
    :return:
    """
    us = User.query.filter_by(username=username).first()
    if us is None:
        flash('Invalid user.')
        return redirect(url_for('.index'))
    page = request.args.get('page', 1, type=int)
    pagination = us.followed.paginate(page, per_page=current_app.config['FLASKY_FOLLOWERS_PER_PAGE'], error_out=False)
    follows = [{'user': item.followed, 'timestamp': item.timestamp} for item in pagination.items]
    return render_template('followers.html', user=us, title="关注", endpoint='.followed_by',
                           pagination=pagination, follows=follows)


@main.route('/all')
@login_required
def show_all():
    """
    cookie 只能在响应对象中设置，因此这两个路由不能依赖 Flask，要使用 make_response()方法创建响应对象。
    set_cookie() 函数的前两个参数分别是 cookie 名和值。
    可选的 max_age 参数设置 cookie 的过期时间，单位为秒。如果不指定参数 max_age ，浏览器关闭后 cookie 就会过期。
    """
    resp = make_response(redirect(url_for('.index')))
    resp.set_cookie('show_followed', '', max_age=7*24*60*60)
    return resp


@main.route('/followed')
@login_required
def show_followed():
    """
    cookie 只能在响应对象中设置，因此这两个路由不能依赖 Flask，要使用 make_response()方法创建响应对象。
    set_cookie() 函数的前两个参数分别是 cookie 名和值。
    可选的 max_age 参数设置 cookie 的过期时间，单位为秒。如果不指定参数 max_age ，浏览器关闭后 cookie 就会过期。
    """
    resp = make_response(redirect(url_for('.index')))
    resp.set_cookie('show_followed', '1', max_age=7*24*60*60)
    return resp


@main.route('/moderate')
@login_required
@permission_required(Permission.MODERATE)
def moderate():
    page = request.args.get('page', 1, type=int)
    pagination = Comment.query.order_by(Comment.timestamp.desc()).paginate(page, per_page=current_app.config['FLASKY_COMMENTS_PER_PAGE'], error_out=False)
    comments = pagination.items
    return render_template('moderate.html', comments=comments, pagination=pagination, page=page)


@main.route('/moderate/enable/<int:id>')
@login_required
@permission_required(Permission.MODERATE)
def moderate_enable(id):
    comment = Comment.query.get_or_404(id)
    comment.disabled = False
    db.session.add(comment)
    db.session.commit()
    return redirect(url_for('.moderate', page=request.args.get('page', 1, type=int)))


@main.route('/moderate/disable/<int:id>')
@login_required
@permission_required(Permission.MODERATE)
def moderate_disable(id):
    comment = Comment.query.get_or_404(id)
    comment.disabled = True
    db.session.add(comment)
    db.session.commit()
    return redirect(url_for('.moderate', page=request.args.get('page', 1, type=int)))
