# -*- coding: utf-8 -*-
# © 2016 ClearCorp
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Cash Budget HR Payroll',
    'version': '8.0.1.2',
    'summary': "Goverment Institutions Cash Budget",
    'author': 'ClearCorp',
    'website': 'http://clearcorp.cr',
    'category': 'Accounting & Finance/Human Resources',
    'license': 'AGPL-3',
    'sequence': 10,
    'application': False,
    'installable': True,
    'auto_install': False,
    'depends': [
        'hr_payroll_account',
        'hr_payroll',
        'cash_budget'
        ],
    'data': [
        'views/hr_payroll.xml',
        ]
}
