import tushare as ts
import requests
import re

TOKEN = '137e3fc78e901b8463d68a102b168b2ea0217cb854abfad24d4dc7f7'
pro = ts.pro_api(TOKEN)
sh_list_datas = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,fullname,market,exchange,curr_type,list_status,list_date')
# print(sh_list_datas)
# for ts_code in sh_list_datas['ts_code']:
#     df = pro.daily(ts_code=ts_code, end_date='20190306')
#     print(df)
symbol_list = sh_list_datas.head(800)['symbol']
code_list = ','.join(map(lambda symbol: 'sh'+str(symbol), symbol_list))
# print(code_list)
response = requests.get('http://hq.sinajs.cn/list={}'.format(code_list))
print(response.text)
result = re.findall(r'hq_str_sh(\d*)="(.*)";', response.text)
print(result)
# for line in result:
#     k = line[0]
#     data = line[1]
#     data_list = data.split(',')
#     print(k, data_list)
# print(result)

# response = requests.get('http://money.finance.sina.com.cn/quotes_service/api/json_v2.php/CN_MarketData.getKLineData?symbol=sz000001&scale=5&ma=5&datalen=1023')
# print(response.text)