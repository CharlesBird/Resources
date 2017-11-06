# -*- coding: utf-8 -*-

from openerp import api, fields, models, SUPERUSER_ID
from openerp.exceptions import Warning, except_orm
import random
import string
import logging
_logger = logging.getLogger(__name__)


def random_secret():
    # the token has an entropy of about 120 bits (6 bits/char * 20 chars)
    chars = string.ascii_letters+string.digits
    return ''.join(random.SystemRandom().choice(chars) for i in xrange(28))


class ResUsers(models.Model):
    _inherit = "res.users"
    _description = u"用户接口扩展"

    secret = fields.Char('密钥', size=28, default=random_secret())
    u_token = fields.Char('Token')
    expiry_date = fields.Datetime('失效日期')

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
