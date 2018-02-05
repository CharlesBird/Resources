from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, ValidationError
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from ..models import User


class LoginForm(FlaskForm):
    """登录界面表单字段对象"""
    email = StringField('Email', validators=[DataRequired(), Length(1, 64), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log In')


class RegistrationForm(FlaskForm):
    """注册界面表单字段对象"""
    email = StringField('Email', validators=[DataRequired(), Length(1, 64), Email()])
    username = StringField('Username', validators=[
        DataRequired(), Length(1, 64),
        Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0, 'Usernames must have only letters, numbers, dots or underscores')])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('password2', message='Passwords must match.')])
    password2 = PasswordField('Comfirm Password', validators=[DataRequired()])
    submit = SubmitField('Register')

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
    old_password = PasswordField('Password', validators=[DataRequired()])
    password = PasswordField('New Password', validators=[DataRequired(), EqualTo('password2', message='Passwords must match.')])
    password2 = PasswordField('Comfirm New Password', validators=[DataRequired()])
    submit = SubmitField('Update password')


class ChangeEmailForm(FlaskForm):
    """修改邮箱表单字段对象"""
    email = StringField('New Email', validators=[DataRequired(), Length(1, 64), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Update Email Address')

    def validate_email(self, field):
        """邮箱验证唯一性验证"""
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('邮箱已存在！')