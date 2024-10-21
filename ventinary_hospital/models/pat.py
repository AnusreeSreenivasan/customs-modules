from odoo import api,fields,models


class HospitalPatient(models.Model):
    _name = "hospital.patients"
    _inherit = 'mail.thread'
    _description = "Patients Records"
    
    name = fields.Char(string="Name")