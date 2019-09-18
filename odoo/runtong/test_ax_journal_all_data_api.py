# 日记帐号 获取具体日记账中的信息
import requests
from requests.auth import HTTPBasicAuth
import json

url = "http://172.70.0.91:8099/api/AXBarCode/InventTransferJournal/1000-32467"

data = {"startingPosition": 1, "numberOfRecordsToFetch": 100}

res = requests.get(url, auth=HTTPBasicAuth('shruntong\Barcode', 'B.rms123'), data=data, headers={"Content-Type": "text/plain"})
print(res.status_code)
print(res.text)
json_res = json.loads(res.text)
print(json_res)