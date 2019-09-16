# 任务号 获取AX 中 日记帐号
import requests
from requests.auth import HTTPBasicAuth
import json

url = "http://172.70.0.91:8099/api/Query/RMS_StockCheckJournalId"

conditions = {
        "Conditions": [
            {
                "DataSourceName": "InventJournalTable",
                "FieldName": "VYA_SalesTaskNumber",
                "Operator": "Equal",
                "Value": "SCPC04PC190213058"
            }
        ]
    }

data = {
    "startingPosition": 1,
    "numberOfRecordsToFetch": 100,
    "conditions": json.dumps(conditions)
}


res = requests.get(url, auth=HTTPBasicAuth('shruntong\Barcode', 'B.rms123'), params=data, headers={"Content-Type": "text/plain"})
print(res.status_code)
print(res.text)
json_res = json.loads(res.text)
print(json_res)
# print(len(json_res['RMS_QueryService']['WMSLocation']))