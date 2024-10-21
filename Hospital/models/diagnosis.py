from odoo import api,fields,models
from odoo.exceptions import ValidationError

class Diagnosis(models.Model):

    _name = "hospital.diagnosis"
    _inherit = 'mail.thread'
    _description = "Diagnosis Records"

    diagnosis = fields.Html(string="diagnosis")
    prescription_ids = fields.One2many(comodel_name='hospital.prescription',inverse_name='diagnosis_id',string="prescription")
    patient_id = fields.Many2one('hospital.patients', string="Patient")
    doctor_id = fields.Many2one('hospital.doctors',string="Doctor")
   

    



class Prescription(models.Model):

    _name = "hospital.prescription"

    
    medicine_id = fields.Many2one('product.product', string="Medicine") 
    description = fields.Char(string="Description")  
    diagnosis_id = fields.Many2one('hospital.diagnosis',string="Diagnosis") 
    frequency = fields.Char(string="frequency")
    dos_age = fields.Many2one(comodel_name='uom.uom',string="Unit of Measure")   
    quantity = fields.Char(string="dosage")





   

    