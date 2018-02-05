from flask import request, make_response, redirect, render_template, session, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from . import auth
from .. import db
from ..models import User
from .forms import LoginForm, RegistrationForm, ChangePasswordForm, ChangeEmailForm


@auth.before_app_request
def before_request():
    """
    before_request在请求收到之前绑定一个函数做一些事情。
    对蓝本来说，before_request 钩子只能应用到属于蓝本的请求上。若想在蓝本中使用针对程序全局请求的钩子，必须使用before_app_request 修饰器。
    """
    if current_user.is_authenticated and not current_user.confirmed and request.blueprint != 'auth' and request.endpoint != 'static':
        return redirect(url_for('auth.unconfirmed'))


@auth.route('/unconfirmed')
def unconfirmed():
    """
    未确认方法
    如果已确认current_user.confirmed跳转到主页
    """
    if current_user.is_anonymous or current_user.confirmed:
        return url_for(url_for('main.index'))
    return render_template('auth/unconfirmed.html', user=current_user)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    """
    登陆请求
    :return:
    """
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('无效用户或者密码')
    return render_template('auth/login.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    """
    登出请求
    @login_required 必须是在已登陆状态下
    :return:
    """
    logout_user()
    flash('注销成功！')
    return redirect(url_for('main.index'))


@auth.route('/register', methods=['GET', 'POST'])
def register():
    """
    注册请求
    :return:
    """
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data, username=form.username.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        token = user.generate_confirmation_token()
        # 此处省去发送邮件功能
        flash('A confirmation email has been sent to you by email. %s' % token)
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)


@auth.route('/confirm/<token>')
@login_required
def confirm(token):
    """
    确认登陆令牌验证
    :param token: 令牌
    :return:
    """
    if current_user.confirmed:
        return redirect(url_for('main.index'))
    if current_user.confirm(token):
        flash('您已经确认账号。 谢谢！')
    else:
        flash('确认链接无效或者已过期！！！')
    return redirect(url_for('main.index'))


@auth.route('/confirm')
@login_required
def resend_confirmation():
    """
    重新发送登陆认证
    :return:
    """
    token = current_user.generate_confirmation_token()
    # 此处省去重发送邮件功能
    flash('A new confirmation email has been sent to you by email.%s' % token)
    # 模拟确认邮件，能够登录账号
    return render_template('auth/email/confirm.html', user=current_user, token=token)
    # return redirect(url_for('main.index'))


@auth.route('/change_password', methods=['GET', 'POST'])
@login_required
def change_password():
    """
    修改密码请求
    必须在登陆状态下
    :return:
    """
    form = ChangePasswordForm()
    if form.validate_on_submit():
        # 验证老密码是否正确
        if current_user.verify_password(form.old_password.data):
            current_user.password = form.password.data
            db.session.add(current_user)
            db.session.commit()
            flash('密码已更改！')
            return redirect(url_for('main.index'))
        else:
            flash('无效密码！')
    return render_template('auth/change_password.html', form=form)


@auth.route('/change_email', methods=['GET', 'POST'])
@login_required
def change_email_request():
    """
    修改邮箱请求
    必须在登陆状态下
    :return:
    """
    form = ChangeEmailForm()
    if form.validate_on_submit():
        # 验证老密码是否正确
        if current_user.verify_password(form.password.data):
            new_email = form.email.data
            # 验证邮箱获取token令牌
            token = current_user.generate_email_change_token(new_email)
            # 此处省去发送邮件确认功能
            # ...

            flash('一封邮件已经发送给您的邮箱！')
            # 模拟邮件确认界面
            return render_template('auth/email/change_email.html', user=current_user, token=token)
            # return redirect(url_for('auth.change_email/%s' % token))
            # return redirect(url_for('main.index'))
        else:
            flash('无效邮件或者密码！')
    return render_template('auth/change_email.html', form=form)


@auth.route('/change_email/<token>')
@login_required
def change_email(token):
    """
    确认更改邮箱请求
    :param token: 令牌
    :return:
    """
    if current_user.change_email(token):
        db.session.commit()
        flash('邮箱已更新')
    else:
        flash('无效访问')
    return redirect(url_for('main.index'))