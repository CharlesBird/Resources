# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

import time
from datetime import datetime
from openerp import api, fields, models, _
import openerp.addons.decimal_precision as dp
from dateutil.relativedelta import relativedelta
from openerp.exceptions import UserError


class ContractCashIn(models.TransientModel):
    _name = "contract.cash.in"
    _description = "Contract Cash In"

    product_id = fields.Many2one('product.product', '产品', required=True)
    end_date = fields.Date('截止日期', required=True,
                           default=lambda *a: time.strftime('%Y-%m-%d'))
    cash = fields.Boolean('头寸')

    @api.multi
    def make_report(self):
        product_id = self.product_id.id
        end_date = self.end_date
        cash = self.cash
        report_data = self.env['linyan.contract'].search_read([('product_id', '=', product_id), ('contract_date', '<=', end_date), ('cash', '=', cash), (
            'state', '!=', 'cancel'), ('buy', '=', True)], ['partner_id', 'product_id', 'year', 'month', 'contract_name', 'actual_qty', 'price', 'amount', 'cash'])
        values = []
        for data in report_data:
            partner_id = data['partner_id'][0]
            product_id = data['product_id'][0]
            year = data['year']
            month = data['month']
            contract_name = data['contract_name']
            actual_qty = data['actual_qty']
            price = data['price']
            amount = data['amount']
            cash = data['cash']
            values.append({
                'partner_id': partner_id,
                'product_id': product_id,
                'year': year,
                'month': month,
                'contract_name': contract_name,
                'actual_qty': actual_qty,
                'price': price,
                'amount': amount,
                'cash': cash})
        self._cr.execute("delete from linyan_cash_report")
        res_ids = []
        for val in values:
            report = self.env['linyan.cash.report'].create(val)
            res_ids.append(report.id)
        name = '空头买入'
        if cash:
            name = '头寸买入'
        return {
            'type': 'ir.actions.act_window',
            'name': name,
            'view_type': 'form',
            'view_mode': 'tree',
            'res_model': 'linyan.cash.report',
            'res_id': res_ids
        }


class ContractCashOut(models.TransientModel):
    _name = "contract.cash.out"
    _description = "Contract Cash Out"

    product_id = fields.Many2one('product.product', '产品', required=True)
    end_date = fields.Date('截止日期', required=True,
                           default=lambda *a: time.strftime('%Y-%m-%d'))
    cash = fields.Boolean('头寸')

    @api.multi
    def make_report(self):
        product_id = self.product_id.id
        end_date = self.end_date
        cash = self.cash
        report_data = self.env['linyan.contract'].search_read([('product_id', '=', product_id), ('contract_date', '<=', end_date), ('cash', '=', cash), (
            'state', '!=', 'cancel'), ('buy', '=', False)], ['partner_id', 'product_id', 'year', 'month', 'contract_name', 'actual_qty', 'price', 'amount', 'cash'])
        values = []
        for data in report_data:
            partner_id = data['partner_id'][0]
            product_id = data['product_id'][0]
            year = data['year']
            month = data['month']
            contract_name = data['contract_name']
            actual_qty = data['actual_qty']
            price = data['price']
            amount = data['amount']
            cash = data['cash']
            values.append({
                'partner_id': partner_id,
                'product_id': product_id,
                'year': year,
                'month': month,
                'contract_name': contract_name,
                'actual_qty': actual_qty,
                'price': price,
                'amount': amount,
                'cash': cash})
        self._cr.execute("delete from linyan_cash_report")
        res_ids = []
        for val in values:
            report = self.env['linyan.cash.report'].create(val)
            res_ids.append(report.id)
        name = '空头卖出'
        if cash:
            name = '头寸卖出'
        return {
            'type': 'ir.actions.act_window',
            'name': name,
            'view_type': 'form',
            'view_mode': 'tree',
            'res_model': 'linyan.cash.report',
            'res_id': res_ids
        }


class MoveQuantity(models.TransientModel):
    _name = "move.quantity"

    product_id = fields.Many2one('product.product', '产品', required=True)
    end_date = fields.Date('截止日期', required=True, default=lambda *a: time.strftime('%Y-%m-%d'))

    @api.multi
    def make_report(self):
        cr = self._cr
        product_id = self.product_id.id
        end_date = (datetime.strptime(self.end_date, "%Y-%m-%d") + relativedelta(days=1)).strftime('%Y-%m-%d')
        move_in = self.env['logistics.move'].search([('product_id', '=', product_id), ('date_done', '<', end_date), ('state', '=', 'done'), ('move_out', '=', False), ('move_in', '=', True)])
        in_datas = []
        if move_in.ids:
            cr.execute("select lm.warehouse_dest_id as warehouse_id, lm.product_id, lc.make_company, lc.supplierinfo_id, sum(lm.actual_qty) as actual_qty from logistics_move lm left join linyan_contract lc on lm.contract_id = lc.id where lm.id in %s group by lm.warehouse_dest_id, lm.product_id, lc.make_company, lc.supplierinfo_id", (tuple(move_in.ids),))
            in_datas = cr.dictfetchall()
        new_in_datas = {}
        for idt in in_datas:
            k = '-'.join([str(idt['warehouse_id']) or '0', idt['make_company'] or '', str(idt['supplierinfo_id']) or '0'])
            new_in_datas.update({k: idt})
        move_out = self.env['logistics.move'].search([('product_id', '=', product_id), ('date_done', '<', end_date), ('state', '=', 'done'), ('move_out', '=', True), ('move_in', '=', False)])
        out_datas = []
        if move_out.ids:
            cr.execute("select lm.warehouse_src_id as warehouse_id, lm.product_id, lc.make_company, lc.supplierinfo_id, sum(lm.actual_qty) as actual_qty from logistics_move lm left join linyan_contract lc on lm.contract_id = lc.id where lm.id in %s group by lm.warehouse_src_id, lm.product_id, lc.make_company, lc.supplierinfo_id", (tuple(move_out.ids),))
            out_datas = cr.dictfetchall()
        new_out_datas = {}
        for odt in out_datas:
            k = '-'.join([str(odt['warehouse_id']) or '0', odt['make_company'] or '', str(odt['supplierinfo_id']) or '0'])
            new_out_datas.update({k: odt})
        quantity_datas = []
        in_lists = list(set(new_in_datas).difference(set(new_out_datas)))
        for il in in_lists:
            quantity_datas.append(new_in_datas[il])
        out_lists = list(set(new_out_datas).difference(set(new_in_datas)))
        for ol in out_lists:
            quantity_out_datas = new_out_datas[ol].copy()
            quantity_out_datas.update({'actual_qty': -new_out_datas[ol]['actual_qty']})
            quantity_datas.append(quantity_out_datas)
        inter_lists = list(set(new_in_datas) & set(new_out_datas))
        for intl in inter_lists:
            actual_qty = new_in_datas[intl]['actual_qty'] - new_out_datas[intl]['actual_qty']
            quantity_inter_datas = new_in_datas[intl].copy()
            quantity_inter_datas.update({'actual_qty': actual_qty})
            quantity_datas.append(quantity_inter_datas)
        self._cr.execute("delete from move_quantity_report")
        res_ids = []
        for qty_dt in quantity_datas:
            report = self.env['move.quantity.report'].create(qty_dt)
            res_ids.append(report.id)
        return {
            'type': 'ir.actions.act_window',
            'name': '库存报表',
            'view_type': 'form',
            'view_mode': 'tree',
            'res_model': 'move.quantity.report',
            'res_id': res_ids
        }


class LinyanMakeInvoice(models.TransientModel):
    _name = "linyan.make.invoice"

    end_date = fields.Date('截止日期', required=True, default=lambda *a: time.strftime('%Y-%m-%d'))

    @api.multi
    def make_report(self):
        cr = self._cr
        end_date = self.end_date
        cr.execute("delete from linyan_invoice_report")
        cr.execute("""select COALESCE(t1.rece_invoice, 0.0) as rece_invoice,
            -1*COALESCE(t2.pay_invoice, 0.0) as pay_invoice,
            -1*COALESCE(t3.rece_payment, 0.0) as rece_payment,
            COALESCE(t4.pay_payment, 0.0) as pay_payment,
            COALESCE(t1.rece_invoice, 0.0)-COALESCE(t3.rece_payment, 0.0)-COALESCE(t2.pay_invoice, 0.0)+COALESCE(t4.pay_payment, 0.0) as amount
            from (select 1 as rel_id, sum(residual) as rece_invoice from linyan_invoice where invoice_type = 'out_invoice'
                and date_invoice < '%s') t1 left join (select 1 as rel_id, sum(residual) as pay_invoice from linyan_invoice
                where invoice_type = 'in_invoice' and date_invoice < '%s') t2 on t1.rel_id = t2.rel_id left join
        (select 1 as rel_id, sum(remaining_amount) as rece_payment from linyan_payment where payment_type = 'inbound'
            and payment_date < '%s') t3 on t1.rel_id = t3.rel_id left join
        (select 1 as rel_id, sum(remaining_amount) as pay_payment from linyan_payment where payment_type = 'outbound'
            and payment_date < '%s') t4 on t1.rel_id = t4.rel_id""" % (end_date, end_date, end_date, end_date))
        value = cr.dictfetchone()
        if value:
            self.env['linyan.invoice.report'].create(value)
            return {
                'type': 'ir.actions.act_window',
                'name': '库存报表',
                'view_type': 'form',
                'view_mode': 'tree',
                'res_model': 'linyan.invoice.report'
            }
        return {'type': 'ir.actions.act_window_close'}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
