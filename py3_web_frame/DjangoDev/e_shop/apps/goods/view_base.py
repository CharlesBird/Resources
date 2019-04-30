from django.views.generic import View
from goods.models import Goods
from django.http import JsonResponse, HttpResponse
import json


class GoodsListView(View):
    def get(self, request):
        json_list = []
        goods = Goods.objects.all()
        for good in goods:
            json_dict = {}
            json_dict['name'] = good.name
            json_dict['category'] = good.category.name
            json_dict['market_price'] = good.market_price
            # json_dict['add_time'] = good.add_time  # 时间类型不能序列化
            json_list.append(json_dict)

        json_data = json.dumps(json_list)
        return HttpResponse(json_data, content_type='application/json')  # 注意必须添加 content_type='application/json'