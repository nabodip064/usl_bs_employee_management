from odoo import models, fields, api, _


class EducationInfo(models.Model):
    _name = "education.info"
    _description = "Education Info"

    institute = fields.Char(string="Institute")
    degree = fields.Char(string="Degree")
    passing_year = fields.Integer(string="Passing Year")
    employee_id = fields.Many2one('employee.info', string="Employee")

