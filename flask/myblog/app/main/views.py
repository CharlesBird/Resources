from datetime import datetime
from flask import request, make_response, redirect, render_template, session, url_for, flash, abort
from flask_login import login_required, current_user
from .forms import NameForm, EditProfileForm, EditProfileAdminForm
from . import main
from .. import db
from ..models import User, Role
from ..decorators import admin_required, permission_required


@main.route('/', methods=['GET', 'POST'])
def index():
    """
    主页路由
    :return:
    """
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed name')
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            session['known'] = False
        else:
            session['known'] = True
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('.index'))
    return render_template('index.html', form=form, current_date=datetime.utcnow(), name=session.get('name', ''), known=session.get('known', False))


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
    return render_template('user.html', user=us)


@main.route('/edit-profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    """
    编辑资料路由
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
        return redirect(url_for('.user'), username=current_user.username)
    form.name.data = current_user.name
    form.location.data = current_user.location
    form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', form=form)


@main.route('/edit-profile/<int:user_id>', methods=['GET', 'POST'])
@login_required
@admin_required
def edit_profile_admin(user_id):
    us = User.query.get_or_404(user_id)
    form = EditProfileAdminForm(user=us)
    if form.validate_on_submit():
        us.email = form.email.data
        us.username = form.username.data
        us.confirmed = form.confirmed.data
        us.role = Role.query.get(form.role.data)
        us.name = form.name.data
        us.location = form.location.data
        us.about_me = form.about_me.data
        db.session.add(us)
        db.session.commit()
        flash('用户资料已经更新。')
        return redirect(url_for('.user', username=us.username))
    form.email.data = us.email
    form.username.data = us.username
    form.confirmed.data = us.confirmed
    form.role.data = us.role_id
    form.name.data = us.name
    form.location.data = us.location
    form.about_me.data = us.about_me
    return render_template('edit_profile.html', form=form, user=us)
