"""e_shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path, include
import xadmin
from django.views.static import serve
from e_shop.settings import MEDIA_ROOT
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token
from goods.views import GoodsListViewSet, CategoryViewSet
from users.views import SmsCodeViewSet, UserViewSet
from user_operation.views import UserFavViewSet, LeavingMessageViewSet, AddressViewSet
from trade.views import ShoppingCartViewSet, OrderViewSet

router = DefaultRouter()
# 商品
router.register(r'goods', GoodsListViewSet, base_name='goods')

# 商品分类
router.register(r'categorys', CategoryViewSet, base_name='categorys')

# 配置codes的url
router.register(r'code', SmsCodeViewSet, base_name='code')

# 配置用户的url
router.register(r'users', UserViewSet, base_name='users')

# 收藏
router.register(r'userfavs', UserFavViewSet, base_name='userfavs')

# 留言
router.register(r'messages', LeavingMessageViewSet, base_name='messages')

# 收货地址
router.register(r'address', AddressViewSet, base_name='address')

# 配置购物车的url
router.register(r'shopcarts', ShoppingCartViewSet, base_name="shopcarts")

# 订单的url
router.register(r'orders', OrderViewSet, base_name="orders")

urlpatterns = [
    path(r'xadmin/', xadmin.site.urls),
    path(r'api-auth/', include('rest_framework.urls')),
    path('ueditor/', include('DjangoUeditor.urls')),
    # 文件
    path(r'media/<path:path>', serve, {'document_root': MEDIA_ROOT}),

    # drf文档，title自定义
    path(r'docs/', include_docs_urls(title='电商平台')),

    path('', include(router.urls)),

    # drf自身token验证
    path(r'api-token-auth/', views.obtain_auth_token),

    # JWT验证
    path(r'login/', obtain_jwt_token)
]
