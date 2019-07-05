import requests
import json

# url = 'http://47.103.32.102:4769/test/partners'
url = 'http://localhost:8069/ax/api/sale.order/eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJBWCBKV1QiLCJzdWIiOiJhZG1pbiIsInVpZCI6MiwiaWF0IjoxNTYyMzA1MjUyLCJleHAiOjE1NjIzNDg0NTJ9.3YH7in9Va5ApXP_unVVHicPrmidXRmnTzwzGDR4-7wA'
headers = {'Content-Type': 'application/json', }
# data = {"jsonrpc": "2.0", "method": "test_method", "params": {"context": {'lang': 'zh_CN'}, "name": "Charles"," company":"CCCC"}, "id": 3434}
data = {"jsonrpc": "2.0", "method": "test_method",
        "params": {
            "context": {},
            "value": {
                "name": "SO0012",
                "task_id": "SCPC99PC190417004",
                "partner_number": "5464567",
                "state": "None",
                "delivery_date": "",
                "delivery_addr": "dfghdfhdfgh",
                "warehouse_id": "102",
                "version": 1,
                "order_line": [
                    {"transId": "line1", "task_id": "SCPC99PC190417004", "partner_number": "5464567", "partner_id": "C000820166", "product_id": "85020000171", "company_id": "1000", "partner_depart_id": "PC04", "qty": 100, "uom_id": "PC", "version": 1},
                    {"transId": "line2", "task_id": "SCPC99PC190417004", "partner_number": "5464567", "partner_id": "C000820166", "product_id": "10008000008", "company_id": "1000", "partner_depart_id": "PC04", "qty": 200, "uom_id": "PC", "version": 1},
                ]
            }
        }, "id": "sdfgsdfg"}
res = requests.put(url, data=json.dumps(data), headers=headers)
print(res.text)
#
# res = requests.delete(url)
# print(res.text)

#
# url = 'http://localhost:8069/ax/token'
#
# data = {"username": "admin", "time_limit": 60*60*12}
# res = requests.get(url, data=data)
# print(res, res.text)

