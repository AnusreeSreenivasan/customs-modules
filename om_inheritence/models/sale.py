from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    sale_person_comment = fields.Text(string="Sale Person Comment")

    def _prepare_invoice(self):
        invoice_vals = super(SaleOrder, self)._prepare_invoice()
        invoice_vals['sale_person_comment'] = self.sale_person_comment
        print("invoice vals", invoice_vals)
        return invoice_vals
    




   
class Invoice(models.Model):
    _inherit = 'account.move'

    sale_person_comment = fields.Text(string="Sale Person Comment")

    