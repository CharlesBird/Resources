from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, BooleanField, SelectField, ValidationError
from wtforms.validators import DataRequired, Length, Email, Regexp
from flask_pagedown.fields import PageDownField
from ..models import User, Role


class NameForm(FlaskForm):
    name = StringField('What is your name', validators=[DataRequired()])
    submit = SubmitField('Submit')


class EditProfileForm(FlaskForm):
    """用户资料编辑表单"""
    name = StringField('真是姓名', validators=[Length(0, 64)])
    location = StringField('地址', validators=[Length(0, 64)])
    about_me = TextAreaField('关于我')
    submit = SubmitField('提交')


class EditProfileAdminForm(FlaskForm):
    """Admin用户资料编辑表单"""
    email = StringField('邮箱', validators=[DataRequired(), Length(1, 64), Email()])
    username = StringField('用户名', validators=[
        DataRequired(), Length(1, 64),
        Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0, '用户名必须是字母，数字，点，下划线，以字母开头')])
    confirmed = BooleanField('Confirmed')
    role = SelectField('权限', coerce=int)
    name = StringField('真是姓名', validators=[Length(0, 64)])
    location = StringField('地址', validators=[Length(0, 64)])
    about_me = TextAreaField('关于我')
    submit = SubmitField('提交')

    def __init__(self, user, *args, **kwargs):
        """初始化"""
        super(EditProfileAdminForm, self).__init__(*args, **kwargs)
        self.role.choices = [(role.id, role.name) for role in Role.query.order_by(Role.name).all()]  # 权限选择初始化，查询权限表所有权限
        self.user = user  # 初始化用户实例，从表单传入具体用户实例，验证邮箱用户名用到

    def validate_email(self, field):
        """
        确保是不是修改邮箱
        邮箱唯一性验证
        :param field:
        :return:
        """
        if field.data != self.user.email and User.query.filter_by(email=field.data).first():
            raise ValidationError('邮箱已经存在。')

    def validate_username(self, field):
        """
        用户名是否修改
        用户名唯一性验证
        """
        if field.data != self.user.username and User.query.filter_by(username=field.data).first():
            raise ValidationError('用户名已经存在。')


class PostForm(FlaskForm):
    """文章表单"""
    body = PageDownField('你的想法：', validators=[DataRequired()])
    submit = SubmitField('发布')