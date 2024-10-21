from odoo import models,fields


class CustomWidget(models.Model):
    _name = "custom.widget"
    _description = "Custom Widget"

    name = fields.Char(string='Name') 
    custom_widgets = fields.Char(string='Custom Field')