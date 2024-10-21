from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order.line'

    is_selected = fields.Boolean(string=" Is Selected")

