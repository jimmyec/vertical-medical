# -*- coding: utf-8 -*-
# Copyright 2016-2017 LasLabs Inc.
# License GPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from odoo.tests.common import HttpCase


class TestUi(HttpCase):

    def test_medical_patient_views(self):
        """ Should navigate around medical patient views without error """
        code = (
            'odoo.__DEBUG__.services["web_tour.tour"].'
            'run("website_portal_medical_patient.medical_patient_tour")'
        )
        ready = (
            'odoo.__DEBUG__.services["web_tour.tour"].tours['
            '"website_portal_medical_patient.medical_patient_tour"].ready'
        )
        self.phantom_js(
            url_path='/my/medical',
            code=code,
            ready=ready,
            login='portal',
        )
