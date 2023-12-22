from odoo import fields, models, api, _


class HostelRoomCopy(models.Model):

    _name = "hostel.room.copy"
    _inherit="hostel.room"
    _description = "Hostel Room Information Copy"
