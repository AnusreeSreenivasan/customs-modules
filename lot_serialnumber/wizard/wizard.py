from odoo import models, fields, api

class StockLotWizard(models.TransientModel):
    _name = 'lot.wizard'
    _description = 'Stock Lot Wizard'

    reason = fields.Text(string='Reason')
    stocklot_id = fields.Many2one('stock.lot',string="StocklotId")

    def confirm_action(self):
        for stock in self.stocklot_id:
            stock.on_hold = True
            stock.message = self.reason