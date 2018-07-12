from pipelines import MongoPipeline
from collections import namedtuple
import csv
from datetime import datetime


def usd_cny2mongo():
    files = ['shanghai-2.csv', 'shanghai-1.csv']
    res = []
    for file in files:
        with open(file, 'r', encoding='utf-8') as f:
            csv_file = csv.reader(f)
            headers = next(csv_file)
            Row = namedtuple('Row', headers)
            for r in csv_file:
                r[0] = datetime.strptime(r[0], '%Y年%m月%d日').strftime('%Y-%m-%d')
                row = Row(*r)
                res.append(dict(row._asdict()))
    return res


if __name__ == '__main__':
    items = usd_cny2mongo()
    mongoPipe = MongoPipeline('118.190.149.30', 27017, 'shanghai_composite', 'composite_day', 'zhc', 'zhc123456')
    mongoPipe.process_item(items)