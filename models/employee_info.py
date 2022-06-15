from datetime import date, datetime, timedelta

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError


class EmployeeInfo(models.Model):
    _name = "employee.info"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Employee Informations"

    name = fields.Char(string="Employee Name", required=True)
    date_of_birth = fields.Date(string="Date of Birth")
    designation = fields.Char(string="Designation")
    manager_id = fields.Many2one('res.users', string="Manager")
    department = fields.Selection([
        ('it', 'IT'),
        ('hr', 'HR'),
        ('account', 'Account'),
        ('sale', 'Sale'),
    ], string='Department')
    emergency_contact_id = fields.One2many('emergency.contact', 'employee_id', string='Emergency Contact Lines', required=True)
    education_info_id = fields.One2many('education.info', 'employee_id', string='Education Info Lines', required=True)
    leave_info_id = fields.One2many('leave.info', 'employee_id', string='Education Info Lines', required=True)

    @api.model_create_multi
    def create(self, vals_list):
        if vals_list:
            for item in vals_list:
                if 'emergency_contact_id' in item.keys():
                    if not item['emergency_contact_id']:
                        raise ValidationError(
                            _('Create At least one Emergency Contact'))
                else:
                    raise ValidationError(
                        _('Create At least one Emergency Contact'))
                if 'education_info_id' in item.keys():
                    if not item['education_info_id']:
                        raise ValidationError(
                            _('Create At least one Education Information'))
                else:
                    raise ValidationError(
                        _('Create At least one Education Information'))
                if 'leave_info_id' in item.keys():
                    if not item['leave_info_id']:
                        raise ValidationError(
                            _('Create At least one Leave Information'))
                else:
                    raise ValidationError(
                        _('Create At least one Leave Information'))
        return super().create(vals_list)

    def write(self, vals):
        if vals:
            if 'emergency_contact_id' in vals.keys():
                if not vals['emergency_contact_id'][0][2]:
                    raise ValidationError(
                        _('Create At least one Emergency Contact'))
            if 'education_info_id' in vals.keys():
                if not vals['education_info_id'][0][2]:
                    raise ValidationError(
                        _('Create At least one Education Information'))
            if 'leave_info_id' in vals.keys():
                if not vals['leave_info_id'][0][2]:
                    raise ValidationError(
                        _('Create At least one Leave Information'))
        return super().write(vals)
