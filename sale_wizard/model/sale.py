from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'



    def action_open_wizard(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Sale Order Wizard',
            'view_mode': 'form',
            'res_model': 'sale.order.wizard',
            'target': 'new',
            'context': {
                'default_sale_order_id': self.id,
            },
        }



  