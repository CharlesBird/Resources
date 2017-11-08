# -*- coding: utf-8 -*-

import json
from lxml import etree
from dateutil.relativedelta import relativedelta
from openerp import api, fields, models
from openerp.tools import float_is_zero, float_compare, float_round, DEFAULT_SERVER_DATETIME_FORMAT
from openerp.exceptions import UserError, RedirectWarning, ValidationError
import openerp.addons.decimal_precision as dp
from datetime import datetime
import time

MAP_INVOICE_TYPE_PARTNER_TYPE = {
    'out_invoice': 'customer',
    'in_invoice': 'supplier'
}


class LinyanContract(models.Model):
    _name = "linyan.contract"
    _inherit = ["mail.thread", "ir.needaction_mixin"]
    _description = "Sales or Pusrchase Order"
    _order = 'create_date desc, id desc'

    # @api.model
    # def _default_warehouse_id(self):
    #     company = self.env.user.company_id.id
    #     warehouse_ids = self.env['stock.warehouse'].search([('company_id', '=', company)], limit=1)
    #     return warehouse_ids

    @api.depends('price', 'actual_qty', 'currency_id', 'tax_ids', 'qty_delivered', 'picking')
    def _compute_price(self):
        for o in self:
            taxes = o.tax_ids.compute_all(o.price, o.currency_id, 1.0, product=o.product_id or False, partner=o.partner_id)
            if o.picking:
                o.amount = o.price * o.qty_delivered
            else:
                o.amount = o.price * o.actual_qty
            o.untax_price = taxes['total_excluded']

    @api.depends('actual_qty', 'used_qty', 'contract_line', 'product_id')
    def _get_compute_qty(self):
        for o in self:
            rounding = o.product_id and o.product_id.uom_id.rounding or 0.0100
            if o.buy:
                o.remaining_qty = float_round(o.actual_qty - o.used_qty, precision_rounding=rounding)
            else:
                used_qty = sum(o.contract_line.mapped('actual_qty'))
                o.remaining_qty = float_round(o.actual_qty - used_qty, precision_rounding=rounding)

    @api.depends('actual_qty', 'qty_delivered', 'picking')
    def _get_qty_to_delivered(self):
        for o in self:
            o.qty_to_delivered = 0.0 if o.picking else (o.actual_qty - o.qty_delivered)

    @api.depends('amount', 'invoice_line', 'invoice_line.invoice_line')
    def _get_unpayment_amount(self):
        for o in self:
            payment_amount = o.invoice_line and o.invoice_line.mapped('invoice_line') and sum(o.invoice_line.mapped('invoice_line').mapped('used_amount')) or 0.0
            o.unpayment_amount = o.amount - payment_amount

    # @api.depends('qty_invoiced', 'qty_delivered', 'actual_qty', 'state')
    # def _get_to_invoice_qty(self):
    #     for o in self:
    #         if o.state in ['sign', 'moved', 'paid', 'done']:
    #             if o.account_ref == 'contract':
    #                 o.qty_to_invoice = o.actual_qty - o.qty_invoiced
    #             else:
    #                 o.qty_to_invoice = o.qty_delivered - o.qty_invoiced
    #         else:
    #             o.qty_to_invoice = 0

    # @api.depends('invoice_lines.invoice_id.state', 'invoice_lines.quantity')
    # def _get_invoice_qty(self):
    #     for o in self:
    #         qty_invoiced = 0.0
    #         for invoice_line in o.invoice_lines:
    #             if invoice_line.invoice_id.state != 'cancel':
    #                 if invoice_line.invoice_id.type in ('out_invoice', 'in_invoice'):
    #                     qty_invoiced += invoice_line.quantity
    #                 elif invoice_line.invoice_id.type == ('out_refund', 'in_refund'):
    #                     qty_invoiced -= invoice_line.quantity
    #         o.qty_invoiced = qty_invoiced

    @api.depends('state', 'invoice_lines')
    def _compute_invoice_status(self):
        for o in self:
            invoice_ids = o.invoice_lines.mapped('invoice_id')
            o.invoice_count = len(set(invoice_ids.ids))

    @api.multi
    @api.depends('move_ids')
    def _compute_move_ids(self):
        for o in self:
            o.delivery_count = len(o.move_ids)

    @api.multi
    @api.depends('picking', 'amount', 'buy', 'contract_amount', 'contract_line.actual_qty', 'contract_line.buy_id', 'contract_line.buy_id.picking', 'sale_contract_line.relation_qty', 'sale_contract_line.sale_id', 'sale_contract_line.untax_price')
    def _compute_profit(self):
        for o in self:
            if o.buy:
                profit = 0.0
                if o.sale_contract_line:
                    for line in o.sale_contract_line:
                        untax_price = line.sale_id.untax_price
                        relation_qty = line.relation_qty
                        # if line.sale_id.picking:
                        #     relation_qty = line.sale_id.qty_delivered
                        profit += (untax_price - o.untax_price - line.sale_id.contract_amount - o.contract_amount) * relation_qty
                    o.profit = profit
                else:
                    o.profit = 0.0
            else:
                if o.contract_line:
                    buy_amount = sale_amount = 0.0
                    if o.picking:
                        sale_amount = (o.untax_price - o.contract_amount) * o.qty_delivered
                    else:
                        sale_amount = (o.untax_price - o.contract_amount) * o.actual_qty
                    for line in o.contract_line:
                        actual_qty = line.actual_qty
                        untax_price = line.buy_id.untax_price
                        buy_contract_amount = line.buy_id.contract_amount
                        picking = line.buy_id.picking
                        if picking:
                            qty_delivered = line.buy_id.qty_delivered
                            buy_amount += (untax_price + buy_contract_amount) * min(actual_qty, qty_delivered)
                        else:
                            buy_amount += (untax_price + buy_contract_amount) * actual_qty
                    o.profit = sale_amount - buy_amount
                else:
                    o.profit = 0.0

    @api.one
    # @api.depends('contract_line')
    def _compute_sell_ids(self):
        contract_line = self.contract_line.search([('buy_id', '=', self.id)])
        if contract_line:
            self.sell_ids = contract_line.mapped('contract_id')

    def _default_tax_ids(self):
        context = self._context
        args = [('type_tax_use', '=', 'sale')]
        if context.get('default_buy', False):
            args = [('type_tax_use', '=', 'purchase')]
        return self.env['account.tax'].search(args)

    name = fields.Char(string='单号', copy=False, readonly=True, index=True, default='草稿')
    buy = fields.Boolean('购买')
    contract_name = fields.Char(string='合同实际编号', index=True, track_visibility='onchange')
    contract_date = fields.Date(string='合同实际日期', default=lambda *a: time.strftime('%Y-%m-%d'), track_visibility='onchange')
    linyan = fields.Boolean('林炎格式')
    year = fields.Char('合同年', required=True, default=lambda *a: time.strftime('%Y'))
    month = fields.Char('合同月', required=True, default=lambda *a: time.strftime('%m'))
    partner_id = fields.Many2one('res.partner', string='合同方', required=True, index=True, track_visibility='onchange')
    product_id = fields.Many2one('product.product', string='商品', required=True, index=True, track_visibility='onchange')
    model_id = fields.Many2one('linyan.model', string='型号', track_visibility='onchange')
    packaging_id = fields.Many2one('product.packaging', string='包装', track_visibility='onchange')
    brand_id = fields.Many2one('linyan.brand', string='品牌', track_visibility='onchange')
    protocol_qty = fields.Float(string='拟定数量', required=True, digits=dp.get_precision('Product Unit of Measure'), default=1.0, track_visibility='onchange')
    picking = fields.Boolean('提货完结')
    actual_qty = fields.Float(string='实际数量', required=True, digits=dp.get_precision('Product Unit of Measure'), default=1.0, track_visibility='onchange')
    currency_id = fields.Many2one('res.currency', '货币', required=True, default=lambda self: self.env['res.currency'].search([('name', '=', 'CNY')]))
    currency_rate = fields.Float('汇率', required=True)
    price = fields.Monetary(string='单价', required=True, digits=dp.get_precision('Product Price'), track_visibility='always')
    tax_ids = fields.Many2many('account.tax', 'linyan_contract_tax_rel', 'contract_id', 'tax_id', string='增值税率', default=lambda self: self._default_tax_ids())
    amount = fields.Monetary(string='金额', compute='_compute_price', store=True)
    untax_price = fields.Monetary(string='人民币税前单价', compute='_compute_price', store=True)
    account_ref = fields.Selection([('contract', '合同日'), ('move', '发货日'), ('bill', '发票日')], '账期起算参考', required=True, default='contract')
    account_date = fields.Integer('付款账期', required=True, default=-1)
    journal_id = fields.Many2one('account.journal', string='付款方式', required=True, track_visibility='onchange', default=lambda self: self.env['account.journal'].search([], limit=1))
    bill = fields.Integer('票面账期', default=0, required=True)
    payment_method = fields.Selection([('after', '月后'), ('now', '当日'), ('before', '月初')], '方式', required=True, default='now')
    days = fields.Integer('天数', required=True, default=-1)
    goods = fields.Boolean('现货')
    cash = fields.Boolean('头寸')
    big_contract = fields.Boolean('长约')
    version = fields.Integer('修正版本', required=True, readonly=True, default=0)
    contract_line = fields.One2many('linyan.contract.line', 'contract_id', '关联购买', copy=False)
    used_qty = fields.Float(string='已用数量', readonly=True, digits=dp.get_precision('Product Unit of Measure'), default=0.0)
    remaining_qty = fields.Float(string='剩余数量', compute='_get_compute_qty', store=True)
    state = fields.Selection([('draft', '发起指示'), ('sign', '合同签订'), ('moved', '履约完成'), ('paid', '付款完成'), ('done', '合同完成'), ('cancel', '取消')], '状态', default='draft', track_visibility='onchange')
    oversell = fields.Boolean('是否卖空')
    invoice_count = fields.Integer(string='发票数', compute='_compute_invoice_status', readonly=True)
    invoice_status = fields.Selection([
        ('invoiced', '已开票'),
        ('to invoice', '待开票')
        ], string='发票状态', default='to invoice')
    invoice_lines = fields.Many2many('account.invoice.line', 'linyan_contract_invoice_line_rel', 'order_line_id', 'invoice_line_id', string='发票明细', copy=False)
    qty_delivered = fields.Float(string='已转移数量', readonly=True, copy=False, digits=dp.get_precision('Product Unit of Measure'), default=0.0)
    qty_to_delivered = fields.Float(string='未提数量', readonly=True, compute='_get_qty_to_delivered', store=True)
    # qty_to_invoice = fields.Float(compute='_get_to_invoice_qty', string='需开票数量', store=True, digits=dp.get_precision('Product Unit of Measure'), default=0.0)
    # qty_invoiced = fields.Float(compute='_get_invoice_qty', string='已开票数量', store=True, digits=dp.get_precision('Product Unit of Measure'), default=0.0)
    # warehouse_id = fields.Many2one('stock.warehouse', string='仓库', required=True, readonly=True, states={'draft': [('readonly', False)]}, default=_default_warehouse_id)
    move_ids = fields.One2many('logistics.move', 'contract_id', string='物流单')
    delivery_count = fields.Integer(string='物流数量', compute='_compute_move_ids')
    company_id = fields.Many2one('res.company', '公司', readonly=True, default=lambda self: self.env['res.company']._company_default_get('linyan.contract'))
    note = fields.Text('备注')
    contract_amount = fields.Monetary('合同费用', default=0.0)
    profit = fields.Monetary('利润', readonly=True, compute='_compute_profit', store=True)
    invoice_line = fields.One2many('linyan.invoice', 'contract_id', '应收\应付', readonly=True, copy=False)
    unpayment_amount = fields.Monetary(string='未付金额', compute='_get_unpayment_amount', readonly=True, store=True)
    sell_ids = fields.Many2many('linyan.contract', string='卖出合同', compute='_compute_sell_ids', domain=[('buy', '=', False)])
    sale_contract_line = fields.One2many('linyan.sale.contract.line', 'contract_id', '关联卖出', copy=False, readonly=True)

    @api.onchange('product_id')
    def onchange_product_id(self):
        if self.product_id:
            self.brand_id = self.product_id.brand_id
            self.model_id = self.product_id.model_id
            self.packaging_id = self.product_id.packaging_id

    @api.multi
    @api.depends('name', 'product_id', 'brand_id', 'price', 'actual_qty')
    def name_get(self):
        result = []
        for contract in self:
            product_name = contract.product_id and contract.product_id.name
            brand_name = contract.brand_id and contract.brand_id.name
            name = brand_name and ':'.join((contract.name, product_name, brand_name, str(contract.actual_qty), str(contract.price))) or ':'.join((contract.name, product_name, str(contract.actual_qty), str(contract.price)))
            result.append((contract.id, name))
        return result

    @api.model
    def search(self, args, offset=0, limit=None, order=None, count=False):
        context = self._context or {}
        if context.get('product_id', False):
            args.extend([('product_id', '=', context['product_id'])])
        if context.get('partner_id', False):
            args.extend([('partner_id', '=', context['partner_id'])])
        return super(LinyanContract, self).search(args, offset, limit, order, count=count)

    @api.model
    def name_search(self, name, args=None, operator='ilike', limit=100):
        args = args or []
        context = self._context
        domain = []
        ids = []
        if context.get('contract_line', []):
            for line in context.get('contract_line'):
                if line[2] and line[2].get('buy_id', False):
                    ids.append(line[2]['buy_id'])
                elif line[1] and line[0] and line[0] == 4:
                    self._cr.execute("select buy_id from linyan_contract_line where id = %s" % line[1])
                    ids.append(self._cr.fetchone()[0])
        if name:
            product = self.env['product.product'].search(['|', ('name', operator, name), ('default_code', operator, name)])
            product_ids = product and product.ids or []
            domain = ['|', ('product_id', 'in', product_ids), ('name', operator, name)]
        contracts = self.search(domain + args, limit=limit)
        if context.get('product_id', False):
            contracts = contracts.filtered(lambda o: o.product_id.id == context.get('product_id', False) and o.id not in ids)
        return contracts.name_get()

    @api.model
    def create(self, vals):
        if vals.get('contract_line', []):
            for line in vals['contract_line']:
                buy_id = line[2]['buy_id']
                out_qty = line[2]['actual_qty']
                contract = self.browse(buy_id)
                remaining_qty = contract.remaining_qty
                contract_line = self.contract_line.search([('buy_id', '=', buy_id), ('state', '!=', 'cancel')])
                out_qty_total = out_qty + sum(contract_line.mapped('actual_qty'))
                if float_compare(out_qty, remaining_qty, 2) == 1:
                    raise UserError((u'订单号(%s)输入的卖出数量(%s)不能大于剩余数量(%s).' % (contract.name, out_qty, remaining_qty)))
                contract.write({'used_qty': out_qty_total})
        if vals.get('name', '草稿') == '草稿':
            if vals.get('buy', False):
                vals['name'] = self.env['ir.sequence'].next_by_code('linyan.contract.buy') or '草稿'
            else:
                vals['name'] = self.env['ir.sequence'].next_by_code('linyan.contract') or '草稿'
        result = super(LinyanContract, self).create(vals)
        return result

    @api.multi
    def write(self, values):
        if values:
            version = self.version + 1
        values.update({'version': version})
        if values.get('contract_line', []):
            buy_ids_qty = {}
            for line in values['contract_line']:
                if line[0] == 2:
                    line_id = line[1]
                    contract_line = self.contract_line.browse(line_id)
                    out_qty = contract_line.actual_qty
                    buy_id = contract_line.buy_id and contract_line.buy_id.id
                    buy_ids_qty.update({buy_id: out_qty})
            for line in values['contract_line']:
                if line[0] == 0:
                    buy_id = line[2]['buy_id']
                    out_qty = line[2]['actual_qty']
                    contract = self.browse(buy_id)
                    remaining_qty = contract.remaining_qty
                    contract_line = self.contract_line.search([('buy_id', '=', buy_id), ('state', '!=', 'cancel')])
                    out_qty_total = out_qty + sum(contract_line.mapped('actual_qty'))
                    if buy_id in buy_ids_qty:
                        old_out_qty = buy_ids_qty.pop(buy_id)
                        remaining_qty += old_out_qty
                        out_qty_total -= old_out_qty
                    if float_compare(out_qty, remaining_qty, 2) == 1:
                        raise UserError((u'订单号(%s)输入的卖出数量(%s)不能大于剩余数量(%s).' % (contract.name, out_qty, remaining_qty)))
                    contract.write({'used_qty': out_qty_total})

                elif line[0] == 1:
                    if line[2].get('buy_id', False):
                        new_buy_id = line[2]['buy_id']
                        line_id = line[1]
                        contract_line = self.contract_line.browse(line_id)
                        old_buy_id = contract_line.buy_id and contract_line.buy_id.id
                        out_qty = line[2].get('actual_qty', 0.0) or contract_line.actual_qty
                        new_contract_line = self.contract_line.search([('buy_id', '=', new_buy_id), ('state', '!=', 'cancel')])
                        old_contract_line = self.contract_line.search([('buy_id', '=', old_buy_id), ('state', '!=', 'cancel')])
                        new_contract = self.browse(new_buy_id)
                        old_contract = self.browse(old_buy_id)
                        remaining_qty = new_contract.remaining_qty
                        if new_buy_id == old_buy_id:
                            remaining_qty += contract_line.actual_qty
                        if float_compare(out_qty, remaining_qty, 2) == 1:
                            raise UserError((u'订单号(%s)输入的卖出数量(%s)不能大于剩余数量(%s).' % (new_contract.name, out_qty, remaining_qty)))
                        new_contract.write({'used_qty': out_qty + sum(new_contract_line.mapped('actual_qty'))})
                        old_contract.write({'used_qty': sum(old_contract_line.mapped('actual_qty')) - contract_line.actual_qty})
                    elif line[2].get('actual_qty', 0.0):
                        line_id = line[1]
                        out_qty = line[2]['actual_qty']
                        contract_line = self.contract_line.browse(line_id)
                        buy_id = contract_line.buy_id and contract_line.buy_id.id
                        old_out_qty = contract_line.actual_qty
                        remaining_qty = contract_line.buy_id and contract_line.buy_id.remaining_qty
                        remaining_qty += old_out_qty
                        contract_line2 = self.contract_line.search([('buy_id', '=', buy_id), ('state', '!=', 'cancel')])
                        out_qty_total = out_qty + sum(contract_line2.mapped('actual_qty')) - old_out_qty
                        if float_compare(out_qty, remaining_qty, 2) == 1:
                            raise UserError((u'订单号(%s)输入的卖出数量(%s)不能大于剩余数量(%s).' % (contract_line.buy_id.name, out_qty, remaining_qty)))
                        contract_line.buy_id.write({'used_qty': out_qty_total})
                    else:
                        pass
                else:
                    pass
            if buy_ids_qty:
                for buy_id, out_qty in buy_ids_qty.items():
                    contract = self.browse(buy_id)
                    contract_line = self.contract_line.search([('buy_id', '=', buy_id), ('state', '!=', 'cancel')])
                    out_qty_total = sum(contract_line.mapped('actual_qty')) - out_qty
                    contract.write({'used_qty': out_qty_total})
        if 'price' in values:
            self.update_invoice_amount(values['price'])
        return super(LinyanContract, self).write(values)

    @api.multi
    def unlink(self):
        for o in self:
            for line in o.contract_line:
                actual_qty = line.actual_qty
                used_qty = line.buy_id.used_qty
                line.buy_id.write({'used_qty': used_qty - actual_qty})
            if o.buy and o.sell_ids:
                raise UserError(('此单据已关联卖出合同，不能直接删除。'))
            if not o.buy and o.contract_line:
                raise UserError(('此单据已关联买入合同，不能直接删除。'))
            if o.move_ids:
                raise UserError(('此单据已关联物流，不能直接删除。'))
            if o.invoice_line:
                raise UserError(('此单据已关联应收应付账款，不能直接删除。'))
        return super(LinyanContract, self).unlink()

    @api.onchange('buy')
    def _onchange_buy(self):
        if self.buy:
            return {'domain': {'partner_id': [('supplier', '=', True), ('is_company', '=', True)], 'tax_ids': [('type_tax_use', '=', 'purchase')]}}
        else:
            return {'domain': {'partner_id': [('customer', '=', True), ('is_company', '=', True)], 'tax_ids': [('type_tax_use', '=', 'sale')]}}

    # @api.onchange('actual_qty')
    # def _onchange_actual_qty(self):
    #     if self.actual_qty:
    #         self.protocol_qty = self.actual_qty

    @api.onchange('contract_line', 'oversell')
    def _onchange_contract_line(self):
        if self.contract_line:
            self.product_id = self.contract_line[0].product_id
            self.model_id = self.contract_line[0].model_id
            self.packaging_id = self.contract_line[0].packaging_id
            self.brand_id = self.contract_line[0].brand_id
        # if not self.oversell:
        #     self.actual_qty = sum(self.contract_line.mapped('actual_qty'))
        # else:
        #     self.actual_qty = 0.0

    # @api.model
    # def fields_view_get(self, view_id=None, view_type='form', toolbar=False, submenu=False):
    #     res = super(LinyanContract, self).fields_view_get(view_id=view_id, view_type=view_type, toolbar=toolbar, submenu=False)
    #     if view_type == 'form' and self._context.get('default_buy', False):
    #         doc = etree.XML(res['arch'])
    #         for node in doc.xpath("//field[@name='product_id']"):
    #             node.set("modifiers", json.dumps({'required': True}))
    #         for node in doc.xpath("//field[@name='supplierinfo_id']"):
    #             node.set("modifiers", json.dumps({'required': True}))
    #         for node in doc.xpath("//field[@name='packaging_id']"):
    #             node.set("modifiers", json.dumps({'required': True}))
    #         res['arch'] = etree.tostring(doc)
    #     return res

    @api.onchange('currency_id')
    def _onchange_currency_id(self):
        if self.currency_id:
            self.currency_rate = self.currency_id.rate

    @api.model
    def _get_warehouse_id(self, partner_id):
        warehouse_ids = self.env['stock.warehouse'].search([('partner_id', '=', partner_id)], limit=1)
        return warehouse_ids

    @api.multi
    def _create_picking(self):
        for o in self:
            warehouse_src_id = warehouse_dest_id = False
            move_out = move_in = False
            if o.buy:
                move_in = True
                partner_id = o.partner_id.id
                warehouse_ids = self._get_warehouse_id(partner_id)
                warehouse_src_id = warehouse_ids and warehouse_ids.id or False
                # partner_id2 = o.company_id and o.company_id.partner_id.id
                # warehouse_ids2 = self._get_warehouse_id(partner_id2)
                # warehouse_dest_id = warehouse_ids2 and warehouse_ids2.id or False
                warehouse_dest_id = self.warehouse_id and self.warehouse_id.id or False
            else:
                move_out = True
                partner_id = o.partner_id.id
                warehouse_ids = self._get_warehouse_id(partner_id)
                warehouse_dest_id = warehouse_ids and warehouse_ids.id or False
                # partner_id2 = o.company_id and o.company_id.partner_id.id
                # warehouse_ids2 = self._get_warehouse_id(partner_id2)
                # warehouse_src_id = warehouse_ids2 and warehouse_ids2.id or False
                warehouse_src_id = self.warehouse_id and self.warehouse_id.id or False
            values = {
                'partner_id': o.partner_id.id,
                'contract_id': o.id,
                'origin': o.name,
                'warehouse_src_id': warehouse_src_id,
                'warehouse_dest_id': warehouse_dest_id,
                'product_id': o.product_id.id,
                'tax_ids': [(6, 0, o.tax_ids.ids)],
                'untax_price': o.untax_price,
                'protocol_qty': o.actual_qty,
                'actual_qty': o.actual_qty,
                'move_out': move_out,
                'move_in': move_in
            }
            self.env['logistics.move'].create(values)
        return True

    @api.multi
    def action_done(self):
        for o in self:
            o.write({'state': 'done'})

    @api.multi
    def action_sign(self):
        for o in self:
            if o.state not in ['draft']:
                continue
            o.write({'state': 'sign'})
            # o._create_picking()
        return True

    @api.multi
    def action_moved(self):
        for o in self:
            o.write({'state': 'moved', 'picking': True})
            # if o.invoice_status == 'invoiced':
            #     o.action_done()

    @api.multi
    def action_paid(self):
        for o in self:
            o.write({'state': 'paid', 'invoice_status': 'invoiced'})
            # if o.picking:
            #     o.action_done()

    @api.multi
    def _get_invoice_date(self, start=None):
        self.ensure_one()
        if not start:
            start = time.strftime('%Y-%m-%d')
        end = time.strftime('%Y-%m-%d')
        if self.account_ref == 'contract':
            start = self.contract_date or start
        # elif self.account_ref == 'move':
        #     if self.picking:
        #         move = self.env['logistics.move'].search([('contract_id', '=', self.id), ('state', '=', 'plan')], order="date_done desc", limit=1)
        #         start = move.date_done
        #     else:
        #         raise UserError(('基于物流单开发票请先完成提货。'))
        else:
            pass
        if len(start) > 10:
            start = start[:10]
        if self.payment_method == 'after':
            end = datetime.strptime(start, "%Y-%m-%d") + relativedelta(day=1, months=1, days=self.days - 1)
        elif self.payment_method == 'before':
            end = datetime.strptime(start, "%Y-%m-%d") + relativedelta(day=1, days=self.days)
        else:
            pass
        return end

    @api.multi
    def _prepare_invoice(self):
        self.ensure_one()
        invoice_vals = {
            'contract_id': self.id,
            'origin': self.name,
            'invoice_type': 'out_invoice',
            'partner_id': self.partner_id.id,
            'journal_id': self.journal_id.id,
            'currency_id': self.currency_id.id,
            'comment': self.note,
            'company_id': self.company_id.id,
            'user_id': self.write_uid and self.write_uid.id,
            # 'date_due': self._get_invoice_date(),
            'tax_ids': [(6, 0, self.tax_ids.ids)],
            'price': self.price,
            'untax_price': self.untax_price,
        }
        if self.buy:
            invoice_vals.update({
                'invoice_type': 'in_invoice'})
        return invoice_vals

    @api.multi
    def _prepare_invoice_line(self, qty):
        self.ensure_one()
        res = {}
        account = self.product_id.property_account_income_id or self.product_id.categ_id.property_account_income_categ_id
        if self.buy:
            account = self.product_id.property_account_expense_id or self.product_id.categ_id.property_account_expense_categ_id
        if not account:
            raise UserError(('Please define income account for this product: "%s" (id:%d) - or for its category: "%s".') % (self.product_id.name, self.product_id.id, self.product_id.categ_id.name))

        res = {
            'name': self.name,
            'origin': self.name,
            'account_id': account.id,
            'price_unit': self.price,
            'quantity': qty,
            'product_id': self.product_id.id or False,
            'invoice_line_tax_ids': [(6, 0, self.tax_ids.ids)],
        }
        return res

    @api.multi
    def invoice_line_create(self, invoice_id, qty):
        precision = self.env['decimal.precision'].precision_get('Product Unit of Measure')
        for o in self:
            if not float_is_zero(qty, precision_digits=precision):
                vals = o._prepare_invoice_line(qty=qty)
                vals.update({'invoice_id': invoice_id, 'contract_ids': [(6, 0, [o.id])]})
                self.env['account.invoice.line'].create(vals)

    @api.multi
    def action_invoice_create(self):
        inv_obj = self.env['account.invoice']
        precision = self.env['decimal.precision'].precision_get('Product Unit of Measure')
        for o in self:
            if float_is_zero(o.qty_to_invoice, precision_digits=precision):
                continue
            inv_data = o._prepare_invoice()
            invoice = inv_obj.create(inv_data)
            o.invoice_line_create(invoice.id, o.qty_to_invoice)
            invoice.compute_taxes()
            if o._context.get('open_invoices', False):
                return o.action_view_invoice()
        return {'type': 'ir.actions.act_window_close'}

    @api.multi
    def action_view_invoice(self):
        invoice_ids = self.mapped('invoice_lines.invoice_id')
        imd = self.env['ir.model.data']
        action = imd.xmlid_to_object('account.action_invoice_tree1')
        list_view_id = imd.xmlid_to_res_id('account.invoice_tree')
        form_view_id = imd.xmlid_to_res_id('account.invoice_form')
        if self.buy:
            action = imd.xmlid_to_object('account.action_invoice_tree2')
            list_view_id = imd.xmlid_to_res_id('account.invoice_supplier_tree')
            form_view_id = imd.xmlid_to_res_id('account.invoice_supplier_form')

        result = {
            'name': action.name,
            'type': action.type,
            'views': [[list_view_id, 'tree'], [form_view_id, 'form']],
            'target': action.target,
            'context': action.context,
            'res_model': action.res_model,
        }
        if len(invoice_ids) > 1:
            result['domain'] = "[('id','in',%s)]" % invoice_ids.ids
        elif len(invoice_ids) == 1:
            result['views'] = [(form_view_id, 'form')]
            result['res_id'] = invoice_ids.ids[0]
        else:
            result = {'type': 'ir.actions.act_window_close'}
        return result

    @api.multi
    def action_view_delivery(self):
        action = self.env.ref('linyan_contract.action_view_linyan_logistics_move')

        result = {
            'name': action.name,
            'type': action.type,
            'view_type': action.view_type,
            'view_mode': action.view_mode,
            'target': action.target,
            'context': action.context,
            'res_model': action.res_model,
        }
        move_ids = sum([o.move_ids.ids for o in self], [])
        if len(move_ids) > 1:
            result['domain'] = "[('id','in',["+','.join(map(str, move_ids))+"])]"
        elif len(move_ids) == 1:
            form = self.env.ref('linyan_contract.view_logistics_move_form', False)
            form_id = form.id if form else False
            result['views'] = [(form_id, 'form')]
            result['res_id'] = move_ids[0]
        return result

    @api.multi
    def update_invoice_amount(self, update_price=0.0):
        cr = self._cr
        inv_obj = self.env['linyan.invoice']
        for o in self:
            update_untax_price = o.tax_ids.compute_all(update_price, o.currency_id, 1.0, product=o.product_id or False, partner=o.partner_id)['total_excluded']
            price = o.price
            untax_price = o.untax_price
            difference = abs(update_price - price)
            difference_untax_price = abs(update_untax_price - untax_price)
            if o.buy:
                inv_data = o._prepare_invoice()
                date_due = o._get_invoice_date()
                price = inv_data.pop('price')
                untax_price = inv_data.pop('untax_price')
                actual_qty = 0.0
                cr.execute("select sum(actual_qty) from logistics_move where state = 'done' and contract_id = %s" % o.id)
                actual_qty = cr.fetchone()[0]
                if not actual_qty:
                    continue
                if update_price - price > 0:
                    inv_data.update({'invoice_type': 'in_invoice'})
                else:
                    inv_data.update({'invoice_type': 'out_invoice'})
                inv_data.update({'amount_untaxed': difference_untax_price * actual_qty, 'amount_total': difference * actual_qty, 'date_due': date_due})
                inv_obj.create(inv_data)
            else:
                inv_data = o._prepare_invoice()
                date_due = o._get_invoice_date()
                price = inv_data.pop('price')
                untax_price = inv_data.pop('untax_price')
                actual_qty = 0.0
                cr.execute("select sum(actual_qty) from logistics_move where state = 'done' and contract_id2 = %s" % o.id)
                actual_qty = cr.fetchone()[0]
                if not actual_qty:
                    continue
                if update_price - price > 0:
                    inv_data.update({'invoice_type': 'out_invoice'})
                else:
                    inv_data.update({'invoice_type': 'in_invoice'})
                inv_data.update({'amount_untaxed': difference_untax_price * actual_qty, 'amount_total': difference * actual_qty, 'date_due': date_due})
                inv_obj.create(inv_data)
        return True


class LinyanContractLine(models.Model):
    _name = "linyan.contract.line"

    contract_id = fields.Many2one('linyan.contract', '关联卖出', ondelete='cascade')
    buy_id = fields.Many2one('linyan.contract', '关联合同', required=True, domain="[('buy', '=', True), ('state', '!=', 'cancel'), ('remaining_qty', '>', 0.0), ('product_id', '=', product_id)]")
    # product_id = fields.Many2one('product.product', related='buy_id.product_id', string='商品', readonly=True, store=True, index=True)
    product_id = fields.Many2one('product.product', string='商品', required=True)
    model_id = fields.Many2one('linyan.model', '型号')
    packaging_id = fields.Many2one('product.packaging', '包装')
    brand_id = fields.Many2one('linyan.brand', '品牌')
    currency_id = fields.Many2one('res.currency', string='货币', related='buy_id.currency_id')
    price = fields.Monetary(string='单价', related='buy_id.price', readonly=True, store=True, digits=dp.get_precision('Product Price'))
    relation_qty = fields.Float(string='买入数量', related='buy_id.actual_qty', readonly=True, store=True)
    actual_qty = fields.Float('卖出数量', required=True, digits=dp.get_precision('Product Unit of Measure'))
    used_qty = fields.Float(string='已用数量', related='buy_id.used_qty', readonly=True)
    remaining_qty = fields.Float(string='剩余数量', related='buy_id.remaining_qty', readonly=True)
    state = fields.Selection([('draft', '发起指示'), ('sign', '合同签订'), ('done', '合同完成'), ('cancel', '取消')], string='状态', related='contract_id.state', readonly=True, store=True)

    @api.onchange('buy_id')
    def _onchange_buy_id(self):
        if self.buy_id:
            self.product_id = self.buy_id.product_id
            self.model_id = self.buy_id.model_id
            self.packaging_id = self.buy_id.packaging_id
            self.brand_id = self.buy_id.brand_id
            self.relation_qty = self.buy_id.actual_qty
            self.used_qty = self.buy_id.used_qty
            self.remaining_qty = self.buy_id.remaining_qty
            self.contract_id.model_id = self.buy_id.model_id
            self.contract_id.packaging_id = self.buy_id.packaging_id
            self.contract_id.brand_id = self.buy_id.brand_id

    @api.model
    def create(self, vals):
        sale_id = vals.get('contract_id', False)
        buy_id = vals.get('buy_id', False)
        actual_qty = vals.get('actual_qty', False)
        self.env['linyan.sale.contract.line'].create({'contract_id': buy_id, 'sale_id': sale_id, 'relation_qty': actual_qty})
        return super(LinyanContractLine, self).create(vals)

    @api.multi
    def write(self, values):
        if values.get('actual_qty', 0.0):
            sale_contract_line = self.env['linyan.sale.contract.line'].search([('contract_id', '=', self.buy_id.id), ('sale_id', '=', self.contract_id.id)])
            sale_contract_line.write({'relation_qty': values['actual_qty']})
        return super(LinyanContractLine, self).write(values)

    @api.multi
    def unlink(self):
        sale_contract_line = self.env['linyan.sale.contract.line'].search([('contract_id', '=', self.buy_id.id), ('sale_id', '=', self.contract_id.id)])
        sale_contract_line.unlink()
        return super(LinyanContractLine, self).unlink()


class LinyanSaleContractSaleLine(models.Model):
    _name = "linyan.sale.contract.line"

    @api.depends('sale_id', 'sale_id.actual_qty', 'sale_id.remaining_qty')
    def _get_compute_qty(self):
        for o in self:
            o.actual_qty = o.sale_id.actual_qty - o.sale_id.remaining_qty

    contract_id = fields.Many2one('linyan.contract', '关联合同', ondelete='cascade')
    sale_id = fields.Many2one('linyan.contract', '关联卖出', readonly=True)
    product_id = fields.Many2one('product.product', related='sale_id.product_id', string='商品', readonly=True, store=True)
    model_id = fields.Many2one('linyan.model', related='sale_id.model_id', string='型号', readonly=True, store=True)
    packaging_id = fields.Many2one('product.packaging', related='sale_id.packaging_id', string='包装', readonly=True, store=True)
    brand_id = fields.Many2one('linyan.brand', related='sale_id.brand_id', string='品牌', readonly=True, store=True)
    currency_id = fields.Many2one('res.currency', string='货币', related='sale_id.currency_id', readonly=True, store=True)
    price = fields.Monetary(string='销售单价', readonly=True, related='sale_id.price', store=True, digits=dp.get_precision('Product Price'))
    untax_price = fields.Monetary(string='人民币税前单价', related='sale_id.untax_price', readonly=True, store=True)
    contract_qty = fields.Float('合同数量', related='sale_id.actual_qty', readonly=True, store=True)
    relation_qty = fields.Float('关联数量', readonly=True)
    actual_qty = fields.Float('已关联数量', compute='_get_compute_qty', readonly=True, store=True)


class LogisticsMove(models.Model):
    _name = "logistics.move"
    _inherit = ["mail.thread", "ir.needaction_mixin"]
    _order = 'create_date desc, id desc'

    name = fields.Char(string='单号', copy=False, readonly=True, index=True, default='草稿')
    move_out = fields.Boolean('出库', readonly=True, states={'draft': [('readonly', False)]})
    move_in = fields.Boolean('入库', readonly=True, states={'draft': [('readonly', False)]})
    contract_id = fields.Many2one('linyan.contract', '买入合同', readonly=True, states={'draft': [('readonly', False)]}, domain=[('buy', '=', True), ('picking', '=', False)], track_visibility='onchange')
    contract_id2 = fields.Many2one('linyan.contract', '卖出合同', readonly=True, states={'draft': [('readonly', False)]}, domain=[('buy', '=', False), ('picking', '=', False)], track_visibility='onchange')
    partner_id = fields.Many2one('res.partner', string='业务伙伴', readonly=True, states={'draft': [('readonly', False)]}, track_visibility='onchange')
    partner_id2 = fields.Many2one('res.partner', string='业务伙伴', readonly=True, states={'draft': [('readonly', False)]}, track_visibility='onchange')
    ref = fields.Char('参考编号')
    origin = fields.Char('源单据', readonly=True, states={'draft': [('readonly', False)]})
    date_done = fields.Datetime(string='完成日期', copy=False, track_visibility='onchange')
    date_done2 = fields.Datetime(string='完成日期', copy=False, track_visibility='onchange')
    date = fields.Datetime('计划日期', readonly=True, states={'draft': [('readonly', False)]}, default=fields.Datetime.now)
    date2 = fields.Datetime('计划日期', readonly=True, states={'draft': [('readonly', False)]}, default=fields.Datetime.now)
    tax_ids = fields.Many2many('account.tax', 'logistics_move_tax_rel', 'logistics_id', 'tax_id', string='增值税率', readonly=True, states={'draft': [('readonly', False)]}, copy=True)
    untax_price = fields.Float(string='税前运输单价', required=True, readonly=True, states={'draft': [('readonly', False)]}, track_visibility='onchange')
    trasport = fields.Boolean('运输责任')
    trasport_user = fields.Char('承运人')
    trasport_price = fields.Float('人民币运输单价')
    protocol_qty = fields.Float(string='计划数量', required=True, readonly=True, states={'draft': [('readonly', False)]}, track_visibility='onchange')
    actual_qty = fields.Float(string='实际数量', required=True, readonly=False, states={'done': [('readonly', True)]}, track_visibility='onchange')
    product_id = fields.Many2one('product.product', string='商品', required=True, readonly=True, states={'draft': [('readonly', False)]}, track_visibility='onchange')
    is_risk = fields.Boolean('风险业务')
    state = fields.Selection([('draft', '计划'), ('plan', '执行中'), ('done', '完成'), ('cancel', '取消')], string='状态', readonly=True, default='draft', copy=False, track_visibility='onchange')
    warehouse_src_id = fields.Many2one('stock.warehouse', string='源仓库', required=True, readonly=True, states={'draft': [('readonly', False)]})
    warehouse_dest_id = fields.Many2one('stock.warehouse', string='目标仓库', required=True, readonly=True, states={'draft': [('readonly', False)]})
    warehouse_addr = fields.Char('仓库地址')
    warehouse_addr2 = fields.Char('仓库地址')
    company_id = fields.Many2one('res.company', '公司', readonly=True, default=lambda self: self.env['res.company']._company_default_get('logistics.move'))
    brand_id = fields.Many2one('linyan.brand', string='品牌', track_visibility='onchange')
    model_id = fields.Many2one('linyan.model', string='规格型号', track_visibility='onchange')

    @api.onchange('contract_id', 'contract_id2')
    def _onchange_contract(self):
        if self.contract_id:
            self.partner_id = self.contract_id.partner_id
            if not self.product_id:
                self.product_id = self.contract_id.product_id
                self.brand_id = self.contract_id.brand_id
                self.model_id = self.contract_id.model_id
        if self.contract_id2:
            self.partner_id2 = self.contract_id2.partner_id
            if not self.product_id:
                self.product_id = self.contract_id2.product_id
                self.brand_id = self.contract_id2.brand_id
                self.model_id = self.contract_id2.model_id

    @api.model
    def create(self, vals):
        if vals.get('name', '草稿') == '草稿':
                vals['name'] = self.env['ir.sequence'].next_by_code('logistics.move') or '草稿'
        result = super(LogisticsMove, self).create(vals)
        return result

    @api.multi
    def unlink(self):
        for move in self:
            invoice = self.env['linyan.invoice'].search([('move_id', '=', move.id)])
            invoice.unlink()
        return super(LogisticsMove, self).unlink()

    @api.multi
    def action_plan(self):
        for o in self:
            o.filtered(lambda s: s.state == 'draft').write({'state': 'plan'})
            o.action_invoice_create()
            if o.contract_id:
                buy_plan_qty = self.get_buy_plan_qty()
                o.contract_id.write({'qty_delivered': buy_plan_qty})
            if o.contract_id2:
                sell_plan_qty = self.get_sell_plan_qty()
                o.contract_id2.write({'qty_delivered': sell_plan_qty})

    @api.multi
    def action_done(self):
        for o in self:
            o.filtered(lambda s: s.state == 'plan').write({'state': 'done'})
            o.action_difference_invoice_create()
            if o.contract_id:
                buy_done_qty = self.get_buy_done_qty()
                o.contract_id.write({'qty_delivered': buy_done_qty})
            if o.contract_id2:
                sell_done_qty = self.get_sell_done_qty()
                o.contract_id2.write({'qty_delivered': sell_done_qty})

    @api.multi
    def action_cancel(self):
        for o in self:
            o.filtered(lambda s: s.state == 'draft').write({'state': 'cancel'})
            # if o.contract_id:
            #     all_qty = self.get_all_qty()
            #     if o.contract_id.actual_qty == all_qty:
            #         o.contract_id.write({'picking': True})
            #         o.contract_id.action_moved()
            #         if o.contract_id.state == 'paid':
            #             o.contract_id.action_done()

    @api.multi
    def get_buy_plan_qty(self):
        cr = self._cr
        contract_id = self.contract_id.id
        cr.execute("select sum(protocol_qty) from logistics_move where state != 'cancel' and contract_id = %s" % contract_id)
        result = cr.fetchone()[0]
        return result

    @api.multi
    def get_buy_done_qty(self):
        cr = self._cr
        contract_id = self.contract_id.id
        cr.execute("select sum(actual_qty) from logistics_move where state = 'done' and contract_id = %s" % contract_id)
        result = cr.fetchone()[0]
        return result

    @api.multi
    def get_sell_plan_qty(self):
        cr = self._cr
        contract_id = self.contract_id2.id
        cr.execute("select sum(protocol_qty) from logistics_move where state = 'done' and contract_id2 = %s" % contract_id)
        result = cr.fetchone()[0]
        return result

    @api.multi
    def get_sell_done_qty(self):
        cr = self._cr
        contract_id = self.contract_id2.id
        cr.execute("select sum(actual_qty) from logistics_move where state = 'done' and contract_id2 = %s" % contract_id)
        result = cr.fetchone()[0]
        return result

    @api.multi
    def get_all_qty(self):
        cr = self._cr
        origin = self.origin
        cr.execute("select sum(actual_qty) from logistics_move where state in ('done', 'cancel') and origin = '%s'" % origin)
        result = cr.fetchone()[0]
        return result

    @api.multi
    def get_remaining_qty(self):
        cr = self._cr
        origin = self.origin
        cr.execute("select sum(actual_qty) from logistics_move where state = 'done' and origin = '%s'" % origin)
        done_qty = cr.fetchone()[0]
        result = self.contract_id.actual_qty - done_qty
        return result

    @api.multi
    def action_invoice_create(self):
        inv_obj = self.env['linyan.invoice']
        for o in self:
            if o.contract_id:
                inv_data = o.contract_id._prepare_invoice()
                date_due = o.contract_id._get_invoice_date(start=o.date_done)
                price = inv_data.pop('price')
                untax_price = inv_data.pop('untax_price')
                inv_data.update({'move_id': o.id, 'amount_untaxed': o.protocol_qty * untax_price, 'amount_total': o.protocol_qty * price, 'date_due': date_due})
                inv_obj.create(inv_data)
                # o.contract_id.invoice_line_create(invoice.id, o.protocol_qty)
                # invoice.compute_taxes()
            if o.contract_id2:
                inv_data = o.contract_id2._prepare_invoice()
                date_due = o.contract_id2._get_invoice_date(start=o.date_done2)
                price = inv_data.pop('price')
                untax_price = inv_data.pop('untax_price')
                inv_data.update({'move_id': o.id, 'amount_untaxed': o.protocol_qty * untax_price, 'amount_total': o.protocol_qty * price, 'date_due': date_due})
                inv_obj.create(inv_data)
                # o.contract_id2.invoice_line_create(invoice.id, o.protocol_qty)
                # invoice.compute_taxes()
        return True

    @api.multi
    def action_difference_invoice_create(self):
        inv_obj = self.env['linyan.invoice']
        protocol_qty = self.protocol_qty
        actual_qty = self.actual_qty
        difference = abs(protocol_qty - actual_qty)
        if self.contract_id and difference:
            inv_data = self.contract_id._prepare_invoice()
            date_due = self.contract_id._get_invoice_date(start=self.date_done)
            price = inv_data.pop('price')
            untax_price = inv_data.pop('untax_price')
            if protocol_qty - actual_qty > 0:
                inv_data.update({'invoice_type': 'out_invoice'})
            else:
                inv_data.update({'invoice_type': 'in_invoice'})
            inv_data.update({'move_id': self.id, 'amount_untaxed': difference * untax_price, 'amount_total': difference * price, 'date_due': date_due})
            inv_obj.create(inv_data)
        if self.contract_id2 and difference:
            inv_data = self.contract_id2._prepare_invoice()
            date_due = self.contract_id2._get_invoice_date(start=self.date_done2)
            price = inv_data.pop('price')
            untax_price = inv_data.pop('untax_price')
            if protocol_qty - actual_qty > 0:
                inv_data.update({'invoice_type': 'in_invoice'})
            else:
                inv_data.update({'invoice_type': 'out_invoice'})
            inv_data.update({'move_id': self.id, 'amount_untaxed': difference * untax_price, 'amount_total': difference * price, 'date_due': date_due})
            inv_obj.create(inv_data)
        return True


class AccountInvoiceLine(models.Model):
    _inherit = 'account.invoice.line'

    contract_ids = fields.Many2many('linyan.contract', 'linyan_contract_invoice_line_rel', 'invoice_line_id', 'order_line_id', string='合同', readonly=True, copy=False)


class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    contract_id = fields.Many2one('linyan.contract', '合同', readonly=True, states={'draft': [('readonly', False)]})

    @api.model
    def create(self, vals):
        if not vals.get('name', ''):
            if self._context.get('type', False) or vals.get('type', False) == 'out_invoice':
                vals['name'] = self.env['ir.sequence'].next_by_code('account.invoice.out')
            else:
                vals['name'] = self.env['ir.sequence'].next_by_code('account.invoice.in')
        invoice = super(AccountInvoice, self.with_context(mail_create_nolog=True)).create(vals)
        return invoice

    # @api.multi
    # def confirm_paid(self):
    #     if self.origin:
    #         contract = self.env['linyan.contract'].search([('name', '=', self.origin)])
    #         if not contract.qty_to_invoice:
    #             contract.action_paid()
    #             if contract.state in ('moved', 'paid'):
    #                 contract.action_done()
    #     return super(AccountInvoice, self).confirm_paid()


class AccountPayment(models.Model):
    _inherit = 'account.payment'

    face_date = fields.Date(string='票面到账期', copy=False)


class StockWarehouse(models.Model):
    _inherit = 'stock.warehouse'

    is_ower = fields.Boolean('本公司仓库')


class LinyanInvoice(models.Model):
    _name = 'linyan.invoice'
    _inherit = ['mail.thread']
    _description = u'林炎流水帐应收应付'
    _order = 'date_invoice desc, id desc'

    @api.one
    @api.depends('amount_total', 'invoice_line', 'invoice_line.used_amount')
    def _compute_residual(self):
        payment_amount = sum(self.mapped('invoice_line').mapped('used_amount'))
        self.residual = self.amount_total - payment_amount

    name = fields.Char(string='单号', index=True, copy=False)
    origin = fields.Char(string='源单据')
    contract_id = fields.Many2one('linyan.contract', '合同')
    move_id = fields.Many2one('logistics.move', '提货单')
    product_id = fields.Many2one('product.product', string='商品', related='contract_id.product_id', store=True)
    invoice_type = fields.Selection([
        ('out_invoice', '客户发票'),
        ('in_invoice', '供应商发票')], readonly=True, index=True, change_default=True,
        default=lambda self: self._context.get('type', 'out_invoice'),
        track_visibility='always')
    date_invoice = fields.Date(string='日期', index=True, copy=False, default=lambda *a: time.strftime('%Y-%m-%d'))
    date_due = fields.Date(string='截止日期', index=True, copy=False)
    partner_id = fields.Many2one('res.partner', string='业务伙伴', change_default=True, required=True, track_visibility='always')
    date = fields.Date(string='发票日期', copy=False)
    tax_ids = fields.Many2many('account.tax', 'linyan_invoice_tax_rel', 'invoice_id', 'tax_id', string='增值税率', copy=True)
    journal_id = fields.Many2one('account.journal', string='付款方式', required=True)
    amount_untaxed = fields.Monetary(string='不含税金额', readonly=True, track_visibility='always')
    amount_total = fields.Monetary(string='金额', readonly=True, track_visibility='always')
    currency_id = fields.Many2one('res.currency', '货币')
    company_id = fields.Many2one('res.company', '公司', default=lambda self: self.env['res.company']._company_default_get('linyan.invoice'))
    residual = fields.Monetary(string='未付余额', compute='_compute_residual', store=True)
    user_id = fields.Many2one('res.users', string='创建人', track_visibility='onchange', default=lambda self: self.env.user)
    comment = fields.Text('备注')
    # payment_ids = fields.Many2many('linyan.payment', 'linyan_invoice_payment_rel', 'invoice_id', 'payment_id', string="实收\实付", copy=False, readonly=True)
    invoice_line = fields.One2many('linyan.invoice.line', 'invoice_id', '实收\实付')

    @api.model
    def create(self, vals):
        if not vals.get('name', ''):
            if self._context.get('type', False) or vals.get('type', False) == 'out_invoice':
                vals['name'] = self.env['ir.sequence'].next_by_code('account.invoice.out')
            else:
                vals['name'] = self.env['ir.sequence'].next_by_code('account.invoice.in')
        invoice = super(LinyanInvoice, self.with_context(mail_create_nolog=True)).create(vals)
        return invoice

    @api.multi
    def unlink(self):
        for invoice in self:
            if invoice.invoice_line:
                raise UserError(('此单据已有关联实收实付，不能直接删除。'))
        return super(LinyanInvoice, self).unlink()


class LinyanInvoiceLine(models.Model):
    _name = 'linyan.invoice.line'

    invoice_id = fields.Many2one('linyan.invoice', 'Ref', ondelete='cascade')
    payment_id = fields.Many2one('linyan.payment', '实收\实付', required=True, domain="[('remaining_amount', '>', 0.0), ('payment_type', '=', {'out_invoice': 'inbound', 'in_invoice': 'outbound'}.get(parent.invoice_type, ''))]")
    journal_id = fields.Many2one('account.journal', string='付款方式', related='payment_id.journal_id', readonly=True, store=True)
    payment_date = fields.Date(string='日期', related='payment_id.payment_date', readonly=True, store=True)
    amount = fields.Monetary(string='金额', related='payment_id.amount', readonly=True, store=True)
    used_amount = fields.Monetary(string='使用金额', required=True)
    remaining_amount = fields.Monetary(string='剩余金额', related='payment_id.remaining_amount', readonly=True, store=True)
    currency_id = fields.Many2one('res.currency', string='币制', related='payment_id.currency_id', readonly=True, store=True)


class LinyanAbstractPayment(models.AbstractModel):
    _name = "linyan.abstract.payment"

    payment_type = fields.Selection([('outbound', '发钱'), ('inbound', '收钱')], string='类型', required=True)
    partner_type = fields.Selection([('customer', '客户'), ('supplier', '供应商')])
    partner_id = fields.Many2one('res.partner', string='业务伙伴')
    amount = fields.Monetary(string='金额', required=True)
    currency_id = fields.Many2one('res.currency', string='币制', required=True, default=lambda self: self.env.user.company_id.currency_id)
    payment_date = fields.Date(string='日期', default=lambda *a: time.strftime('%Y-%m-%d'), required=True, copy=False)
    communication = fields.Char(string='备注')
    journal_id = fields.Many2one('account.journal', string='付款方式', required=True, domain=[('type', 'in', ('bank', 'cash'))])
    company_id = fields.Many2one('res.company', related='journal_id.company_id', string='Company', readonly=True)


class LinyanPayment(models.Model):
    _name = "linyan.payment"
    _inherit = ['linyan.abstract.payment', 'mail.thread']
    _description = "Payments"
    _order = "payment_date desc, name desc"

    # @api.one
    # @api.depends('invoice_ids')
    # def _get_has_invoices(self):
    #     self.has_invoices = bool(self.invoice_ids)

    @api.one
    @api.depends('amount', 'invoice_line.used_amount')
    def _get_used_amount(self):
        used_amount = sum(self.mapped('invoice_line').mapped('used_amount'))
        self.used_amount = used_amount
        self.remaining_amount = self.amount - used_amount

    @api.one
    @api.depends('invoice_line')
    def _compute_invoices(self):
        self.invoice_ids = self.invoice_line.mapped('invoice_id')

    name = fields.Char(readonly=True, copy=False, string='单号', default="New")
    payment_type = fields.Selection(selection_add=[('transfer', 'Internal Transfer')], string='类型')
    invoice_ids = fields.Many2many('linyan.invoice', string="应收\应付", compute='_compute_invoices', store=True, readonly=True)
    face_date = fields.Date(string='票面到账期', copy=False, default=lambda *a: time.strftime('%Y-%m-%d'))
    # has_invoices = fields.Boolean(compute="_get_has_invoices", help="Technical field used for usability purposes")
    used_amount = fields.Monetary(string='使用金额', compute="_get_used_amount", readonly=True, store=True, track_visibility='onchange')
    remaining_amount = fields.Monetary(string='剩余金额', compute="_get_used_amount", readonly=True, store=True, track_visibility='onchange')
    invoice_line = fields.One2many('linyan.invoice.line', 'payment_id', '明细')

    # @api.model
    # def default_get(self, fields):
    #     rec = super(LinyanPayment, self).default_get(fields)
    #     invoice_defaults = self.resolve_2many_commands('invoice_ids', rec.get('invoice_ids'))
    #     if invoice_defaults and len(invoice_defaults) == 1:
    #         invoice = invoice_defaults[0]
    #         rec['communication'] = invoice['name']
    #         rec['currency_id'] = invoice['currency_id'][0]
    #         rec['payment_type'] = invoice['invoice_type'] == 'out_invoice' and 'inbound' or 'outbound'
    #         rec['partner_type'] = MAP_INVOICE_TYPE_PARTNER_TYPE[invoice['invoice_type']]
    #         rec['partner_id'] = invoice['partner_id'][0]
    #         rec['amount'] = invoice['residual']
    #     return rec

    @api.multi
    @api.depends('name', 'partner_id', 'remaining_amount')
    def name_get(self):
        result = []
        for payment in self:
            partner_name = payment.partner_id and payment.partner_id.name
            name = ':'.join((payment.name, partner_name, str(payment.remaining_amount)))
            result.append((payment.id, name))
        return result

    @api.model
    def name_search(self, name, args=None, operator='ilike', limit=100):
        args = args or []
        domain = []
        if name:
            partner = self.env['res.partner'].search([('name', operator, name)])
            partner_ids = partner and partner.ids or []
            domain = ['|', ('partner_id', 'in', partner_ids), ('name', operator, name)]
        payments = self.search(domain + args, limit=limit)
        return payments.name_get()

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            if vals.get('partner_type', '') == 'customer' and vals.get('payment_type', '') == 'inbound':
                vals['name'] = self.env['ir.sequence'].next_by_code('linyan.payment.customer.invoice')
            if vals.get('partner_type', '') == 'supplier' and vals.get('payment_type', '') == 'outbound':
                vals['name'] = self.env['ir.sequence'].next_by_code('linyan.payment.supplier.invoice')
        result = super(LinyanPayment, self).create(vals)
        return result

    @api.multi
    def unlink(self):
        for payment in self:
            self._cr.execute("select id from linyan_invoice_line where payment_id = %s" % payment.id)
            if self._cr.fetchall():
                raise UserError(('此单据已有关联数据，不能直接删除。'))
        return super(LinyanPayment, self).unlink()

    @api.multi
    def post(self):
        for rec in self:
            if rec.partner_type == 'customer' and rec.payment_type == 'inbound':
                sequence_code = 'linyan.payment.customer.invoice'
            if rec.partner_type == 'supplier' and rec.payment_type == 'outbound':
                sequence_code = 'linyan.payment.supplier.invoice'
            rec.name = self.env['ir.sequence'].with_context(ir_sequence_date=rec.payment_date).next_by_code(sequence_code)