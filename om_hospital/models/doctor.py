from odoo import api,fields,models


class HospitalPatient(models.Model):
    _name = "hospital.doctor"
    _inherit = 'mail.thread'
    _description = "Doctor Records"
    _rec_name = 'name'



    name = fields.Char(string="Name" ,required=True)
    ref = fields.Char(string="Reference",required=True)
    age = fields.Integer(string="Age")
    gender = fields.Selection([('male','Male'),('female','Female'),('other','Other')], string="Gender")
    Department = fields.Char(string="Department")
    active = fields.Boolean(default=True)

    @api.depends('name')
    def _compute_display_name(self):
        for rec in self:
            name =  f'{rec.ref} - {rec.name}'
            rec.display_name = name
    # def name_get (self):
        # res = []
        # for rec in self:
        #   name = f'{rec.ref} - {rec.name}'
        #   res.append((rec.id,name))
        # return res    
# this code will get combination of 2 methods in patient doctor table

