from odoo import api,fields,models
from odoo.exceptions import ValidationError

class Department(models.Model):
    _name = "hospital.department"
    _inherit = 'mail.thread'
    _description = " Department Records"


    name = fields.Char(string="Name" , required=True)
