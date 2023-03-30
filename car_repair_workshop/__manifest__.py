# -*- coding: utf-8 -*-
{
    'name': "car_repair_workshop",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
                Car repair services 
    """,

    'author':"Redian Software pvt.ltd",
    'website': "http://www.rediansoftware.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale_management','purchase','stock','fleet','account'],

    # always loaded
    'data': [
         'security/ir.model.access.csv',
        'security/security.xml',
        'data/car.xml',
        'views/views.xml',
        'views/checklist_view.xml',
        'views/car_diagnosis_view.xml',
        'views/work_order.xml',
        'views/menu.xml',
        'views/hide_menu.xml',
        'views/inherited_views.xml',
        'wizard/update_technician.xml',
        'report/car_repair.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
