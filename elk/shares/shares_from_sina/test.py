# http://hq.sinajs.cn/list=sz000016
import tushare as ts
import re
import requests
TOKEN = '137e3fc78e901b8463d68a102b168b2ea0217cb854abfad24d4dc7f7'
pro = ts.pro_api(TOKEN)
sh_list_datas = pro.stock_basic(exchange='', list_status='', fields='ts_code,symbol')
shares_list = sh_list_datas.to_dict('records')

step = 800
start = 0
sina_codes = []
while shares_list[start:start+step]:
    per_codes = []
    for share in shares_list[start:start+step]:
        if share['ts_code'][-2:] == 'SH':
            per_codes.append('sh' + share['symbol'])
        elif share['ts_code'][-2:] == 'SZ':
            per_codes.append('sz' + share['symbol'])
        else:
            pass
    sina_codes.append(per_codes)
    start += step
# print(sina_codes)

result = {}
for codes in sina_codes:
    url = 'http://hq.sinajs.cn/list={}'.format(','.join(codes))
    response = requests.get(url)
    data = response.text
    pattern = re.compile('="(.*)"')
    data_list = pattern.findall(data)
    # print(codes)
    # print(data_list)
    for i, str_data in enumerate(data_list):
        code = codes[i]
        list_data = str_data.split(',')
        # print(code, list_data)
        # result.update({code: list_data})
        print(code, len(list_data))
        print(list_data)
# print(result)