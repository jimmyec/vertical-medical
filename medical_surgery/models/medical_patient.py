# -*- coding: utf-8 -*-
# Copyright 2017 Mauro Estrella
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import _, api, fields, models


class MedicalPatient(models.Model):
    _inherit = 'medical.patient'
    

    surgery_ids = fields.One2many(
        comodel_name='medical.surgery',
        inverse_name='patient_id',
        string='Surgeries',
    )
    count_surgery_ids = fields.Integer(
        compute='_compute_count_surgery_ids',
        string='Surgeries',
    )
    @api.multi
    def _compute_count_surgery_ids(self):
        for rec_id in self:
            rec_id.count_surgery_ids = len(rec_id.surgery_ids)
