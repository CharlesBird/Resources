# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Linyan base datas',
    'version': '1.0',
    'summary': 'Base datas',
    'description': """Partner, product, users and account""",
    'category': 'Linyan',
    'website': 'https://www.odoo.com',
    'depends': ['stock', 'account', 'report'],
    'data': [
        'security/linyan_security.xml',
        'security/ir.model.access.csv',
        'linyan_base_view.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False
}
