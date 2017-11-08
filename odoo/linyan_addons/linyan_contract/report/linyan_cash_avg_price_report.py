# -*- coding: utf-8 -*-

from openerp import tools
from openerp import models, fields
import openerp.addons.decimal_precision as dp


class LinyanCashAvgPriceReport(models.Model):
    _name = "linyan.cash.avg.price.report"
    _description = u"头寸数量，与加权平均价"
    _auto = False

    buy_remaining_qty = fields.Float('买入头寸', digits=dp.get_precision('Product Unit of Measure'), readonly=True)
    buy_avg_untax_price = fields.Float('买入税前平均价', digits=dp.get_precision('Product Price'), readonly=True)
    buy_avg_price = fields.Float('买入平均价', digits=dp.get_precision('Product Price'), readonly=True)
    remaining_qty = fields.Float('卖出头寸', digits=dp.get_precision('Product Unit of Measure'), readonly=True)
    avg_untax_price = fields.Float('卖出税前平均价', digits=dp.get_precision('Product Price'), readonly=True)
    avg_price = fields.Float('卖出平均价', digits=dp.get_precision('Product Price'), readonly=True)

    def init(self, cr):
        tools.drop_view_if_exists(cr, 'linyan_cash_avg_price_report')
        cr.execute("""CREATE or REPLACE VIEW linyan_cash_avg_price_report as (
            select t1.id,
            t1.buy_remaining_qty,
            t1.buy_avg_untax_price,
            t1.buy_avg_price,
            t2.remaining_qty,
            t2.avg_untax_price,
            t2.avg_price
            from (select 1 as id,
                sum(remaining_qty) as buy_remaining_qty,
                sum(untax_price * remaining_qty) / sum(remaining_qty) as buy_avg_untax_price,
                sum(price * remaining_qty) / sum(remaining_qty) as buy_avg_price
                from linyan_contract where remaining_qty != 0 and buy = 't') t1
            join
                (select 1 as id,
                sum(remaining_qty) as remaining_qty,
                sum(untax_price * remaining_qty) / sum(remaining_qty) as avg_untax_price,
                sum(price * remaining_qty) / sum(remaining_qty) as avg_price
                from linyan_contract where remaining_qty != 0 and buy = 'f') t2 on t1.id = t2.id)""")
