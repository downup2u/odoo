# -*- coding: utf-8 -*-
{
    'name': "cashcard",

    'summary': """
        cash card""",

    'description': """
        Long description of module's purpose
    """,

    'author': "wangxiaoqing",
    'website': "http://www.xiaoke.info",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.2',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'templates.xml',
        'views/cashcard.xml',
     ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}