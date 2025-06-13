from odoo import models, fields, api

class MembershipBranch(models.Model):
    _name = 'membership.branch'
    _description = 'Branch'

    name = fields.Char(string="Branch Name", required=True)

class MembershipMember(models.Model):
    _name = 'membership.member'
    _description = 'Member'
    _rec_name = 'full_name_en'

    first_name = fields.Char(string="First Name")
    last_name = fields.Char(string="Last Name")
    full_name_en = fields.Char(string="Full Name (EN)", compute="_compute_full_name_en", store=True)
    full_name_ar = fields.Char(string="Full Name (AR)")
    branch_ids = fields.Many2many('membership.branch', string="Branches")
    renewal_date = fields.Date(string="Latest Renewal Date", compute="_compute_latest_renewal", store=False)
    status = fields.Selection([
        ('draft', 'Draft'),
        ('approved', 'Approved'),
        ('black_list', 'Black List')
    ], string='Status', default='draft')

    @api.depends('first_name', 'last_name')
    def _compute_full_name_en(self):
        for rec in self:
            rec.full_name_en = f"{rec.first_name or ''} {rec.last_name or ''}".strip()

  
    def _compute_latest_renewal(self):
        for rec in self:
            sale_orders = self.env['sale.order'].search([
                ('partner_id', '=', rec.id),
                ('state', 'in', ['sale', 'done'])
            ], order='date_order desc', limit=1)
            rec.renewal_date = sale_orders.date_order if sale_orders else False

