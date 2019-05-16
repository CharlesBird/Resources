import time
from rest_framework import serializers
from goods.models import Goods
from goods.serializers import GoodsSerializer
from .models import ShoppingCart, OrderInfo, OrderGoods


class ShopCartDetailSerializer(serializers.ModelSerializer):
    """
    购物车详情
    """
    # 一个购物车对应一个商品
    goods = GoodsSerializer(many=False, read_only=True)

    class Meta:
        model = ShoppingCart
        fields = ("goods", "nums")


class ShopCartSerializer(serializers.Serializer):
    """
    添加购物车
    """
    # 获取当前登录的用户
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    nums = serializers.IntegerField(required=True, label="数量", min_value=1,
                                    error_messages={
                                        "min_value": "商品数量不能小于一",
                                        "required": "请选择购买数量"
                                    })
    # 这里是继承Serializer，必须指定queryset对象，如果继承ModelSerializer则不需要指定
    # goods是一个外键，可以通过这方法获取goods object中所有的值
    goods = serializers.PrimaryKeyRelatedField(required=True, queryset=Goods.objects.all())

    # 继承的Serializer没有save功能，必须写一个create方法
    def create(self, validated_data):
        # validated_data是已经处理过的数据
        # 获取当前用户
        user = self.context["request"].user
        nums = validated_data["nums"]
        goods = validated_data["goods"]

        existed = ShoppingCart.objects.filter(user=user, goods=goods)
        if existed:
            existed = existed[0]
            existed.nums += nums
            existed.save()
        else:
            existed = ShoppingCart.objects.create(**validated_data)

        return existed

    def update(self, instance, validated_data):
        instance.nums = validated_data["nums"]
        instance.save()
        return instance


class OrderGoodsSerializer(serializers.ModelSerializer):
    goods = GoodsSerializer(many=True)

    class Meta:
        model = OrderGoods
        fields = "__all__"


class OrderDetailSerializer(serializers.ModelSerializer):
    goods = OrderGoodsSerializer(many=True)

    class Meta:
        model = OrderInfo
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    def generate_order_sn(self):
        # 生成订单号
        # 当前时间+userid+随机数
        from random import Random
        random_ins = Random()
        order_sn = "{time_str}{userid}{ranstr}".format(time_str=time.strftime("%Y%m%d%H%M%S"),
                                                       userid=self.context["request"].user.id,
                                                       ranstr=random_ins.randint(10, 99))
        return order_sn

    def validate(self, attrs):
        # validate中添加order_sn，然后在view中就可以save
        attrs["order_sn"] = self.generate_order_sn()
        return attrs

    class Meta:
        model = OrderInfo
        fields = "__all__"