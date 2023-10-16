# -*- coding: utf-8 -*-
from odoo import models, fields


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    utilities_service_key = fields.Char("Utilities Service Key", config_parameter='iap.utilities_service_key')
