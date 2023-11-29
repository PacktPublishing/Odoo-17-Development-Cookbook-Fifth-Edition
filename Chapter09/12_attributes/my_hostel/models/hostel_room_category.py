# -*- coding: utf-8 -*-
from odoo import fields, models, _


class RoomCategory(models.Model):
    _name = 'hostel.room.category'
    _inherit = ['mail.thread', 'mail.activity.mixin']
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
    hoste_room_ids = fields.One2many(
        'hostel.room', 'hostel_room_category_id',
        string='Hostel Room')
    related_hostel_room = fields.Integer(compute='_compute_related_hostel_room')

    def _compute_related_hostel_room(self):
        for record in self:
            record.related_hostel_room = self.env['hostel.room'].search_count([
                ('hostel_room_category_id', '=', record.id),
            ])

    def action_open_related_hostel_room(self):
        related_hostel_room_ids = self.env['hostel.room'].search([
                ('hostel_room_category_id', '=', self.id),
            ]).ids
        return {
            'type': 'ir.actions.act_window',
            'name': _('Hostel Room'),
            'res_model': 'hostel.room',
            'view_type': 'list',
            'view_mode': 'list',
            'views': [[False, 'list'], [False, 'form']],
            'domain': [('id', 'in', related_hostel_room_ids)],
        }

