import requests
from requests.auth import HTTPBasicAuth
import json

url = 'http://172.70.0.91:8099/api/VendPackingSlipPost'

headers = [('Content-Type', 'text/plain')]

# data = {'VendPackingSlipId':'1908220019',
# 'Detail':[{'PurchId':'CPO-00339783','ItemId':'90999000945','PostQty':'1','InventTransId':'1000-005938021', 'InventBatchId':'jjjkklll'}]}

data = {'VendPackingSlipId':'20190821454',
'Detail':[{'PurchId':'CPO-00339783','ItemId':'90999000945','PostQty':'1','InventTransId':'1000-005938021', 'InventBatchId':'123323'},
{'PurchId':'CPO-00339783','ItemId':'90999001207','PostQty':'1','InventTransId':'1000-005938022', 'InventBatchId':'abv'},
{'PurchId':'CPO-00339789','ItemId':'90999000946','PostQty':'1','InventTransId':'1000-005938021', 'InventBatchId':'abn'}]}

if __name__ == '__main__':
    res = requests.post(url, auth=HTTPBasicAuth('shruntong\Barcode', 'B.rms123'), data=json.dumps(data), headers=dict(headers))
    # res = requests.post(url, auth=HTTPBasicAuth('shruntong\Barcode', 'B.rms123'), data=data, headers=dict(headers))
    print(res.request.headers)
    print(res.status_code)
    print(res.text, type(res.text))