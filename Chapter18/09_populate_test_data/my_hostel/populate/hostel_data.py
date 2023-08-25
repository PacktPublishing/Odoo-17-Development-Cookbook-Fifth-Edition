# -*- coding: utf-8 -*-

import logging
import random

from odoo import models
from odoo.tools import populate

_logger = logging.getLogger(__name__)


class RoomData(models.Model):
    _inherit = 'hostel.room.member'
    _populate_sizes = {'small': 10, 'medium': 100, 'large': 500}
    _populate_dependencies = ["res.partner"]

    def _populate_factories(self):
        partner_ids = self.env.registry.populated_models['res.partner']
        return [
            ('partner_id', populate.randomize(partner_ids)),
        ]

class HostelData(models.Model):
    _inherit = 'hostel.room'
    _populate_sizes = {'small': 10, 'medium': 100, 'large': 500}
    _populate_dependencies = ["hostel.room.member"]

    def _populate_factories(self):
        member_ids = self.env.registry.populated_models['hostel.room.member']
        def get_member_ids(values, counter, random):
            return [
                (6, 0, [
                    random.choice(member_ids) for i in range(random.randint(1, 2))
                ])
            ]
        return [
            ('name', populate.constant('Hostel Room {counter}')),
            ('room_no', populate.constant('{counter}')),
            ('member_ids', populate.compute(get_member_ids)),
        ]
