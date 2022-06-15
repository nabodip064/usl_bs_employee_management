from odoo import models, fields, api, _


class EmergencyContact(models.Model):
    _name = "emergency.contact"
    _description = "Emergency Contact"

    name = fields.Char(string="Contact Person Name")
    address = fields.Char(string="Contact Person Address")
    phone = fields.Char(string="Contact Person Phone")
    employee_id = fields.Many2one('employee.info', string="Employee")
