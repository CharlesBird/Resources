import requests
from requests.auth import HTTPBasicAuth
import json

url = "http://172.70.0.86:8092/api/AXBarCode/InventoryOnHand?company=1000"

data = {
    "ItemId": "P6024000038",
    "InventSiteId": "",
    "InventLocationId": "",
    "WMSLocationId": "",
    "InventBatchId": "",
    # "StartingPosition": 1,
    # "NumberOfRecordsToFetch": 100,
}


res = requests.get(url, auth=HTTPBasicAuth('shruntong\Barcode', 'B.rms123'), params=data, headers={"Content-Type": "text/plain"})
print(res.status_code)
print(res.text)
json_res = json.loads(res.text)
print(json_res)
