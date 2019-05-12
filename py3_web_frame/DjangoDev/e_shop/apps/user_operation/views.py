from rest_framework import viewsets, mixins
from .serializers import UserFavSerializer
from .models import UserFav


class UserFavViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    """
    用户收藏
    """
    queryset = UserFav.objects.all().order_by("id")
    serializer_class = UserFavSerializer