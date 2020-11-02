# -*- coding: utf-8 -*

# Template l10n_croatian:
# © 2018 Davor Bojkić - Bole <bole@dajmi5.com>

# 2020 Ernad Husremović <hernad@bring.out.ba>

# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Bosna i Hercegovina - Banke",
    "summary": "Banke u Bosni i Hercegovini",
    "category": "Localisation / Bosnia",
    "images": [],
    "version": "10.0.8",
    "application": False,
    "author": "Ernad Husremović",
    "website": "https://github.com/hernad/odoo_l10n-bosnia",
    "license": "AGPL-3",
    "depends": [
        "base_iban",
    ],
    "data": [
        "data/res_bank_data.xml",
        "views/res_partner_bank_view.xml",
        "views/res_bank_view.xml",
    ],
    "qweb": [],
    "demo": [],
    "auto_install": False,
    "installable": True,
}
