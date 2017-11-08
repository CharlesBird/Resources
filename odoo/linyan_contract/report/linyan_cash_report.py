# -*- coding: utf-8 -*-

import time
from openerp import api, models, fields
import openerp.addons.decimal_precision as dp


class LinyanCashReport(models.TransientModel):
    _name = 'linyan.cash.report'

    partner_id = fields.Many2one('res.partner', '合同方', readonly=True)
    product_id = fields.Many2one('product.product', '产品', readonly=True)
    year = fields.Char('合同年', readonly=True)
    month = fields.Char('合同月', readonly=True)
    contract_name = fields.Char('合同编号', readonly=True)
    actual_qty = fields.Float('数量', digits=dp.get_precision('Product Unit of Measure'), readonly=True)
    price = fields.Float('单价', digits=dp.get_precision('Product Price'), readonly=True)
    # untax_price = fields.Float('税前单价', digits=dp.get_precision('Product Price'), readonly=True)
    amount = fields.Float('金额', readonly=True)
    cash = fields.Boolean('头寸', readonly=True)


class MoveQuantityReport(models.TransientModel):
    _name = 'move.quantity.report'

    warehouse_id = fields.Many2one('stock.warehouse', '仓库', readonly=True)
    product_id = fields.Many2one('product.product', '产品', readonly=True)
    make_company = fields.Char('品牌', readonly=True)
    supplierinfo_id = fields.Many2one('product.supplierinfo', '型号', readonly=True)
    actual_qty = fields.Float('数量', digits=dp.get_precision('Product Unit of Measure'), readonly=True)


class LinyanInvoiceReport(models.TransientModel):
    _name = 'linyan.invoice.report'

    rece_invoice = fields.Float('应收未收总金额', readonly=True)
    pay_invoice = fields.Float('应付未付总金额', readonly=True)
    rece_payment = fields.Float('已收未提总金额', readonly=True)
    pay_payment = fields.Float('实付未提总金额', readonly=True)
    amount = fields.Float('总值', readonly=True)
