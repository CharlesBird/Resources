# http://tushare.org/
import tushare as ts
import requests
import re

TOKEN = '137e3fc78e901b8463d68a102b168b2ea0217cb854abfad24d4dc7f7'
pro = ts.pro_api(TOKEN)
sh_list_datas = pro.stock_basic(exchange='', list_status='', fields='ts_code,symbol,name,area,industry,fullname,enname,market,exchange,curr_type,list_status,list_date,delist_date,is_hs')
# sh_list_datas.to_csv('share_list.csv',index=0)
res = sh_list_datas.to_dict('records')
# print(res)
for r in res:
    print(r)
# print(list(sh_list_datas.head(1)))
# for f in list(sh_list_datas.head(1)):
#     print(f + '; ' + sh_list_datas.head(1)[f])
# print(sh_list_datas.head(1), )
# print(len(sh_list_datas))
# for ts_code in sh_list_datas['ts_code']:
#     df = pro.daily(ts_code=ts_code, end_date='20190306')
#     print(df)
# symbol_list = sh_list_datas.head(800)['symbol']
# code_list = ','.join(map(lambda symbol: 'sh'+str(symbol), symbol_list))
# print(code_list)
# response = requests.get('http://hq.sinajs.cn/list={}'.format(code_list))
# print(response.text)
# result = re.findall(r'hq_str_sh(\d*)="(.*)";', response.text)
# print(result)
# for line in result:
#     k = line[0]
#     data = line[1]
#     data_list = data.split(',')
#     print(k, data_list)
# print(result)

# response = requests.get('http://money.finance.sina.com.cn/quotes_service/api/json_v2.php/CN_MarketData.getKLineData?symbol=sz000001&scale=5&ma=5&datalen=1023')
# print(response.text)