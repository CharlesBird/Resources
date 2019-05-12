from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, mixins, generics, viewsets
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.authentication import TokenAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from .filters import GoodsFilter
from .serializers import GoodsSerializers, CategorySerializers
from .models import Goods, GoodsCategory


# class GoodstList(APIView):
#     """
#     List all goods.
#     """
#     def get(self, request, format=None):
#         goods = Goods.objects.all()
#         serializer = Goodsserializers(goods, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = Goodsserializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GoodsPagination(PageNumberPagination):
    page_size = 12
    page_size_query_param = 'page_size'
    page_query_param = 'page'
    max_page_size = 100


# class GoodsListView(generics.ListAPIView):
#     """
#     商品列表页
#     """
#     queryset = Goods.objects.all()
#     serializer_class = GoodsSerializers
#     pagination_class = GoodsPagination

class GoodsListViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    商品列表页，分页，过滤，搜索，排序
    """
    queryset = Goods.objects.all().order_by('id')
    serializer_class = GoodsSerializers
    pagination_class = GoodsPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    # filterset_fields = ('name', 'shop_price')
    # authentication_classes = (TokenAuthentication,)  # 可以单独给view增加验证方式
    filter_class = GoodsFilter
    search_fields = ('name', 'goods_desc', 'goods_brief')
    ordering_fields = ('shop_price', 'sold_num')

    # def get_queryset(self):
    #     queryset = Goods.objects.all().order_by('id')
    #     price_min = self.request.query_params.get('price_min', 0)
    #     if price_min:
    #         queryset = Goods.objects.filter(shop_price__gt=int(price_min)).order_by('id')
    #     return queryset


class CategoryViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    list:
        商品分类列表数据
    """
    queryset = GoodsCategory.objects.filter(category_type=1).order_by('id')
    serializer_class = CategorySerializers