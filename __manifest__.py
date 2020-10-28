# -*- coding: utf-8 -*-
{
    'name': "dd_external_id",

    'summary': """
        External ID management made esier""",

    'description': """
        This modules adds a mixin allowing to expose the external XMLID of every record as a computed field
        It also allows to automatically generate XMLID for the records missing one (but only when forced to do so)
    """,

    'author': "Digital Domus s.n.c.",
    'website': "http://www.digitaldomus.it",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '13.0.1.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        #'views/views.xml',
        #'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
