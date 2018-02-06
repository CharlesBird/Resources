from . import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, AnonymousUserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
import hashlib


class Permission(object):
    """权限常量"""
    FOLLOW = 1
    COMMENT = 2
    WRITE = 4
    MODERATE = 8
    ADMIN = 16


class Role(db.Model):
    """角色模型"""
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role', lazy='dynamic')
    default = db.Column(db.Boolean, default=False, index=True)
    permissions = db.Column(db.Integer)

    def __repr__(self):
        """角色模型名称"""
        return '<Role %r>' % self.name

    @staticmethod
    def insert_roles():
        """
        insert_roles() 函数并不直接创建新角色对象，而是通过角色名查找现有的角色，然后再进行更新。只有当数据库中没有某个角色名时才会创建新角色对象。
        """
        roles = {
            'User': (Permission.FOLLOW, Permission.COMMENT, Permission.WRITE),
            'Moderator': (Permission.FOLLOW, Permission.COMMENT, Permission.WRITE, Permission.MODERATE),
            'Administrator': (Permission.FOLLOW, Permission.COMMENT, Permission.WRITE, Permission.MODERATE, Permission.ADMIN)
        }
        default_role = 'User'
        for r in roles:
            role = Role.query.filter_by(name=r).first()
            if role is None:
                role = Role(name=r)
            role.reset_permissions()
            for perm in roles[r]:
                role.add_permission(perm)
            role.default = role.name == default_role
            db.session.add(role)
        db.session.commit()

    def reset_permissions(self):
        """重置权限"""
        self.permissions = 0

    def add_permission(self, perm):
        """
        如果权限变量已添加不用再添加
        :param perm: 权限变量
        """
        if not self.has_permission(perm):
            self.permissions += perm

    def has_permission(self, perm):
        """
        根据位运算符& 判断是否有此权限
        & 按位与运算符：参与运算的两个值,如果两个相应位都为1,则该位的结果为1,否则为0
        | 按位或运算符：只要对应的二个二进位有一个为1时，结果位就为1。
        ^ 按位异或运算符：当两对应的二进位相异时，结果为1
        :param perm: 权限变量
        """
        return self.permissions & perm == perm


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

    def __init__(self, **kwargs):
        """实例初始化"""
        super(User).__init__(**kwargs)
        # 定义默认的用户角色
        if self.role is None:
            if self.email == current_app.config['FLASKY_ADMIN']:
                self.role = Role.query.filter_by(name='Administrator').first()
            if self.role is None:
                self.role = Role.query.filter_by(default=True).first()

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

    def generate_reset_token(self, expiration=3600):
        """重设密码时根据邮箱生成唯一令牌"""
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'reset': self.id}).decode('utf-8')

    @staticmethod
    def reset_password(token, new_password):
        """确认重设密码，并赋值"""
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token.encode('utf-8'))
        except:
            return False
        user = User.query.get(data.get('reset'))
        if user is None:
            return False
        user.password = new_password
        db.session.add(user)
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

    def can(self, perm):
        """
        如果角色中包含请求的所有权限位，则返回 True ，表示允许用户执行此项操作
        :param perm: 权限变量
        :return: True|False
        """
        return self.role is not None and self.role.has_permission(perm)

    def is_administrator(self):
        """检查管理员权限的功能经常用到，因此使用单独的方法 is_administrator() 实现。"""
        return self.can(Permission.ADMIN)


class AnonymousUser(AnonymousUserMixin):
    """
    继承自 Flask-Login 中的 AnonymousUserMixin 类，并将其设为用户未登录时current_user 的值。
    这样程序不用先检查用户是否登录，就能自由调用 current_user.can() 和current_user.is_administrator() 。
    """
    def can(self, perm):
        """
        如果角色中包含请求的所有权限位，则返回 True ，表示允许用户执行此项操作
        :param perm: 权限变量
        :return: True|False
        """
        return False

    def is_administrator(self):
        """检查管理员权限的功能经常用到，因此使用单独的方法 is_administrator() 实现。"""
        return False

login_manager.anonymous_user = AnonymousUserMixin  # 注册给匿名用户


@login_manager.user_loader
def load_user(user_id):
    """
    login_user的时候会设置session["user_id"]
    使用user_loader装饰器的回调函数非常重要，他将决定 user 对象是否在登录状态
    这个id参数的值是在 login_user(user)中传入的 user 的 id 属性
    """
    return User.query.get(int(user_id))
