from flask import g, jsonify
from flask_httpauth import HTTPBasicAuth
from ..models import User
from .errors import unauthorized, forbidden
from . import api


hauth = HTTPBasicAuth()


@hauth.verify_password
def verify_password(email_or_token, password):
    """验证api接口的回掉函数"""
    if email_or_token == '':
        return False
    if password == '':
        g.current_user = User.verify_hauth_token(email_or_token)
        g.token_used = True
        return g.current_user is not None
    user = User.query.filter_by(email=email_or_token).first()
    if not user:
        return False
    g.current_user = user
    g.token_used = False
    return user.verify_password(password)


@hauth.error_handler
def hauth_error():
    """无效身份错误处理"""
    return unauthorized('无效身份')


@api.before_request
@hauth.login_required
def before_request():
    """还没确认用户接口返回"""
    if not g.current_user.is_anonymous and not g.current_user.confirmed:
        return forbidden('账号还没确认。')


@api.route('/tokens/', methods=['POST', 'GET'])
def get_token():
    """获取token路由"""
    if g.current_user.is_anonymous or g.current_user.confirmed:
        return unauthorized('无效身份。')
    return jsonify({'token': g.current_user.generate_hauth_token(expiration=60*60), 'expiration': 3600})