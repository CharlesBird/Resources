# 缺货检查
import requests
from requests.auth import HTTPBasicAuth
import json

url = "http://172.70.0.91:8099/api/AXBarCode/InventTransferJournal/1000-32461/stockCheck"

data = {}

res = requests.post(url, auth=HTTPBasicAuth('shruntong\Barcode', 'B.rms123'), data=json.dumps(data), headers={"Content-Type": "text/plain"})
print(res.status_code)
print(res.text)
print(json.loads(res.text))