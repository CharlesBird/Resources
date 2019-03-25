from django.db import models

class StockBasic(models.Model):
    ts_code = models.CharField('TS代码', max_length=16)
    symbol = models.CharField('股票代码', max_length=8, unique=True, db_index=True)
    name = models.CharField('股票名称', max_length=32, db_index=True)
    area = models.CharField('所在地域', max_length=16)
    industry = models.CharField('所属行业', max_length=16)
    fullname = models.CharField('股票全称', max_length=64)
    enname = models.CharField('英文全称', max_length=128)
    market = models.CharField('市场类型', max_length=8)
    exchange = models.CharField('交易所代码', max_length=8, choices=(('SSE','上交所'),('SZSE','深交所'),('HKEX','港交所')))
    curr_type = models.CharField('交易货币', max_length=8)
    list_status = models.CharField('上市状态', max_length=4, choices=(('L','上市'),('S','退市'),('P','暂停上市')))
    list_date = models.DateField('上市日期')
    delist_date = models.DateField('退市日期', null=True)
    is_hs = models.CharField('是否沪深港通标的', max_length=4, choices=(('N','否'),('H','沪股通'),('S','深股通')))

    def __str__(self):
        return self.ts_code

    class Meta:
        db_table = 'share_list'
        ordering = ['symbol']
        verbose_name = '股票列表'

    @staticmethod
    def pull_shares_from_tushare():
        import tushare as ts
        TOKEN = '137e3fc78e901b8463d68a102b168b2ea0217cb854abfad24d4dc7f7'
        pro = ts.pro_api(TOKEN)
        sh_list_datas = pro.stock_basic(exchange='', list_status='',
                                        fields='ts_code,symbol,name,area,industry,fullname,enname,market,exchange,curr_type,list_status,list_date,delist_date,is_hs')
        for line in sh_list_datas.to_dict('records'):
            list_date = line['list_date']
            if list_date is not None:
                line['list_date'] = '-'.join([list_date[:4], list_date[4:6], list_date[6:8]])
            delist_date = line['delist_date']
            if delist_date is not None:
                line['delist_date'] = '-'.join([delist_date[:4], delist_date[4:6], delist_date[6:8]])
            StockBasic.objects.create(**line)