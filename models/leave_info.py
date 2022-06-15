from datetime import date, datetime, timedelta
from odoo import models, fields, api, _


class LeaveInfo(models.Model):
    _name = "leave.info"
    _description = "Leave Info"

    leave_type = fields.Selection([
        ('casual', 'Casual Leave'),
        ('sick', 'Sick Leave'),
        ('maternity', 'Maternity Leave'),
        ('others', 'Others Leave'),
    ], string='Leave Type', default='casual')
    leave_days = fields.Integer(string="Leave Days", required=True)
    Leave_period = fields.Integer(string="Leave Period", readonly=True, default=date.today().year)
    employee_id = fields.Many2one('employee.info', string="Employee")
