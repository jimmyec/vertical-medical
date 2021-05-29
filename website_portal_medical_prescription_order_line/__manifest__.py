# -*- coding: utf-8 -*-
# Copyright 2016-2017 LasLabs Inc.
# License GPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html)

{
    'name': 'Medical Portal - Prescriptions',
    'version': '13.0.0.0.0',
    'author': "LasLabs, Odoo Community Association (OCA)",
    'category': 'Medical',
    'depends': [
        'website_portal_medical_patient',
        'website_sale_medical_prescription',
    ],
    'website': 'https://laslabs.com',
    'license': 'GPL-3',
    'data': [
        'security/ir.model.access.csv',
        'static/src/xml/website_portal_medical_prescription_order_line.xml',
        'templates/assets.xml',
    ],
    'demo': [
        'demo/medical_medicament.xml',
        'demo/medical_patient.xml',
        'demo/medical_patient_medication.xml',
        'demo/medical_physician.xml',
        'demo/medical_prescription_order.xml',
        'demo/medical_prescription_order_line.xml',
    ],
    'application': False,
    'installable': True,
}
