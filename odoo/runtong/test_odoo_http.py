import requests
import json

headers = {'Content-Type': 'application/json', }

# url = 'http://localhost:8069/ax/api/sale.order/eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJBWCBKV1QiLCJzdWIiOiJhZG1pbiIsInVpZCI6MiwiaWF0IjoxNTY4MDA5OTYxLCJleHAiOjE1NjgwNTMxNjF9.cUg8VatZX1v2W_icbwAmUl40Rszvfp1uZeK9nkILFbY'
#
# data = {"jsonrpc": "2.0", "method": "create_sale_order",
#         "params": {
#             "context": {},
#             "value": {
#                 "name": "SOTEST201909090002",
#                 "task_id": "SCPC99PC190417004",
#                 "partner_id": "C000820166",
#                 "partner_number": "cus20190001",
#                 "state": "None",
#                 "sale_type": "Sales",
#                 "delivery_date": "2019-09-09",
#                 "delivery_addr": "test",
#                 "warehouse_id": "102",
#                 "version": 1,
#                 "order_line": [
#                     {"transId": "soline0909-0031", "partner_no": 10000, "task_id": "SCPC99PC190417004", "partner_number": "cus20190001",
#                      "partner_id": "C000820166", "product_id": "10004000005", "company_id": "1000", "partner_depart_id": "AGENCY",
#                      "qty": 300, "uom_id": "PC", "state": "None", "version": 1, "ref_type": "Sales", "ref_transId": "00000001", "ax_key": "soline0909-0031"},
#                     {"transId": "soline0909-0032", "partner_no": 20000, "task_id": "SCPC99PC190417004", "partner_number": "cus20190001",
#                      "partner_id": "C000820166", "product_id": "10004000006", "company_id": "1000", "partner_depart_id": "AGENCY",
#                      "qty": 300, "uom_id": "PC", "state": "None", "version": 1, "ref_type": "Sales", "ref_transId": "00000002", "ax_key": "soline0909-0031"},
#                 ],
#                 "ax_key": "SOTEST201909090002"
#             }
#         }, "id": 'SOTEST201909090002'}
# res = requests.put(url, data=json.dumps(data), headers=headers)
# print(res.text)

# data = {"jsonrpc": "2.0", "method": "delete_sale_order", "id": None}
# url = 'http://localhost:8069/ax/api/sale.order/SO0012/eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJBWCBKV1QiLCJzdWIiOiJhZG1pbiIsInVpZCI6MiwiaWF0IjoxNTYzODQzMjE2LCJleHAiOjE1NjM4ODY0MTZ9.VahT89A_1JhG85ygTGS0cU2bSwAvn-Cxcmn7mJsns94'
# res = requests.delete(url, data=json.dumps(data), headers=headers)
# print(res.text)

# url = 'http://localhost:8069/ax/api/sale.order/SO0012/eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJBWCBKV1QiLCJzdWIiOiJhZG1pbiIsInVpZCI6MiwiaWF0IjoxNTY2MjA2MzAyLCJleHAiOjE1NjYyNDk1MDJ9.rweDWps9p_ZXisnHrcbJOAuEl9NhABrD6ggZb0X0JZw'
#
# data = {"jsonrpc": "2.0", "method": "update_sale_order",
#         "params": {
#             "context": {},
#             "value": {
#                 "name": "SO0012",
#                 "task_id": "SCPC99PC190417004",
#                 "partner_id": "C000300670",
#                 "partner_number": "12345678",
#                 "state": "None",
#                 "sale_type": "Sales",
#                 "delivery_date": "2019-07-23",
#                 "delivery_addr": "当当当",
#                 "warehouse_id": "102",
#                 "version": 2,
#                 "order_line": [
#                     {"transId": "line1", "partner_no": "1", "task_id": "SCPC99PC190417004", "partner_number": "12345678",
#                      "partner_id": "C000820166", "product_id": "85020000171", "company_id": "1000", "partner_depart_id": "AGENCY",
#                      "qty": 100, "uom_id": "PC", "state": "None", "version": 2, "ref_type": "Sales", "ref_transId": "00000001", "ax_key": "line1"},
#                     {"transId": "line2", "partner_no": "2", "task_id": "SCPC99PC190417004", "partner_number": "12345678",
#                      "partner_id": "C000820166", "product_id": "10008000008", "company_id": "1000", "partner_depart_id": "AGENCY",
#                      "qty": 300, "uom_id": "PC", "state": "None", "version": 3, "ref_type": "Sales", "ref_transId": "00000002", "ax_key": "line2"},
#                 ],
#                 "ax_key": "SO0012"
#             }
#         }, "id": "SO0012"}
# res = requests.post(url, data=json.dumps(data), headers=headers)
# print(res.text)

#
# url = 'http://localhost:8069/ax/token'
#
# data = {"username": "admin", "time_limit": 60*60*12}
# res = requests.get(url, data=data)
# print(res, res.text)


# url = 'http://47.103.32.102:4769/test/partners'


url = 'http://localhost:8069/ax/api/purchase.order/eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJBWCBKV1QiLCJzdWIiOiJhZG1pbiIsInVpZCI6MiwiaWF0IjoxNTc0MjM4NTI0LCJleHAiOjE1NzQyODE3MjR9.llPm03NojFNaQu1qYyBqvyJMO4nku8IFODn8Kn9hbOI'
#
#
data = {"jsonrpc": "2.0", "method": "create_purchase_order",
        "params": {
            "context": {},
            "value": {
                "name": "POTEST201909090008",
                "task_id": "SCPC99PC190417004",
                "partner_id": "SVNM00002",
                "purchase_type": "Purch",
                "state": "Backorder",
                "delivery_date": "2019-09-09",
                "warehouse_id": "102",
                "site_id": "ST01",
                "company_id": "1000",
                "version": 1,
                "order_line": [
                    {"transId": "POline0909-0020", "line_number": "10003", "task_id": "SCPC99PC190417004", "product_id": "10004000005",
                     "company_id": "1000", "qty": 500, "uom_id": "PC", "state": "Backorder", "delivery_date": "2019-09-10",
                     "version": 1, "ref_type": "Purch", "ref_transId": "00000001", "sale_transId": "",
                     "ax_key": "POline0909-0020"},
                    {"transId": "POline0909-0021", "line_number": "10004", "task_id": "SCPC99PC190417004", "product_id": "10004000006",
                     "company_id": "1000", "qty": 600, "uom_id": "PC", "state": "Backorder", "delivery_date": "2019-09-10",
                     "version": 1, "ref_type": "Purch", "ref_transId": "00000001", "sale_transId": "",
                     "ax_key": "POline0909-0021"},
                ],
                "ax_key": "POTEST201909090008"
            }
        }, "id": "POTEST201909090008"}
res = requests.put(url, data=json.dumps(data), headers=headers)
print(res.text)

