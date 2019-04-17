import requests
import re
import time
import asyncio
import aiohttp
url = 'http://hq.sinajs.cn/list=hf_OIL'
check = None
while True:
    response = requests.get(url)
    resp = response.text

    pattern = re.compile('="(.*)"')
    s = pattern.findall(resp)
    res = {}
    if s:
        s_l = s[0].split(',')
        change_time = ' '.join([s_l[12], s_l[6]])
        if check is None:
            check = change_time
        else:
            if check == change_time:
                continue
        res.update({
            'last_price': float(s_l[0]),
            'change_value': float(s_l[1]),
            'buy_price': float(s_l[2]),
            'sell_price': float(s_l[3]),
            'max_price': float(s_l[4]),
            'min_price': float(s_l[5]),
            'yestoday_price': float(s_l[7]),
            'open_price': float(s_l[8]),
            'amount': float(s_l[9]),
            'buy_amount': float(s_l[10]),
            'sell_amount': float(s_l[11]),
            'name': s_l[13],
            'change_time': change_time
        })
        check = change_time
    time.sleep(1)
    print(res)