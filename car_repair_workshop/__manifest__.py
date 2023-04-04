# -*- coding: utf-8 -*-
{
    'name': "Car Repair Workshop",

    'summary': """Fleet Repair Vehical Repair car maintenance Auto fleet service repair car
        """,

    'description': """
                Car repair services V14.0
    """,

    'author':"Redian Software pvt.ltd",
    'website': "http://www.rediansoftware.com",
    'category': 'Extra Tools',
    'version': '0.1',
    'support': 'krishna.y@rediansoftware.com',
    'version': '14.0.1.0.1',
    'images': ['static/description/car_repair.png'],

    # any module necessary for this one to work correctly
    'depends': ['base','sale_management','purchase','stock','fleet','account'],

    # always loaded
    'license': 'LGPL-3',
    'currency': 'USD',
    'price': '1.0',
    'category': 'Feet',
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
