import requests
import json

# url = 'http://47.103.32.102:4769/test/partners'
url = 'http://localhost:8069/ax/api/sale.order/eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJBWCBKV1QiLCJzdWIiOiJhZG1pbiIsInVpZCI6MiwiaWF0IjoxNTYyNTYzMjgyLCJleHAiOjE1NjI2MDY0ODJ9.H49mj8zXRaVob5ixZsKB3-c8eHoCr_YJT_o_vI-A8No'
headers = {'Content-Type': 'application/json', }
# data = {"jsonrpc": "2.0", "method": "test_method", "params": {"context": {'lang': 'zh_CN'}, "name": "Charles"," company":"CCCC"}, "id": 3434}
data = {"jsonrpc": "2.0", "method": "create_sale_order",
        "params": {
            "context": {},
            "value": {
                "name": "SO0012",
                "task_id": "SCPC99PC190417004",
                "partner_id": "C000300670",
                "partner_number": "5464567",
                "state": "None",
                "sale_type": "Sales",
                "delivery_date": "2018-09-09",
                "delivery_addr": "dfghdfhdfgh",
                "warehouse_id": "102",
                "version": 1,
                "order_line": [
                    {"transId": "line1", "partner_no": "1", "task_id": "SCPC99PC190417004", "partner_number": "5464567",
                     "partner_id": "C000820166", "product_id": "85020000171", "company_id": "1000", "partner_depart_id": "AGENCY",
                     "qty": 100, "uom_id": "PC", "state": "None", "version": 1, "ref_type": "Sales", "ref_transId": "00000001"},
                    {"transId": "line2", "partner_no": "2", "task_id": "SCPC99PC190417004", "partner_number": "5464567",
                     "partner_id": "C000820166", "product_id": "10008000008", "company_id": "1000", "partner_depart_id": "AGENCY",
                     "qty": 200, "uom_id": "PC", "state": "None", "version": 1, "ref_type": "Sales", "ref_transId": "00000002"},
                ]
            }
        }, "id": "SO0012"}
# res = requests.put(url, data=json.dumps(data), headers=headers)
# print(res.text)
#
# res = requests.delete(url)
# print(res.text)

#
# url = 'http://localhost:8069/ax/token'
#
# data = {"username": "admin", "time_limit": 60*60*12}
# res = requests.get(url, data=data)
# print(res, res.text)

