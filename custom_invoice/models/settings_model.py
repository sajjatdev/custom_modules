from odoo import api, models, fields


class SettingsModel(models.TransientModel):
    _inherit = "base.document.layout"

    signature = fields.Binary(related="company_id.signature", readonly=False)
    preview_signature = fields.Binary(related="signature", string="Signature")

    seal = fields.Binary(related="company_id.seal", readonly=False)
    preview_seal = fields.Binary(related="seal", string="The Seal")
