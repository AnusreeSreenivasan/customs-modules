from odoo import models, fields, api

class SaleSqlView(models.Model):
    _name = 'sale.sql.view'
    _description = 'Sale Sql View'
    _auto = False


    sale_number = fields.Char('Sale Number')
    customer_name = fields.Char('Customer')
    order_date = fields.Datetime('Order Date')
    amount = fields.Monetary('Amount')
    currency_id = fields.Many2one('res.currency', string='Currency')
    user_name = fields.Char('User')
    product_qty = fields.Float('Quantity')
    product_volume = fields.Float('Volume')
    # total_amount = fields.Float('SUM')

    def init(self):
        self._cr.execute("""
            CREATE OR REPLACE VIEW  sale_sql_view AS (
                SELECT row_number() OVER() as id,
                so.name as sale_number,
                rp.name as customer_name,
                so.date_order as order_date,
                so.amount_total as amount,
                rc.id as currency_id,
                ru.login as user_name,
                SUM(sol.product_uom_qty) as product_qty,
                SUM(pp.volume * sol.product_uom_qty) as product_volume
                From sale_order so
                JOIN res_partner rp ON so.partner_id = rp.id
                JOIN res_company rc ON so.currency_id = rc.id
                JOIN res_users ru ON so.user_id = ru.id 
                JOIN sale_order_line sol ON so.id = sol.order_id 
                JOIN product_product pp ON sol.product_id = pp.id  
                GROUP BY so.name, rp.name, so.date_order, so.amount_total, rc.id, ru.login

            )
        """)