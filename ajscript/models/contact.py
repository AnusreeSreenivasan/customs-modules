from odoo import models,fields,api

class AjsContact(models.Model):
    _name = 'ajs.contact'
    _description = 'AJS Contact'
    
    name = fields.Char(string="Customer Name", required=True)
    age = fields.Integer()
    # partner_id = fields.Many2one('res.partner',string='Name')
    
    
    latitude = fields.Float(string="Latitude")
    longitude = fields.Float(string="Longitude")
    coordinate = fields.Char(string="Coordinates", compute="_compute_coordinates", store=False)

    @api.depends('latitude', 'longitude')
    def _compute_coordinates(self):
        for record in self:
            if record.latitude and record.longitude:
                record.coordinate = f"{record.latitude},{record.longitude}"
            else:
                record.coordinate = ''