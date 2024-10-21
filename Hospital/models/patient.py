from odoo import api,fields,models
from odoo.exceptions import ValidationError
import datetime


class HospitalPatient(models.Model):
    _name = "hospital.patients"
    _inherit = 'mail.thread'
    _description = "Patients Records"




    name = fields.Char(string="Name:", required=True)
    doctor_ids = fields.Many2many('hospital.doctor', string='Doctors')
    age = fields.Integer(string="Age:")
    gender = fields.Selection([('male','Male'),('female','Female')],string="Gender")
    ref = fields.Char(string="Reference:", default=lambda self:('New'))
    address = fields.Char(string="Address:")
    street = fields.Char(string="street:")
    street2 = fields.Char(string="street2:")
    city = fields.Char(string="city:")
    state_id = fields.Char(string="state_id")
    zip = fields.Char(string="zip")
    phone = fields.Char(string="Phone")
    country_id = fields.Many2one('res.country',string="country_id")
    image = fields.Image(string="image")
    appointment_count = fields.Integer(string="Appointment count:",compute="_compute_appointment_count")
    appointment_ids = fields.One2many(comodel_name="hospital.appointments",inverse_name="patient_id",string="appointment_ids")
    bdate = fields.Date(string="Date of Birth",required=True)
    

    
        
    

    @api.onchange('bdate')
    def calculate_age(self):
        today_date = fields.Date.today()
        for stud in self:
            if stud.bdate:
                bdate = fields.Datetime.to_datetime(stud.bdate).date()
                total_age = today_date.year - bdate.year - ((today_date.month, today_date.day) < (bdate.month, bdate.day))
                if total_age < 0 :
                    raise ValidationError("please selecte correct one")
                else:
                    stud.age = total_age
            

                    


    @api.depends('appointment_ids')
    def _compute_appointment_count(self):
            for patients in self:
                patients.appointment_count = len(patients.appointment_ids.ids)
   

                

    @api.model_create_multi
    def create(self,val):
        for vals in val:
            vals['ref']=self.env['ir.sequence'].next_by_code('hospital.patients')
            print(vals)
        return super(HospitalPatient,self).create(val)
    
    def action_view_appointments(self):
        return {
            'name': ('Appointments'),
            'res_model':'hospital.appointments',
            'view_mode':'list,form',
            'context':{},
            'domain':[('patient_id', '=',self.id)],
            'type':'ir.actions.act_window',

        }



    




