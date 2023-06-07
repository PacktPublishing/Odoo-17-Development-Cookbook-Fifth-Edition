from odoo import fields, models


class HostelRoom(models.Model):
    _inherit = "hostel.room"

    category = fields.Integer('Category')
