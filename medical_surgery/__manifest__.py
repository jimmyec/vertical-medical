# -*- coding: utf-8 -*-
{
    'name': "Medical Surgery",

    'summary': """
        Medical    
    """,

    'description': """
        - Medical surgery
    """,

    'author': "Capstone Solutions Inc.",
    'website': "http://www.capstone.ph",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Medical',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        # 'medical', 
        'medical_physician', 
        'medical_pathology', 
    ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/ir_sequence_data.xml',
        'views/medical_surgery_view.xml',
        'views/medical_procedure_view.xml',
        'views/medical_operating_area_view.xml',
        'views/medical_operating_sector_view.xml',
        # 'views/medical_patient.xml',
        'views/medical_menu.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
    'qweb': [
        'static/src/xml/web_widget_image_webcam.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}