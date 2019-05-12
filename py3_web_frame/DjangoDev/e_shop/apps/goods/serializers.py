from rest_framework import serializers
from goods.models import Goods, GoodsCategory, GoodsImage


# class Goodserializers(serializers.Serializer):
#     name = serializers.CharField(required=False, max_length=100)
#     click_num = serializers.IntegerField(default=0)
#     goods_front_image = serializers.ImageField()
#
#     def create(self, validated_data):
#         """
#         Create and return a new `Goods` instance, given the validated data.
#         """
#         return Goods.objects.create(**validated_data)

class CategorySerializers3(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = "__all__"


class CategorySerializers2(serializers.ModelSerializer):
    sub_cat = CategorySerializers3(many=True)
    class Meta:
        model = GoodsCategory
        fields = "__all__"


class CategorySerializers(serializers.ModelSerializer):
    sub_cat = CategorySerializers2(many=True)
    class Meta:
        model = GoodsCategory
        fields = "__all__"


class GoodsImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = GoodsImage
        fields = ("image",)


class GoodsSerializers(serializers.ModelSerializer):
    # 覆盖外键字段
    category = CategorySerializers()
    # images是数据库中设置的related_name="images"
    images = GoodsImageSerializer(many=True)

    class Meta:
        model = Goods
        # fields = ('name', 'click_num', 'market_price', 'goods_front_image')
        fields = "__all__"
