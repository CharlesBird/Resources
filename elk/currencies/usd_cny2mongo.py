from pipelines import MongoPipeline
from collections import namedtuple
import csv


def usd_cny2mongo():
    files = ['USD_CNY_2.csv', 'USD_CNY_1.csv']
    res = []
    for file in files:
        with open(file, 'r', encoding='utf-8') as f:
            csv_file = csv.reader(f)
            headers = next(csv_file)
            Row = namedtuple('Row', headers)
            for r in csv_file:
                row = Row(*r)
                res.append(dict(row._asdict()))
    return res


if __name__ == '__main__':
    items = usd_cny2mongo()
    mongoPipe = MongoPipeline('118.190.149.30', 27017, 'exchange_rate', 'usd_cny', 'zhc', 'zhc123456')
    mongoPipe.process_item(items)