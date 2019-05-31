import requests
import json

url = 'http://47.103.32.102:4769/test/partners'
headers = {'Content-Type': 'application/json', }
# data = {"jsonrpc": "2.0", "method": "test_method", "params": {"context":{}, "name":"Charles","company":"CCCC"}, "id": 123}
data = {"jsonrpc": "2.0", "method": "test_method", "params": {"context": {}}, "id": 123}
res = requests.post(url, data=json.dumps(data), headers=headers)
print(res.text)