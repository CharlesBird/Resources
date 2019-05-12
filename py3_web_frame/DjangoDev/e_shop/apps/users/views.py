from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from rest_framework import mixins, viewsets, status
from rest_framework.response import Response
from rest_framework_jwt.serializers import jwt_payload_handler, jwt_encode_handler
from random import choice
from .serializers import SmsSerializer, UserRegisterSerializer
from e_shop.settings import APIKEY
from utils.yunpian import YunPian
from .models import VerifyCode
from django.contrib.auth import get_user_model
User = get_user_model()


class CustomBackend(ModelBackend):
    """
    自定义用户验证
    """
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(username=username) | Q(mobile=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class SmsCodeViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    发送短信验证
    """
    serializer_class = SmsSerializer

    def generate_code(self):
        """
        生成四位数字的验证码
        """
        seeds = "1234567890"
        random_str = []
        for i in range(4):
            random_str.append(choice(seeds))

        return "".join(random_str)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        # 调用所有验证方法
        serializer.is_valid(raise_exception=True)  # raise_exception=True作用 出现异常就返回400错误返回给Response

        mobile = serializer.validated_data['mobile']

        code = self.generate_code()

        yun_pian = YunPian(APIKEY)
        sms_status = yun_pian.send_sms(code=code, mobile=mobile)

        if sms_status["code"] != 0:
            return Response({
                'mobile': sms_status['msg']
            }, status=status.HTTP_400_BAD_REQUEST)
        else:
            code_record = VerifyCode(code=code, mobile=mobile)
            code_record.save()
            return Response({
                'mobile': mobile
            }, status=status.HTTP_201_CREATED)


class UserViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    用户注册
    """
    serializer_class = UserRegisterSerializer
    queryset = User.objects.all().order_by("id")

    # 用户注册后系统自动登录，token返回给前端的解决方式
    def create(self, request, *args, **kwargs):
        """
        重载mixin的创建方法，生成token返回前端
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = self.perform_create(serializer)
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        res_dict = serializer.data
        res_dict['token'] = token
        res_dict['name'] = user.name if user.name else user.username

        headers = self.get_success_headers(serializer.data)
        return Response(res_dict, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        """
        重载，返回用户
        :param serializer:
        :return:
        """
        return serializer.save()

