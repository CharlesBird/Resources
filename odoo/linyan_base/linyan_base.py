# -*- coding: utf-8 -*-

import json
from lxml import etree
from dateutil.relativedelta import relativedelta
from openerp import api, fields, models
from openerp.tools import float_is_zero, float_compare
from openerp.exceptions import UserError, RedirectWarning, ValidationError
import openerp.addons.decimal_precision as dp


class ResPartner(models.Model):
    _inherit = "res.partner"

    code = fields.Char('编号')
    short_name = fields.Char('简称', required=True, index=True)
    eng_name = fields.Char('英文名称', required=True, index=True)
    country_id2 = fields.Char('英文注册地址', readonly=True, default='CHINA')
    transport = fields.Boolean('运输服务')
    warehouse = fields.Boolean('仓储服务')
    sex = fields.Selection([('0', '女'), ('1', '男')], '性别', required=True, default='1')
    department = fields.Char('部门')


class ProductProduct(models.Model):
    _inherit = "product.product"

    short_name = fields.Char('简称', required=True, index=True)
    eng_name = fields.Char('英文名称', required=True, index=True)
    shape = fields.Selection([('liquid', '液态'), ('solid', '固态')], '商品形态')
    brand_id = fields.Many2one('linyan.brand', '品牌')
    model_id = fields.Many2one('linyan.model', '规格型号')
    packaging_id = fields.Many2one('product.packaging', '包装')
    user_ids = fields.Many2many('res.users', 'product_user_rel', 'product_id', 'user_id', string='可见人员', readonly=True, default=lambda self: [(6, 0, [self._uid])])

    # @api.model
    # def create(self, vals):
    #     vals['user_ids'] = [(6, 0, [self._uid])]
    #     result = super(ProductProduct, self).create(vals)
    #     return result

    @api.model
    def name_search(self, name, args=None, operator='ilike', limit=100):
        args = args or []
        domain = []
        if name:
            conds = name.split('-')
            for cond in conds:
                domain += ['|',('brand_id','ilike',cond),'|',('model_id','ilike',cond),'|',('packaging_id','ilike',cond),('name','ilike',cond)]
        recs = self.search(domain + args, limit=limit)
        return recs.name_get()


class LinyanBrand(models.Model):
    _name = "linyan.brand"

    name = fields.Char('名称', required=True)


class LinyanModel(models.Model):
    _name = "linyan.model"
    _rec_name = "description"

    description = fields.Char('牌号描述')
    brand_id = fields.Many2one('linyan.brand', '品牌', required=True, ondelete='cascade')


class ProductPackaging(models.Model):
    _inherit = "product.packaging"

    bulk = fields.Boolean('散装')
    pallet = fields.Boolean('托盘')
    note = fields.Text('其他描述')


class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    move_amount = fields.Monetary(string='账款金额', help="对应提货货值")


class ResUsers(models.Model):
    _inherit = "res.users"

    product_ids = fields.Many2many('product.product', 'product_user_rel', 'user_id', 'product_id', string='可见商品')