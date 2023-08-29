# -*- coding: utf-8 -*-
from odoo import fields, models


class RoomCategory(models.Model):
    _name = 'hostel.room.category'
    _description = "Hostel Room Category"

    name = fields.Char('Category')
    description = fields.Text('Description')
    parent_id = fields.Many2one(
        'hostel.room.category',
        string='Parent Category',
        ondelete='restrict',
        index=True
    )
    child_ids = fields.One2many(
        'hostel.room.category', 'parent_id',
        string='Child Categories')
    amount = fields.Float("Amount", help="Enter amount per month")
