# custom_invoice/__manifest__.py
{
    "name": "Custom Invoice Template",
    "version": "1.0",
    "summary": "Custom Invoice Template for Odoo 17",
    "category": "Invoice",
    "depends": ["base_setup", "account", "l10n_gcc_invoice", "web"],
    "data": [
        "report/custom_invoice.xml",
    ],
    "installable": True,
    "application": False,
}
