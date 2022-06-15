from odoo import api, fields, models


class ResUserInherit(models.Model):
    _inherit = "res.users"

    department = fields.Selection([
        ('it', 'IT'),
        ('hr', 'HR'),
        ('account', 'Account'),
        ('sale', 'Sale'),
    ], string='Department')