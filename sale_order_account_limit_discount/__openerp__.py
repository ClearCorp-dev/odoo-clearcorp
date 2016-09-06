# -*- coding: utf-8 -*-
# © <YEAR(S)> ClearCorp
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Sale order limit discount',
    'summary': 'The module allows the creation of different groups that '
               'restrict changes in prices and discounts.',
    'version': '9.0.1.0',
    'category': 'Sales',
    'website': 'http://clearcorp.cr',
    'author': 'ClearCorp',
    'license': 'AGPL-3',
    'sequence': 10,
    'application': False,
    'installable': True,
    'auto_install': False,
    'depends': [
        'base', 'sale', 'account'
    ],
    'data': [
        'security/sale_order_account_limit_discount.xml',
        'security/ir.model.access.csv',
        'views/account_limit_view.xml'
    ]
}

