from odoo import api,fields, models

class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Hospital Appointment"


    patient_id = fields.Many2one('hospital.patient', string="Patient")
    gender = fields.Selection([('male','Male'),('female','Female'),('others','Others')], string="Gender", related='patient_id.gender')
    appointment_time = fields.Datetime(string='Appoinment Time', default=fields.Datetime.now)
    booking_date = fields.Date(string='Booking Date', default=fields.Date.context_today)
    prescription = fields.Html(string='prescription')


    priority = fields.Selection([
        ('0', 'Normal'),
        ('1', 'Low'),
        ('2', 'High'),
        ('3', 'Very High')], string="Priority",
        help='Gives the sequence order when displaying a list of MRP documents.')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_consulation', 'In Consultation'),
        ('done', 'Done'),
        ('cancel', 'Cancelled')], string="Status")
    
    
    

    
    


    

