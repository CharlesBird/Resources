# http://tushare.org/
import tushare as ts
import requests
import re

TOKEN = 'dc1e13cbe81f034909eecb8b0abad6341db7115b751c3196c3264242'
pro = ts.pro_api(TOKEN)

# sh_list_datas = pro.stock_basic(exchange='', list_status='', fields='ts_code,symbol,name,area,industry,fullname,enname,market,exchange,curr_type,list_status,list_date,delist_date,is_hs')
# sh_list_datas.to_csv('share_list.csv',index=0)
# res = sh_list_datas.to_dict('records')
# for r in res:
#     print(r)

# dates = pro.trade_cal(exchange='', start_date='20190411', end_date='20190515')
# print(dates)

df = pro.daily(ts_code='601700.SH', trade_date='20190730')
print(df)

# df = ts.pro_bar(ts_code='000035.SZ', api=pro, asset='I', start_date='20190710', end_date='20190712', freq='1min')
# print(df)

# df = pro.mins(ts_code='000001.SZ', start_time='20190912', end_time='20190913', freq='1min')
# print(df)

# df = pro.suspend(ts_code='', suspend_date='20190715', resume_date='', fields='ts_code,suspend_date,resume_date,ann_date,suspend_reason,reason_type')
# print(df)

# df = pro.weekly(ts_code='000001.SZ', trade_date='20190705')
# print(df)

# df = pro.news(src='sina', start_date='20170725 09:00:00', end_date='20190725 11:00:00', fields='datetime,content,title,channels')
# res = df.to_dict('records')
# for r in res:
#     print(r)
# print(df)

# df = pro.anns(ts_code='600519.SH', start_date='20190401', end_date='20191231', year='2019')
# print(df)

# df = pro.cctv_news(date='20190724')
# res = df.to_dict('records')
# for r in res:
#     print(r)

# df = pro.income(ts_code='600519.SH', start_date='20190101', end_date='20191230')
# print(df)

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