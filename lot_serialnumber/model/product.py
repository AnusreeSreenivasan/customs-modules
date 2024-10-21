from odoo import fields,models,api


class StockMoveLine(models.Model):
    _inherit = 'stock.move.line'

    
    @api.model
    def create(self, vals):
        if 'lot_id' in vals:
            product_id = vals.get('product_id')
            if product_id:
                available_lots = self.env['stock.lot'].search([
                    ('product_id', '=', product_id),
                    ('on_hold', '=', False)
                ])
                if available_lots:
                    vals['lot_id'] = available_lots[0].id
                else:
                    vals['lot_id'] = False
        res = super(StockMoveLine, self).create(vals)
        return res
