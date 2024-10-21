from odoo import models, fields, api
from io import BytesIO
import base64
import xlrd


class SaleOrderWizard(models.TransientModel):
    _name = 'sale.order.wizard'
    _description = 'Sale Order Wizard'

    upload_file= fields.Binary(string='Upload File')
    sale_order_id = fields.Many2one("sale.order",string='ordered id')

    def action_open_excel_reports(self):
        file = base64.b64decode(self.upload_file)
        workbook = xlrd.open_workbook(file_contents=file)
        worksheet = workbook.sheet_by_index(0)

        for row_index in range(1, worksheet.nrows):  # Skip header row
            product_id = worksheet.cell(row_index, 0).value
            qty = worksheet.cell(row_index, 1).value
            unit_price = worksheet.cell(row_index, 2).value

            # Find product by name
            product = self.env['product.product'].search([('default_code', '=',product_id )], limit=1)
            if product:
                # Create Sale Order line
                self.env['sale.order.line'].create({
                        'order_id': self.sale_order_id.id,
                        'product_id': product.id,
                        'product_uom_qty': qty,
                        'price_unit': unit_price,
                    })

            return {'type': 'ir.actions.act_window_close'}