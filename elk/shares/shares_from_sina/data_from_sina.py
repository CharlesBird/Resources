"""
es 插入速度优化？
多进程+异步IO ？
"""
import tushare as ts
from elasticsearch import Elasticsearch
from elasticsearch import helpers
import re
import requests
from datetime import datetime
import time
import threading
import multiprocessing
from concurrent.futures import ThreadPoolExecutor
TOKEN = '137e3fc78e901b8463d68a102b168b2ea0217cb854abfad24d4dc7f7'
pro = ts.pro_api(TOKEN)
es = Elasticsearch(['47.103.32.102:9200'])

index = "shares_real_time_data_2019-09-19_00001"


def all_shares_codes():
    sh_list_datas = pro.stock_basic(exchange='', list_status='', fields='ts_code,symbol')
    return sh_list_datas.to_dict('records')


def get_sina_codes(step=100):
    """
    :param step: 子列表长度
    :return: [[], [], []...]
    """
    shares_list = all_shares_codes()
    start = 0
    sina_codes = []
    while shares_list[start:start + step]:
        per_codes = []
        for share in shares_list[start:start + step]:
            if share['ts_code'][-2:] == 'SH':
                per_codes.append('sh' + share['symbol'])
            elif share['ts_code'][-2:] == 'SZ':
                per_codes.append('sz' + share['symbol'])
            else:
                pass
        sina_codes.append(per_codes)
        start += step
    return sina_codes


def get_share_datas(codes):
    # sina_codes = get_sina_codes()
    # for codes in sina_codes:
    # s1 = time.time()
    url = 'http://hq.sinajs.cn/list={}'.format(','.join(codes))
    response = requests.get(url)
    data = response.text
    # print('requests time: ', time.time() - s1)

    # s2 = time.time()
    pattern = re.compile('="(.*)"')
    data_list = pattern.findall(data)
    actions = []
    for i, str_data in enumerate(data_list):
        code = codes[i]
        list_data = str_data.split(',')
        features = ['name', 'open', 'yesterday_close', 'price', 'high', 'low', 'bid_price', 'auction_price',
                    'volume', 'amount', 'buy1_vol', 'buy1_quote', 'buy2_vol', 'buy2_quote', 'buy3_vol',
                    'buy3_quote', 'buy4_vol', 'buy4_quote', 'buy5_vol', 'buy5_quote', 'sell1_vol', 'sell1_quote',
                    'sell2_vol', 'sell2_quote', 'sell3_vol', 'sell3_quote', 'sell4_vol', 'sell4_quote', 'sell5_vol',
                    'sell5_quote']
        value = {'code': code}
        for j, f in enumerate(features):
            value.update({f: list_data[j]})
        date = list_data[30]
        date_t = list_data[31]
        str_date = date + ' ' + date_t
        d = datetime.strptime(str_date, '%Y-%m-%d %H:%M:%S')
        value.update({'@timestamp': d})
        action = {
            "index": index,
            "doc_type": "_doc",
            "_source": value
        }
        actions.append(action)
        # print(value)
    insert_into_es(actions)
    # print('deal data time: ', time.time() - s2)


def insert_into_es(values):
    # es.bulk(values, index=index)
    helpers.bulk(es, values, index=index)
    # es.index(index=index, body=data)


class SharesThread(threading.Thread):

    def __init__(self, thread_name, codes):
        threading.Thread.__init__(self)
        self.name = thread_name
        self.codes = codes

    def run(self) -> None:
        # print("Current thread: {}".format(threading.current_thread().getName()))
        get_share_datas(self.codes)


# def main(per_codes):
#     """
#     不用多线程
#     :param all_codes:
#     :return:
#     """
#     get_share_datas(per_codes)


def main(per_codes):
    """
    使用线程池
    :param per_codes:
    :return:
    """
    interval = len(per_codes) // 20
    i = 0
    tasks = []
    executor = ThreadPoolExecutor(max_workers=5)
    while per_codes[i: i+interval]:
        task = executor.submit(get_share_datas, (per_codes[i: i+interval], ))
        tasks.append(task)
    for t in tasks:
        print(t.done())
        print(t.result())


if __name__ == '__main__':
    # step: 500, time: 18.63
    # step: 600, time: 19
    # step: 800, time: 24
    sina_codes = get_sina_codes()

    while True:
        process_pool = multiprocessing.Pool(6)
        s = time.time()
        for cs in sina_codes:
            process_pool.apply_async(main, args=(cs,))

        process_pool.close()
        process_pool.join()

        print('Over...')
        print('Total time: ', time.time() - s)


"""
Linux
requests time:  0.019827604293823242
requests time:  0.02409052848815918
requests time:  0.02358698844909668
requests time:  0.029944419860839844
requests time:  0.02356100082397461
requests time:  0.030556201934814453
requests time:  0.03229117393493652
requests time:  0.023755788803100586
requests time:  0.02716207504272461
requests time:  0.02599811553955078
requests time:  0.038443565368652344
requests time:  0.054688215255737305
requests time:  0.02953338623046875
requests time:  0.04949188232421875
requests time:  0.046948909759521484
requests time:  0.03600573539733887
requests time:  0.05284476280212402
requests time:  0.06654834747314453
requests time:  0.05897092819213867
requests time:  0.05301642417907715
requests time:  0.05198073387145996
requests time:  0.06847715377807617
requests time:  0.05627727508544922
requests time:  0.027814865112304688
requests time:  0.027997732162475586
requests time:  0.055940866470336914
requests time:  0.06766033172607422
requests time:  0.06978201866149902
requests time:  0.08487105369567871
requests time:  0.013313770294189453
requests time:  0.06674385070800781
requests time:  0.020785808563232422
requests time:  0.044267892837524414
requests time:  0.020911455154418945
requests time:  0.04450535774230957
requests time:  0.019321203231811523
requests time:  0.02321004867553711
requests time:  0.021479129791259766
requests time:  0.017664432525634766
requests time:  0.043720245361328125
requests time:  0.02530360221862793
requests time:  0.013871431350708008
requests time:  0.05796003341674805
requests time:  0.04012012481689453
requests time:  0.044471025466918945
requests time:  0.025713443756103516
requests time:  0.018213748931884766
requests time:  0.03302264213562012
requests time:  0.021834135055541992
requests time:  0.035663604736328125
requests time:  0.034728288650512695
requests time:  0.031192302703857422
requests time:  0.018440723419189453
requests time:  0.03617238998413086
requests time:  0.048723697662353516
deal data time:  2.99039626121521
deal data time:  3.1815121173858643
deal data time:  3.200035810470581
deal data time:  3.3738362789154053
deal data time:  3.333780288696289
deal data time:  3.4447898864746094
deal data time:  3.4242405891418457
deal data time:  3.5241057872772217
deal data time:  3.4341881275177
deal data time:  3.6147971153259277
deal data time:  3.6722612380981445
deal data time:  3.74814772605896
deal data time:  3.705871343612671
deal data time:  3.7933945655822754
deal data time:  3.7746472358703613
deal data time:  3.6964669227600098
deal data time:  3.7926621437072754
deal data time:  3.738291025161743
deal data time:  3.8311455249786377
deal data time:  3.7964775562286377
deal data time:  3.9103660583496094
deal data time:  3.914250135421753
deal data time:  3.901224374771118
deal data time:  3.7858169078826904
deal data time:  3.8557279109954834
deal data time:  3.855412483215332
deal data time:  3.8764936923980713
deal data time:  3.917663812637329
deal data time:  3.9667913913726807
deal data time:  3.883902072906494
deal data time:  3.8951845169067383
deal data time:  3.8885750770568848
deal data time:  3.9496912956237793
deal data time:  3.9765312671661377
deal data time:  3.956423759460449
deal data time:  3.925088882446289
deal data time:  3.940563440322876
deal data time:  3.9984939098358154
deal data time:  3.963765859603882
deal data time:  4.023428678512573
deal data time:  4.053938865661621
deal data time:  4.034225702285767
deal data time:  4.036418914794922
deal data time:  4.023843288421631
deal data time:  4.035953521728516
deal data time:  4.06139874458313
deal data time:  4.024825811386108
deal data time:  4.0828330516815186
deal data time:  4.024506092071533
deal data time:  4.082539796829224
deal data time:  4.041406631469727
deal data time:  4.014848709106445
deal data time:  4.060866832733154
deal data time:  4.065259218215942
deal data time:  4.06471848487854
Over...
Total time:  4.230188369750977
"""