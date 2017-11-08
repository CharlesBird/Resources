# -*- coding: utf-8 -*-

from openerp import tools
from openerp import models, fields


class LinyanProfitReport(models.Model):
    _name = "linyan.profit.report"
    _description = u"销售毛利统计"
    _auto = False
    _rec_name = 'product_id'

    product_id = fields.Many2one('product.product', string='商品', readonly=True)
    brand_id = fields.Many2one('linyan.brand', string='品牌', readonly=True)
    date = fields.Date('日期', readonly=True)
    year = fields.Char('年', readonly=True)
    month = fields.Char('月', readonly=True)
    profit = fields.Float('毛利', readonly=True)

    _order = 'date desc'

    def init(self, cr):
        tools.drop_view_if_exists(cr, 'linyan_profit_report')
        cr.execute("""CREATE or REPLACE VIEW linyan_profit_report as (
            select lm.id,
            lm.date2 + interval '8 hours' as date,
            extract(year from lm.date2 + interval '8 hours')::varchar(4) as year,
            extract(month from lm.date2 + interval '8 hours')::varchar(2) as month,
            lm.product_id,
            lm.brand_id,
            case when lc.picking = 't' then lc.profit*(lm.actual_qty/lc.qty_delivered)
            else lc.profit*(lm.actual_qty/lc.actual_qty) end as profit
            from logistics_move lm left join linyan_contract lc on lm.contract_id2 = lc.id
            where lm.state = 'done' and lm.contract_id2 is not null)""")
