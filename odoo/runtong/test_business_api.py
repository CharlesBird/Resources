import requests
from requests.auth import HTTPBasicAuth

url = "http://172.70.0.91:8099/api/Query/RMS_Department_BC"

data = {
    "startingPosition": 1,
    "numberOfRecordsToFetch": 200
}

res = requests.get(url, auth=HTTPBasicAuth('shruntong\Barcode', 'B.rms123'), params=data, headers={"Content-Type": "text/plain"})
print(res.status_code)
print(res.text)

url = 'http://172.70.0.91:8099/api/DataSync/RMS_InventBatch_BC'

data = {'conditions':
            '{"Conditions": [{"DataSourceName": "InventBatch", "FieldName": "RecId", "Operator": "Equal", "Value": "5639694605,5639694606,5639694607,5639694576,5639694577,5639694578,5639694579,5639694580"}]}'
        }

res = requests.get(url, auth=HTTPBasicAuth('shruntong\Barcode', 'B.rms123'), params=data, headers={"Content-Type": "text/plain"})