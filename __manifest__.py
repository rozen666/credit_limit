# Copyright 2022 By Lortega
# License LGPL-3 or later (http://www.gnu.org/licenses/lgpl).
{
    'name': 'Credit Limit',
    'summary': '''
    Instance creator for virtualdemand. This is the app.
    ''',
    'author'  : 'lortega',
    'website' : '',
    'license' : 'LGPL-3',
    'category': 'Installer',
    'version' : '1.0',
    "depends" : [
                  'hr',
                  'sale_management',
                  'account',
                ],
    'test'    : [
                ],
    'data'    : [
                  'views/credit_limit.xml',        
                ],
    'demo'    : [
                ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
