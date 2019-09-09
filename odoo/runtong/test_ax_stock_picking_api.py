import requests
import json

headers = {'Content-Type': 'application/json'}

# url = 'http://localhost:8069/ax/token'
#
# data = {"username": "admin", "time_limit": 60*60*12}
# res = requests.get(url, data=data)
# print(res, res.text)

url = 'http://localhost:8069/ax/api/stock.picking/eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJBWCBKV1QiLCJzdWIiOiJhZG1pbiIsInVpZCI6MiwiaWF0IjoxNTY4MDA5OTYxLCJleHAiOjE1NjgwNTMxNjF9.cUg8VatZX1v2W_icbwAmUl40Rszvfp1uZeK9nkILFbY'

data = {"jsonrpc": "2.0", "method": "create_stock_picking",
        "params": {
            "context": {"journal_type": "picking", "data_origin": "AX"},
            "value": {
                "name": "Pick2019090900001",
                "journal_type_id": "Picking",
                "st_shortage": "No",
                "note": "测试数据",
                "task_id": "SCPC99PC190417004",
                "site_id": "ST01",
                "warehouse_dest_id": "102",
                "company_id": "1000",
                "ax_key": "Pick2019090900001",
                "immediate_transfer": True,
                "move_line_ids": [
                    {"line_num": "10001", "date": "2019-09-09", "product_id": "10004000005", "product_uom_qty": 300, "qty_done": 300,
                     "product_uom_id": "PC", "order_num": "c12345", "site_id": "ST01", "location_id": "101+AX-10-2",
                     "lot_id": "0000052", "lot_name": "0000052", "site_dest_id": "ST01", "location_dest_id": "102+WA1-1",
                     "sale_transId": "soline0909-0031", "ref_Id": "refid125", "company_id": "1000", "ax_key": "Pickingline0909-0001"},
                    {"line_num": "10002", "date": "2019-09-09", "product_id": "10004000006", "product_uom_qty": 300, "qty_done": 300,
                     "product_uom_id": "PC", "order_num": "c12349", "site_id": "ST01", "location_id": "101+AX-10-3",
                     "lot_id": "0000053", "lot_name": "0000053", "site_dest_id": "ST01", "location_dest_id": "102+WA1-1",
                     "sale_transId": "soline0909-0032", "ref_Id": "refid126", "company_id": "1000", "ax_key": "Pickingline0909-0002"}
                ]
            }
        }, "id": "Pick2019090900001"}
res = requests.put(url, data=json.dumps(data), headers=headers)
print(res.text)