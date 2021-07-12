# -*- coding: utf-8 -*-

from odoo import models, fields 


class MedicalSurgeryProcedure(models.Model):
    _name = 'medical.surgery.procedure'
    _description = 'Medical Surgery Procedure'

    surgery_id = fields.Many2one(
    	string='Surgery', 
    	comodel_name='medical.surgery', 
    	required=True, 
    	index=True
    )
    procedure_id = fields.Many2one(
    	string='Procedure', 
    	comodel_name='medical.procedure', 
    	required=True, 
    	index=True
    )
    notes = fields.Text(string='Notes')
    