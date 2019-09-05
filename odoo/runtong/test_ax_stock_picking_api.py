import requests
import json

headers = {'Content-Type': 'application/json'}

# url = 'http://localhost:8069/ax/token'
#
# data = {"username": "admin", "time_limit": 60*60*12}
# res = requests.get(url, data=data)
# print(res, res.text)

url = 'http://localhost:8069/ax/api/stock.picking/eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJBWCBKV1QiLCJzdWIiOiJhZG1pbiIsInVpZCI6MiwiaWF0IjoxNTY3NDcyNzM4LCJleHAiOjE1Njc1MTU5Mzh9.M18l24qfjZ7VvdpNfnGfSBp5Hi0YFSgnbyX_uVARi84'

data = {"jsonrpc": "2.0", "method": "create_stock_picking",
        "params": {
            "context": {"journal_type": "picking", "data_origin": "AX"},
            "value": {
                "name": "2019090300002",
                "journal_type_id": "Picking",
                "st_shortage": "No",
                "note": "测试数据",
                "task_id": "SCPC99PC190417004",
                "site_id": "ST01",
                "warehouse_dest_id": "102",
                "company_id": "1000",
                "ax_key": "2019090300001",
                "immediate_transfer": True,
                "move_line_ids": [
                    {"line_num": "2001", "date": "2019-09-03", "product_id": "10001000007", "product_uom_qty": 10, "qty_done": 10,
                     "product_uom_id": "PC", "order_num": "c12345", "site_id": "ST01", "location_id": "101+AX-10-1",
                     "lot_id": "0000027", "lot_name": "0000027", "site_dest_id": "ST01", "location_dest_id": "102+WA1-1",
                     "sale_transId": "Soline123", "ref_Id": "refid123", "company_id": "1000", "ax_key": "Pickingline3"},
                    {"line_num": "2002", "date": "2019-09-03", "product_id": "10001000002", "product_uom_qty": 5, "qty_done": 5,
                     "product_uom_id": "PC", "order_num": "c12349", "site_id": "ST01", "location_id": "101+AX-10-1",
                     "lot_id": "0000023", "lot_name": "0000023", "site_dest_id": "ST01", "location_dest_id": "102+WA1-1",
                     "sale_transId": "Soline125", "ref_Id": "refid123", "company_id": "1000", "ax_key": "Pickingline4"}
                ]
            }
        }, "id": "2019090300002"}
res = requests.put(url, data=json.dumps(data), headers=headers)
print(res.text)