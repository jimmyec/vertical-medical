# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License GPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

{
    'name': 'Medical Website Base',
    'version': '13.0.0.0.0',
    'author': "LasLabs, Odoo Community Association (OCA)",
    'category': 'Medical',
    "website": "https://laslabs.com",
    "license": "GPL-3",
    "application": False,
    'installable': True,
    'post_init_hook': '_update_patients_legal_rep',
    'depends': [
        'medical',
        'website_portal',
        'website_form',
    ],
    'data': [
        'views/assets.xml',
        'views/medical_form_template.xml',
        'views/website_medical_template.xml',
    ],
    'demo': [
        'demo/medical_patient_demo.xml',
    ],
}
