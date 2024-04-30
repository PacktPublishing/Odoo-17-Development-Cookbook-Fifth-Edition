from odoo import fields, models


class Hostel(models.Model):
    _name = "hostel.hostel"
    _description = "Information about hostel"

    name = fields.Char(string="Hostel Name", required=True)
    hostel_code = fields.Char(string="Code", required=True)
    street = fields.Char("Street")
    street2 = fields.Char("Street2")
