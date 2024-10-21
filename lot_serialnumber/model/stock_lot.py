from odoo import models,api,fields

class StockLots(models.Model):
    _inherit = "stock.lot"

    on_hold = fields.Boolean(string="OnHold")

    message =  fields.Char(string="Message")
