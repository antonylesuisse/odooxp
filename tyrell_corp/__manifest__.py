# -*- coding: utf-8 -*-
{
    'name': "tyrell_corp",

    'summary': """
        Tyrell Corp Replicant Manager
    """,

    'description': """
            Tyrell Corp Replicant Manager
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.3',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'crm',
    ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/tyrell_corp_data.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
