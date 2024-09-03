# custom_invoice/__manifest__.py
{
    "name": "Custom Invoice Template",
    "version": "1.0",
    "summary": "Custom Invoice Template for Odoo 17",
    "category": "Invoice",
    "depends": ["base_setup", "account", "l10n_gcc_invoice", "web"],
    "data": [
        "views/layout_views.xml",
        "report/custom_invoice.xml",
        "report/google_font.xml",
    ],
    "installable": True,
    "application": False,
}
