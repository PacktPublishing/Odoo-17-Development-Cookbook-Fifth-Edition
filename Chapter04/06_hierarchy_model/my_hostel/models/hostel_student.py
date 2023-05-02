from odoo import fields, models


class HostelStudent(models.Model):
    _name = "hostel.student"
    _description = "Hostel Student Information"

    name = fields.Char("Student Name")
    stud_gender = fields.Char("Gender", help="Student gender")
    active = fields.Boolean("Active", default=True,
        help="Activate/Deactivate hostel record")
    room_id = fields.Many2one("hostel.room", "Room",
        help="Select hostel room")
    status = fields.Selection([("draft", "Draft"),
        ("reservation", "Reservation"), ("pending", "Pending"),
        ("paid", "Done"),("discharge", "Discharge"), ("cancel", "Cancel")],
        string="Status", copy=False, default="draft",
        help="State of the student hostel")
