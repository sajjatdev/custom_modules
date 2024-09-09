from odoo import api, fields, models


class ContactsCustomModel(models.Model):
    _inherit = "res.partner"

    arabic_name = fields.Char(string="Arabic Name")
    registration_number = fields.Char(string="Registration number")
