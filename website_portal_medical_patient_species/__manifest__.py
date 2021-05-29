# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License GPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

{
    "name": "Medical Website - Patient Species",
    "summary": "Add species options to website_medical patients.",
    "version": "13.0.0.0.0",
    "category": "Medical",
    "website": "https://laslabs.com/",
    "author": "LasLabs, Odoo Community Association (OCA)",
    "license": "GPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "website_portal_medical_patient",
        "medical_patient_species",
    ],
    "data": [
        "data/ir_model_data.xml",
        "views/patients_template.xml",
        "views/assets.xml",
        "security/ir.model.access.csv",
    ],
}
