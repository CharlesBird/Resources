import requests
import json

# url = 'http://47.103.32.102:4769/test/partners'
url = 'http://localhost:8069/ax/api/res.partner/eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJBWCBKV1QiLCJzdWIiOiJhZG1pbiIsInVpZCI6MiwiaWF0IjoxNTYwMzM0Mzg1LCJleHAiOjE1NjAzMzQ0NDV9.Xv4tvHq0O3O-mXJraN6JMRDS3czPWDc03hF8rp6WqSA'
headers = {'Content-Type': 'application/json', }
# data = {"jsonrpc": "2.0", "method": "test_method", "params": {"context": {'lang': 'zh_CN'}, "name": "Charles"," company":"CCCC"}, "id": 3434}
data = {"jsonrpc": "2.0", "method": "test_method", "params": {"context": {}}, "id": 123}
res = requests.get(url, data=json.dumps(data), headers=headers)
print(res.text)
#
# res = requests.delete(url)
# print(res.text)

#
# url = 'http://localhost:8069/ax/token'
#
# data = {"username": "admin", "time_limit": 60}
# res = requests.get(url, data=data)
# print(res, res.text)

