# http://tushare.org/
import tushare as ts
import requests
import re

TOKEN = '137e3fc78e901b8463d68a102b168b2ea0217cb854abfad24d4dc7f7'
pro = ts.pro_api(TOKEN)

sh_list_datas = pro.stock_basic(exchange='', list_status='', fields='ts_code,symbol,name,area,industry,fullname,enname,market,exchange,curr_type,list_status,list_date,delist_date,is_hs')
# sh_list_datas.to_csv('share_list.csv',index=0)
res = sh_list_datas.to_dict('records')
for r in res:
    print(r)

dates = pro.trade_cal(exchange='', start_date='20190411', end_date='20190515')
print(dates)

df = pro.daily(ts_code='000001.SZ', trade_date='20190705')
print(df)

df = pro.weekly(ts_code='000001.SZ', trade_date='20190705')
print(df)

# for ts_code in sh_list_datas['ts_code']:
#     df = pro.daily(ts_code=ts_code, end_date='20190326')
#     d_data = df.to_dict('records')
#     for d in d_data:
#         print(d)
# ts.get_latest_news(top=5,show_content=True)
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