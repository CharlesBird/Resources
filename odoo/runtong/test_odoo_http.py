import requests
import json

headers = {'Content-Type': 'application/json', }

# url = 'http://localhost:8069/ax/api/sale.order/eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJBWCBKV1QiLCJzdWIiOiJhZG1pbiIsInVpZCI6MiwiaWF0IjoxNTYzOTUzMTIwLCJleHAiOjE1NjM5OTYzMjB9.LMzR4DE3VLiB4iIn9wi1f1k2pe6j0QZv8G46IkMwNGM'
#
# data = {"jsonrpc": "2.0", "method": "create_sale_order",
#         "params": {
#             "context": {},
#             "value": {
#                 "name": "SO0012",
#                 "task_id": "SCPC99PC190417004",
#                 "partner_id": "C000300670",
#                 "partner_number": "5464567",
#                 "state": "None",
#                 "sale_type": "Sales",
#                 "delivery_date": "2018-09-09",
#                 "delivery_addr": "dfghdfhdfgh",
#                 "warehouse_id": "102",
#                 "version": 1,
#                 "order_line": [
#                     {"transId": "line1", "partner_no": "1", "task_id": "SCPC99PC190417004", "partner_number": "5464567",
#                      "partner_id": "C000820166", "product_id": "85020000171", "company_id": "1000", "partner_depart_id": "AGENCY",
#                      "qty": 100, "uom_id": "PC", "state": "None", "version": 1, "ref_type": "Sales", "ref_transId": "00000001", "ax_key": "line1"},
#                     {"transId": "line2", "partner_no": "2", "task_id": "SCPC99PC190417004", "partner_number": "5464567",
#                      "partner_id": "C000820166", "product_id": "10008000008", "company_id": "1000", "partner_depart_id": "AGENCY",
#                      "qty": 200, "uom_id": "PC", "state": "None", "version": 1, "ref_type": "Sales", "ref_transId": "00000002", "ax_key": "line2"},
#                 ],
#                 "ax_key": "SO0012"
#             }
#         }, "id": None}
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


url = 'http://localhost:8069/ax/api/purchase.order/eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJBWCBKV1QiLCJzdWIiOiJhZG1pbiIsInVpZCI6MiwiaWF0IjoxNTY2OTgyNTQwLCJleHAiOjE1NjcwMjU3NDB9.AR-fzJ31p7Yx1H8jErXw6-HRs68feEB0N8lRwNk2mMA'


data = {"jsonrpc": "2.0", "method": "create_purchase_order",
        "params": {
            "context": {},
            "value": {
                "name": "PO19082801",
                "task_id": "SCPC99PC190417004",
                "partner_id": "SKOR00024",
                "purchase_type": "Purch",
                "state": "Backorder",
                "delivery_date": "2019-08-28",
                "warehouse_id": "102",
                "site_id": "ST01",
                "company_id": "1000",
                "version": 1,
                "order_line": [
                    # {"transId": "POline1", "line_number": "10000", "task_id": "SCPC99PC190417004", "product_id": "10001000007",
                    #  "company_id": "1000", "qty": 100, "uom_id": "PC", "state": "Backorder", "delivery_date": "2019-08-19",
                    #  "version": 1, "ref_type": "Purch", "ref_transId": "00000001", "sale_transId": "SOline1", "ax_key": "POline1"},
                    # {"transId": "POline2", "line_number": "10001", "task_id": "SCPC99PC190417004",
                    #  "product_id": "10001000013",
                    #  "company_id": "1000", "qty": 100, "uom_id": "PC", "state": "Backorder",
                    #  "delivery_date": "2019-08-19",
                    #  "version": 1, "ref_type": "Purch", "ref_transId": "00000001", "sale_transId": "SOline2",
                    #  "ax_key": "POline2"},
                    # {"transId": "POline3", "line_number": "10001", "task_id": "SCPC99PC190417004",
                    #  "product_id": "10001000017",
                    #  "company_id": "1000", "qty": 300, "uom_id": "PC", "state": "Backorder",
                    #  "delivery_date": "2019-08-19",
                    #  "version": 1, "ref_type": "Purch", "ref_transId": "00000001", "sale_transId": "SOline3",
                    #  "ax_key": "POline3"},

                    {"transId": "POline4", "line_number": "10000", "task_id": "SCPC99PC190417004", "product_id": "10001000007",
                     "company_id": "1000", "qty": 100, "uom_id": "PC", "state": "Backorder", "delivery_date": "2019-08-19",
                     "version": 1, "ref_type": "Purch", "ref_transId": "00000001", "sale_transId": "SOline4", "ax_key": "POline4"},
                    {"transId": "POline5", "line_number": "10001", "task_id": "SCPC99PC190417004",
                     "product_id": "10001000013",
                     "company_id": "1000", "qty": 100, "uom_id": "PC", "state": "Backorder",
                     "delivery_date": "2019-08-19",
                     "version": 1, "ref_type": "Purch", "ref_transId": "00000001", "sale_transId": "SOline5",
                     "ax_key": "POline5"},
                    {"transId": "POline6", "line_number": "10001", "task_id": "SCPC99PC190417004",
                     "product_id": "10001000017",
                     "company_id": "1000", "qty": 300, "uom_id": "PC", "state": "Backorder",
                     "delivery_date": "2019-08-19",
                     "version": 1, "ref_type": "Purch", "ref_transId": "00000001", "sale_transId": "SOline6",
                     "ax_key": "POline6"},
                ],
                "ax_key": "PO19082801"
            }
        }, "id": "PO19082801"}
res = requests.put(url, data=json.dumps(data), headers=headers)
print(res.text)

