# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    ThinkOpen Solutions Brasil
#    Copyright (C) Thinkopen Solutions <http://www.tkobr.com>.
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

import logging
import openerp

_logger = logging.getLogger(__name__)


class DbSetRoot(openerp.http.Root):

    def setup_db(self, httprequest):
        res = super(DbSetRoot, self).setup_db(httprequest)
        data = httprequest.args
        if httprequest.method in ['POST', 'GET'] and data and data.get('db', ''):
            httprequest.session.db = data.get('db', '')
        return res


root = DbSetRoot()
openerp.http.root.setup_db = root.setup_db