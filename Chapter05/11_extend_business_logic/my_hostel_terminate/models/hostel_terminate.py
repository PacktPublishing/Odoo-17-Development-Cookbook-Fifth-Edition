# -*- coding: utf-8 -*-
from datetime import timedelta
from odoo import models, fields


class HostelRoom(models.Model):
    _inherit = 'hostel.room'

    date_terminate = fields.Date('Date of Termination')
    category_id = fields.Many2one("hostel.room.category", string="Category")

    def make_closed(self):
        day_to_allocate = self.category_id.max_allow_days or 10
        self.date_terminate = fields.Date.today() + timedelta(days=day_to_allocate)
        return super(HostelRoom, self).make_closed()

    def make_available(self):
        self.date_terminate = False
        return super(HostelRoom, self).make_available()


class RoomCategory(models.Model):
    _inherit = 'hostel.room.category'

    max_allow_days = fields.Integer(
        'Maximum allows days',
        help="For how many days room can be assigned",
        default=10)

