# -*- coding: utf-8 -*-
import openerp
from openerp import api, fields, models, SUPERUSER_ID
import logging
_logger = logging.getLogger(__name__)


class ResUsers(models.Model):
    _inherit = "res.users"
    _description = u"用户接口扩展"

    u_token = fields.Char('Token')

    def check_credentials(self, cr, uid, password):
        # 钉钉免密登录验证
        try:
            return super(ResUsers, self).check_credentials(cr, uid, password)
        except openerp.exceptions.AccessDenied:
            res = self.search(cr, SUPERUSER_ID, [('id', '=', uid), ('u_token', '=', password)])
            if not res:
                raise

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
