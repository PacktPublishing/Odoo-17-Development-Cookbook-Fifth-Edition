# -*- coding: utf-8 -*-

import logging

from odoo import models
from odoo.tools import populate

_logger = logging.getLogger(__name__)

class HostelData(models.Model):
    _inherit = 'hostel.room'
    _populate_sizes = {'small': 10, 'medium': 100, 'large': 500}

    def _populate_factories(self):
        return [
            ('name', populate.constant('Hostel Room {counter}')),
            ('room_no', populate.constant('{counter}')),
        ]

