import tushare as ts
import requests
import re

TOKEN = '137e3fc78e901b8463d68a102b168b2ea0217cb854abfad24d4dc7f7'
pro = ts.pro_api(TOKEN)
sh_list_datas = pro.stock_basic(exchange='SSE', list_status='L', fields='ts_code,symbol,name,area,industry,fullname,market,curr_type,list_date')
print(len(sh_list_datas))
symbol_list = sh_list_datas.head(800)['symbol']
code_list = ','.join(map(lambda symbol: 'sh'+str(symbol), symbol_list))
# print(code_list)
response = requests.get('http://hq.sinajs.cn/list={}'.format(code_list))
print(response.text)
result = re.findall(r'hq_str_sh(\d*)="(.*)";', response.text)
# print(result)
# for line in result:
#     k = line[0]
#     data = line[1]
#     data_list = data.split(',')
#     print(k, data_list)
# print(result)