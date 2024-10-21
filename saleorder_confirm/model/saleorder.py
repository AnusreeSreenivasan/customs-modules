from odoo import api,fields,models
from odoo.exceptions import UserError


class SaleOrder(models.Model):
    _inherit = "sale.order"

    state = fields.Selection(selection_add=[
        ('waiting_approval', 'Waiting Approval'),
        ('approval', 'Approval'),("sale",)
    ])
        


    # def action_set_waiting_approval(self):
    #     self.state = 'waiting approval'

    def action_set_approval(self):
        self.ensure_one()
        self.state = 'approval'

        mail_activity_type = self.env.ref('mail.mail_activity_data_todo')  

        if not mail_activity_type:
            raise UserError('Activity Type "ToDo" not found')

        self.env['mail.activity'].create({
            'activity_type_id': mail_activity_type.id,
            'res_id': self.id,
            'res_model_id': self.env['ir.model']._get_id('sale.order'),
            'user_id': self.env.user.id, 
            'summary': 'Approval Required',
            'note': 'This record is approved.',  
            'date_deadline': fields.Date.context_today(self), 
        })
        # self.message_post(body="Sale order submitted for approval by %s" % (self.env.user))
    
    def action_draft_confirm(self):
        self.ensure_one()
        self.state = 'draft'
        mail_activity_type = self.env.ref('mail.mail_activity_data_todo')  

        if not mail_activity_type:
            raise UserError('Activity Type "ToDo" not found')

        self.env['mail.activity'].create({
            'activity_type_id': mail_activity_type.id,
            'res_id': self.id,
            'res_model_id': self.env['ir.model']._get_id('sale.order'),
            'user_id': self.env.user.id, 
            'summary': 'Approval Rejected',
            'note': 'This record is go to draft state.', 
            'date_deadline': fields.Date.context_today(self), 
        })
        # self.message_post(body="Sale order approval Rejected by %s" % (self.env.user))

    
    def action_set_waiting_approval(self):
        self.ensure_one()
        self.state = 'waiting_approval'

        mail_activity_type = self.env.ref('mail.mail_activity_data_todo')  

        if not mail_activity_type:
            raise UserError('Activity Type "ToDo" not found')

        self.env['mail.activity'].create({
            'activity_type_id': mail_activity_type.id,
            'res_id': self.id,
            'res_model_id': self.env['ir.model']._get_id('sale.order'),
            'user_id': self.env.user.id,  
            'summary': 'Waiting for Approval',
            'note': 'This record is waiting for approval.',  
            'date_deadline': fields.Date.context_today(self),  
        })        
        # self.message_post(body="Sale order submitted for waiting_approval by %s" % (self.env.user))



    def _can_be_confirmed(self):
        self.ensure_one()
        return self.state in {'approval'} or super()._can_be_confirmed()

    def action_confirm(self):
        if self.state not in 'approval':
            raise UserError('Invalid Operation: The sale order must be approved before it can be confirmed.')
        self.message_post(body="Sale order confirmed by %s" % (self.env.user.name))
        super(SaleOrder, self).action_confirm()