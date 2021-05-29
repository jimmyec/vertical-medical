# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License GPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

{
    'name': 'Medical Website - Medicament Sales',
    'version': '13.0.0.0.0',
    'author': "LasLabs, Odoo Community Association (OCA)",
    'category': 'Medical',
    'depends': [
        'sale_stock_medical_prescription',
        'website_sale',
        'sale_medical_medicament',
    ],
    "website": "https://laslabs.com",
    "license": "GPL-3",
    "application": False,
    'installable': True,
    'data': [
        'security/ir.model.access.csv',
        'security/medical_medicament.xml',
    ],
}
