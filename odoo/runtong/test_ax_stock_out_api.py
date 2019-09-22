# 发货清单 同步
import requests
from requests.auth import HTTPBasicAuth
import json

url = "http://172.70.0.91:8099/api/AXBarCode/CustPackingSlipJour?company=1000"

data = {
    "SalesId": "SO-00010316",
    "Detail": [
        {
            "InventTransId": "1000-408766",
            "PostQty": 1.0
        }
    ]
}

res = requests.request('post', url, auth=HTTPBasicAuth('shruntong\Barcode', 'B.rms123'), data=json.dumps(data), headers={"Content-Type": "text/plain"})
print(res.status_code)
print(res.text)
# json_res = json.loads(res.text)
# print(json_res)