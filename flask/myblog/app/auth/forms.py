from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, ValidationError
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from ..models import User


class LoginForm(FlaskForm):
    """登录界面表单字段对象"""
    email = StringField('邮箱', validators=[DataRequired(), Length(1, 64), Email()])
    password = PasswordField('密码', validators=[DataRequired()])
    remember_me = BooleanField('记住我')
    submit = SubmitField('登录')


class RegistrationForm(FlaskForm):
    """注册界面表单字段对象"""
    email = StringField('邮箱', validators=[DataRequired(), Length(1, 64), Email()])
    username = StringField('用户名', validators=[
        DataRequired(), Length(1, 64),
        Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0, '用户名必须是字母，数字，点，下划线，以字母开头')])
    password = PasswordField('密码', validators=[DataRequired(), EqualTo('password2', message='确认密码要一致')])
    password2 = PasswordField('确认密码', validators=[DataRequired()])
    submit = SubmitField('注册')

    def validate_email(self, field):
        """邮箱唯一性验证"""
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')

    def validate_username(self, field):
        """用户名唯一性验证"""
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already registered.')


class ChangePasswordForm(FlaskForm):
    """修改密码界面表单字段对象"""
    old_password = PasswordField('旧密码', validators=[DataRequired()])
    password = PasswordField('新密码', validators=[DataRequired(), EqualTo('password2', message='确认密码要一致')])
    password2 = PasswordField('确认密码', validators=[DataRequired()])
    submit = SubmitField('修改密码')


class ChangeEmailForm(FlaskForm):
    """修改邮箱表单字段对象"""
    email = StringField('新邮箱', validators=[DataRequired(), Length(1, 64), Email()])
    password = PasswordField('密码', validators=[DataRequired()])
    submit = SubmitField('修改邮箱')

    def validate_email(self, field):
        """邮箱验证唯一性验证"""
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('邮箱已存在！')


class ResetPasswordRequestForm(FlaskForm):
    """重设密码表单字段对象"""
    email = StringField('邮箱', validators=[DataRequired(), Length(1, 64), Email()])
    submit = SubmitField('重设密码')


class ResetPasswordForm(FlaskForm):
    """确认重设密码表单字段对象"""
    password = PasswordField('密码', validators=[DataRequired(), EqualTo('password2', message='确认密码要一致')])
    password2 = PasswordField('确认密码', validators=[DataRequired()])
    submit = SubmitField('重设密码')