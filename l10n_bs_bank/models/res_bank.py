# -*- coding: utf-8 -*-

from odoo import api, fields, models


class ResBank(models.Model):
    _inherit = "res.bank"

    prefix = fields.Char( 'Prefix', size=4, required=True, help='Prefix broja transakcijskog računa')

    _sql_constraints = [
        ('prefix_uniq', 'unique(prefix)', 'Prefiks banke mora biti jedinstven!'),
    ]
    