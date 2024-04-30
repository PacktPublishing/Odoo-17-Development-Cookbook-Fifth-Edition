from odoo import fields, models


class HostelRoom(models.Model):

    _name = "hostel.room"
    _description = "Hostel Room Information"
    _rec_name = "room_no"

    name = fields.Char(string="Room Name", required=True)
    room_no = fields.Char("Room No.", required=True)
    image = fields.Binary(string="Image")
    hostel_id = fields.Many2one("hostel.hostel", "hostel", help="Name of hostel")
    category = fields.Integer('Category')
    student_ids = fields.One2many("hostel.student", "room_id",
        string="Students", help="Enter students")

