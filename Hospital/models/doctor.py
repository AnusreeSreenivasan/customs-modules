from odoo import api,fields,models
from odoo.exceptions import ValidationError

class HospitalPatient(models.Model):
    _name = "hospital.doctors"
    _inherit = 'mail.thread'
    _description = "Doctor Records"




    name = fields.Char(string="Name" , required=True)
    department = fields.Char(string="Department")
    phone = fields.Char(string="Phone")
    ref = fields.Char(string="Reference", default=lambda self:('New'))
    patient_ids = fields.Many2many('hospital.patient', string='Patients')
    user_id = fields.Many2one('res.users',string="User", required=True)
    prescription_details = fields.Text(string="Prescription Details")
    prescription_date = fields.Datetime(string="Date of Prescription", default=fields.Datetime.now)
    description_details = fields.Text(string="Description")
    description_date = fields.Datetime(string="Date of Description", default=fields.Datetime.now)