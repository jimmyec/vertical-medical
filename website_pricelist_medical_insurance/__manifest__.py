# -*- coding: utf-8 -*-
# © 2015 LasLabs Inc.
# License GPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

{

    'name': 'Medical Website - Insurance Pricelist',
    'description': 'Adds Insurance logic to Website pricelists',
    'version': '13.0.0.0.0',
    'author': 'LasLabs, Odoo Community Association (OCA)',
    'category': 'Medical',
    'depends': [
        'website_sale',
        'medical_insurance_pricelist',
    ],
    'data': [
        'views/website_pricelist_view.xml',
        'security/ir.model.access.csv',
        'security/medical_insurance_security.xml',
    ],
    'website': 'https://laslabs.com',
    'license': 'GPL-3',
    'installable': True,
    'auto_install': False,
}
