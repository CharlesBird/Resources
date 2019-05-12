from rest_framework import serializers
from rest_framework.validators import UniqueValidator
import re
from datetime import datetime, timedelta
from e_shop.settings import REGEX_MOBILE
from .models import VerifyCode
from django.contrib.auth import get_user_model
User = get_user_model()


class SmsSerializer(serializers.Serializer):
    mobile = serializers.CharField(max_length=11)

    def validate_mobile(self, mobile):
        """
        手机号码验证
        :param mobile:
        :return:
        """
        # 验证号码是否已注册
        if User.objects.filter(mobile=mobile).count():
            raise serializers.ValidationError("用户已存在")

        # 验证号码合法性
        if not re.match(REGEX_MOBILE, mobile):
            raise serializers.ValidationError("手机号码非法")

        # 设置重复发送验证码时间间隔
        one_minutes_ago = datetime.now() - timedelta(hours=0, minutes=1, seconds=0)
        if VerifyCode.objects.filter(add_time__gt=one_minutes_ago, mobile=mobile).count():
            raise serializers.ValidationError("距离上一次发送未超过60s")

        return mobile


class UserRegisterSerializer(serializers.ModelSerializer):
    code = serializers.CharField(label="验证吗", max_length=4, min_length=4, required=True, help_text="验证吗", write_only=True,
                                 error_messages={
                                     "blank": "请输入验证码",
                                     "required": "请输入验证码",
                                     "max_length": "验证码格式错误",
                                     "min_length": "验证码格式错误"
                                 })
    username = serializers.CharField(label="用户名", help_text="用户名", required=True, allow_blank=False,
                                     validators=[UniqueValidator(queryset=User.objects.all(), message="用户已存在")])
    password = serializers.CharField(label="密码", style={'input_type': 'password'}, write_only=True)

    # 使用信号量方式代替
    # def create(self, validated_data):
    #     """
    #     重载创建方法，给密码加密
    #     :param validated_data:
    #     :return:
    #     """
    #     user = super(UserRegisterSerializer, self).create(validated_data)
    #     user.set_password(validated_data["password"])
    #     user.save()
    #     return user

    def validate_code(self, code):
        """
        验证验证吗
        :param code:
        :return:
        """
        # 此方式会有两种问题，所以不用这种方式
        # 1、不存在数据
        # 2、查出多条记录
        # try:
        #     verify_records = VerifyCode.objects.get(mobile=self.initial_data["username"], code=code)
        # except VerifyCode.DoesNotExist as e:
        #     pass
        # except VerifyCode.MultipleObjectsReturned as e:
        #     pass

        verify_records = VerifyCode.objects.filter(mobile=self.initial_data["username"]).order_by("-add_time")
        if verify_records:
            last_record = verify_records[0]
            five_minutes_ago = datetime.now() - timedelta(hours=0, minutes=5, seconds=0)
            if five_minutes_ago > last_record.add_time:
                raise serializers.ValidationError("验证吗过期")

            if last_record.code != code:
                raise serializers.ValidationError("验证吗错误")
        else:
            raise serializers.ValidationError("验证吗错误")

    def validate(self, attrs):
        """
        删除code
        :param attrs: 返回所有字段的dict
        :return:
        """
        attrs['mobile'] = attrs['username']
        del attrs['code']
        return attrs

    class Meta:
        model = User
        fields = ("username", "code", "mobile", "password")