from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from .models import UserFav
from goods.serializers import GoodsSerializer


class UserFavDetailSerializer(serializers.ModelSerializer):
    """
    用户收藏列表
    """
    goods = GoodsSerializer()

    class Meta:
        model = UserFav
        fields = ("goods", "id")


class UserFavSerializer(serializers.ModelSerializer):
    """
    收藏
    """
    # 获取当前登录的用户
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    
    class Meta:

        model = UserFav
        # validate实现唯一联合，一个商品只能收藏一次
        validators = [
            UniqueTogetherValidator(
                queryset=UserFav.objects.all(),
                fields=('user', 'goods'),
                message="已经收藏")
        ]

        fields = ("user", "goods", "id")