import requests
from requests.auth import HTTPBasicAuth
import json

url = 'http://172.70.0.91:8099/api/UserInfo/user'
# res = requests.get(url, auth=HTTPBasicAuth('shruntong\Barcode', 'B.rms123'), headers={"Content-Type": "text/plain"})
# res = requests.get(url, auth=HTTPBasicAuth('shenyutest', 'Sy*0929'), headers={"Content-Type": "text/plain"})
res = requests.get(url, auth=HTTPBasicAuth('shruntong\sdfgsd', 'Sy*sds'), headers={"Content-Type": "text/plain"})
print(res.status_code)
print(res.text)