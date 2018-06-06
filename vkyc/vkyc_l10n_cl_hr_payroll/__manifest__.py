# -*- coding: utf-8 -*-
{
    'name': 'Chilean Payroll and Indicators Adjustment',
    'version': '10.0.2.0.0',
    'category': 'Tools',
    'license': 'AGPL-3',
    'description': '''Update UF, UTM and Dollar Official Value in a daily basis
using SBIF webservices''',
    'author': 'VKYC',
    'website': 'http://vkyc',
    'depends': [
        'hr_payroll',
        'l10n_cl_hr_payroll',
    ],
    'data': [
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'auto_install': False,
}
