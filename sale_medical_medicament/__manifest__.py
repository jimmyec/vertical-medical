# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License GPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

{
    'name': 'Sales - Medical Medicament',
    'version': '13.0.0.0.0',
    'author': "LasLabs, Odoo Community Association (OCA)",
    'category': 'Medical',
    'depends': [
        'medical_medicament',
        'sale',
    ],
    "website": "https://laslabs.com",
    "license": "GPL-3",
    "application": False,
    'installable': True,
    'data': [
        'views/product_product_view.xml',
        'views/product_template_view.xml',
    ],
}
