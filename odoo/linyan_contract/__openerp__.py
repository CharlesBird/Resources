# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Linyan contract',
    'version': '1.0',
    'summary': 'Sale, Purchase and move',
    'description': """Sale, Purchase and move""",
    'category': 'Linyan',
    'website': 'https://www.odoo.com',
    'depends': ['linyan_base'],
    'data': [
        'security/linyan_security.xml',
        'security/ir.model.access.csv',
        'wizard/contract_make_report.xml',
        'linyan_contract_view.xml',
        'linyan_contract_sequence.xml',
        'report/linyan_cash_report_view.xml',
        'report/linyan_profit_report_view.xml',
        'report/linyan_cash_avg_price_report_view.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False
}
