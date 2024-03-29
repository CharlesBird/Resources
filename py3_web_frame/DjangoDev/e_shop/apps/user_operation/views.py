from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication
from utils.permissions import IsOwnerOrReadOnly
from .serializers import UserFavSerializer, UserFavDetailSerializer, LeavingMessageSerializer, AddressSerializer
from .models import UserFav, UserLeavingMessage, UserAddress


class UserFavViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    """
    用户收藏
    """
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    serializer_class = UserFavSerializer
    lookup_field = "goods_id"

    def get_queryset(self):
        # 只能查看当前登录用户的收藏，不会获取所有用户的收藏
        return UserFav.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action == 'list':
            return UserFavDetailSerializer
        elif self.action == 'create':
            return UserFavSerializer
        return UserFavSerializer


class LeavingMessageViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    """
    list:
        获取用户留言
    create:
        添加留言
    delete:
        删除留言
    """
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    serializer_class = LeavingMessageSerializer

    def get_queryset(self):
        # 只能看到自己的留言
        return UserLeavingMessage.objects.filter(user=self.request.user)


class AddressViewSet(viewsets.ModelViewSet):
    """
    ModelViewSet继承了mixins所有动作
    收货地址管理
    list:
        获取收货地址
    create:
        添加收货地址
    update:
        更新收货地址
    delete:
        删除收货地址
    """
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    serializer_class = AddressSerializer

    def get_queryset(self):
        # 只能看到自己的地址
        return UserAddress.objects.filter(user=self.request.user)

