# 拣货单 同步到 AX
import requests
from requests.auth import HTTPBasicAuth
import json

url = "http://172.70.0.91:8099/api/AXBarCode/InventTransferJournal"

data = {
    "JournalId": "1000-70957",
    "InventJournalTrans": [
        {"InventTransId": "1000-006795985",
         "TotalQty": 36.0,
         "InventTrans": [
             {
                 "RecId": "5644932407",
                 "Qty": 36.0
             }
         ]}
    ]
}

res = requests.request('patch', url, auth=HTTPBasicAuth('shruntong\Barcode', 'B.rms123'), data=json.dumps(data), headers={"Content-Type": "text/plain"})
print(res.status_code)
print(res.text)
json_res = json.loads(res.text)
print(json_res)