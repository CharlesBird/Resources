from . import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
import hashlib


class Role(db.Model):
    """角色模型"""

    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role')

    def __repr__(self):
        """角色模型名称"""
        return '<Role %r>' % self.name


class User(UserMixin, db.Model):
    """用户模型"""

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    confirmed = db.Column(db.Boolean, default=False)
    avatar_hash = db.Column(db.String(32))

    def __repr__(self):
        """显示模型名称"""
        return '<User %r>' % self.username

    @property
    def password(self):
        """password字段只能赋值，不能读取"""
        raise AttributeError('password is not readable attribute.')

    @password.setter
    def password(self, password):
        """密码加密赋值给password_hash"""
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        """登陆时密码加密验证"""
        return check_password_hash(self.password_hash, password)

    def generate_confirmation_token(self, expires_in=3600):
        """注册用户或者用户登陆之前确认生效令牌"""
        s = Serializer(current_app.config['SECRET_KEY'], expires_in)
        return s.dumps({'confirm': self.id}).decode('utf-8')

    def confirm(self, token):
        """用户注册登陆之前确认验证"""
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token.encode('utf-8'))
        except:
            return False
        if data.get('confirm') != self.id:
            return False
        self.confirmed = True
        db.session.add(self)
        return True

    def generate_email_change_token(self, new_email, expiration=3600):
        """修改邮箱时根据邮箱生成唯一令牌"""
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'change_email': self.id, 'new_email': new_email}).decode('utf-8')

    def change_email(self, token):
        """确认更改邮箱方法"""
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token.encode('utf-8'))
        except:
            return False
        if data.get('change_email') != self.id:
            return False
        new_email = data.get('new_email')
        if not new_email:
            return False
        if self.query.filter_by(email=new_email).first() is not None:
            return False
        self.email = new_email
        self.avatar_hash = self.gravatar_hash()
        db.session.add(self)
        return True

    def gravatar_hash(self):
        """修改邮箱时图标更改字段赋值"""
        return hashlib.md5(self.email.lower().encode('utf-8')).hexdigest()

    def gravatar(self, size=100, default='identicon', rating='g'):
        """前端界面显示用户图标"""
        url = 'https://secure.gravatar.com/avatar'
        hash = self.avatar_hash or self.gravatar_hash()
        return '{url}/{hash}?s={size}&d={default}&r={rating}'.format(
            url=url, hash=hash, size=size, default=default, rating=rating)


@login_manager.user_loader
def load_user(user_id):
    """
    login_user的时候会设置session["user_id"]
    使用user_loader装饰器的回调函数非常重要，他将决定 user 对象是否在登录状态
    这个id参数的值是在 login_user(user)中传入的 user 的 id 属性
    """
    return User.query.get(int(user_id))
