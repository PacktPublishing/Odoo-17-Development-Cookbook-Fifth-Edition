# -*- coding: utf-8 -*-
from odoo import models, fields


class ConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    group_start_date = fields.Boolean(
        "Manage hostel start dates",
        group='base.group_user',
        implied_group='my_hostel.group_start_date',
    )
    module_note = fields.Boolean("Install Notes app")
