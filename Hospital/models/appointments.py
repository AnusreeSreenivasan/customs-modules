from odoo import api,fields,models
from odoo.exceptions import ValidationError

class Appointment(models.Model):
    _name = "hospital.appointments"
    _inherit = 'mail.thread'
    _description = "Appointment Records"


    patient_id = fields.Many2one('hospital.patients', string="Patient")
    ref = fields.Char(string="Reference:", default=lambda self:('New'))
    description_ids = fields.One2many(comodel_name='hospital.description',inverse_name='Appointment_id',string="description")
    doctor_id = fields.Many2one('hospital.doctors', string="Doctor")
    appointment_time = fields.Date(string='Appoinment Date', default=fields.Date.context_today)
    booking_date = fields.Date(string='Booking Date', default=fields.Date.context_today)
    prescriptions = fields.Html(string="prescriptions")
    # phone_num = fields.Char(string="Phone")
    # phone_id = fields.Many2one(comodel_name="hospital.patients",inverse_name="phone",string="phone")
    phone_number = fields.Integer(string="Patient phone:",compute ="_compute_patient_phone", inverse="inverse_compute_patient_phone",tracking=True)


    

    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_consulation', 'In Consultation'),
        ('done', 'Done'),
        ('cancel', 'Cancelled')], string="Status")

    @api.depends('patient_id')
    def _compute_patient_phone(self):
            for patients in self:
                patients.phone_number = patients.patient_id.phone
    @api.depends('phone')
    def inverse_compute_patient_phone(self):
         for patients in self:
            if patients.phone_number:
                self.patient_id.phone = self.phone_number
         
   
    # @api.onchange('patient_id')
    # def onchange_patient_id(self):
    #     for patients in self:
    #         patients.phone_num = patients.patient_id.phone
        
    # @api.onchange('phone_num')
    # def onchange_phone(self):
    #     for patients in self:
    #         if patients.phone_num:
    #             self.patient_id.phone = self.phone_num
         

    @api.model_create_multi
    def create(self,val):
        for vals in val:
            vals['ref']=self.env['ir.sequence'].next_by_code('hospital.appointments')
            print(vals)
        return super(Appointment,self).create(val)
    
    

    
    
class Description(models.Model):
    _name = "hospital.description"


    medicine_id = fields.Many2one('product.product', string="Medicine") 
    descriptions = fields.Char(string="Descriptions")  
    Appointment_id = fields.Many2one('hospital.appointments',string="Appointment") 
    frequency = fields.Char(string="frequency")
    dos_age = fields.Many2one(comodel_name='uom.uom',string="Dosage")   
    duration = fields.Integer(string="Duration")
    duration_unit = fields.Char(string="Duration Unit")



    








   


