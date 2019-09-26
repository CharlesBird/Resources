import requests
import json

headers = {'Content-Type': 'application/json'}

# url = 'http://localhost:8069/ax/token'
#
# data = {"username": "admin", "time_limit": 60*60*12}
# res = requests.get(url, data=data)
# print(res, res.text)

url = 'http://localhost:8069/ax/api/stock.picking/eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJBWCBKV1QiLCJzdWIiOiJhZG1pbiIsInVpZCI6MiwiaWF0IjoxNTY5NDY1NDEzLCJleHAiOjE1Njk1MDg2MTN9.rkyhPZASpcX9o6GOI_u1U6aar72buq5EoEn-DXrD2YI'

data = {"jsonrpc": "2.0", "method": "create_stock_picking",
        "params": {
            "context": {"journal_type": "picking", "data_origin": "AX"},
            "value": {
                "name": "Pick2019092600005",
                "journal_type_id": "Transfer",
                "st_shortage": "No",
                "note": "测试数据",
                "task_id": "SCPC99PC190417004",
                "site_id": "ST01",
                "warehouse_dest_id": "102",
                "company_id": "1000",
                "ax_key": "Pick2019092600005",
                "immediate_transfer": True,
                "move_line_ids": [
                    {"line_num": "100020001", "date": "2019-09-26", "product_id": "10004000005", "product_uom_qty": 300, "qty_done": 2, "planned_qty": 300,
                     "product_uom_id": "PC", "order_num": "c12345", "site_id": "ST01", "location_id": "101+AX-10-2",
                     "lot_id": "0000052", "lot_name": "0000052", "site_dest_id": "ST01", "location_dest_id": "102+WA1-1",
                     "sale_transId": "soline0909-0031", "ref_Id": "refid125", "company_id": "1000", "ax_key": "Pickingline0926-0001"},
                    {"line_num": "100030001", "date": "2019-09-26", "product_id": "10004000006", "product_uom_qty": 300, "qty_done": 0, "planned_qty": 300,
                     "product_uom_id": "PC", "order_num": "c12349", "site_id": "ST01", "location_id": "101+AX-10-3",
                     "lot_id": "0000053", "lot_name": "0000053", "site_dest_id": "ST01", "location_dest_id": "102+WA1-1",
                     "sale_transId": "soline0909-0032", "ref_Id": "refid126", "company_id": "1000", "ax_key": "Pickingline0926-0002"}
                ]
            }
        }, "id": "Pick2019090900001"}
res = requests.put(url, data=json.dumps(data), headers=headers)
print(res.text)