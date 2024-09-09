from odoo import fields, models


class CustomCompanyModel(models.Model):
    _inherit = "res.company"

    signature = fields.Binary(string="Signature")
    seal = fields.Binary(string="The Seal")

    
