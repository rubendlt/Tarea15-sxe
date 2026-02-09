# -*- coding: utf-8 -*-
{
    'name': "hospital_primoplus",

    'summary': "Gestion de pacientes",

    'description': """
Una vaina para manejar pacientes
    """,

    'author': "Hospial SL",
    'website': "https://danielcastelao.org",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'report/hospital_report.xml',
        'report/hospital_report_template.xml',
        'report/hospital_report_herencia.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

