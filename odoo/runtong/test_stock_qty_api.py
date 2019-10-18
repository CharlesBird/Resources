import requests
from requests.auth import HTTPBasicAuth
import json

url = "http://172.70.0.91:8099/api/AXBarCode/InventoryOnHand?company=1000"

data = {
    "ItemId": "10001000020",
    "InventSiteId": "ST01",
    "InventLocationId": "102",
    "WMSLocationId": "WA1-1",
    "InventBatchId": "2018073391738",
    # "StartingPosition": 1,
    # "NumberOfRecordsToFetch": 100,
}


res = requests.get(url, auth=HTTPBasicAuth('shruntong\Barcode', 'B.rms123'), params=data, headers={"Content-Type": "text/plain"})
print(res.status_code)
print(res.text)
json_res = json.loads(res.text)
print(json_res)
