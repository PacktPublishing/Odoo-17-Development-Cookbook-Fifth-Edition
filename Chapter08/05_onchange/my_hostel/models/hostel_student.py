from datetime import timedelta
from odoo import _, api, models, fields


class HostelStudent(models.Model):
    _name = "hostel.student"
    _description = "Hostel Student Information"

    def _inverse_duration(self):
        for stu in self:
            if stu.discharge_date and stu.admission_date:
                duration = (stu.discharge_date - stu.admission_date).days
                if duration != stu.duration:
                    stu.discharge_date = (stu.admission_date + timedelta(days=stu.duration)).strftime('%Y-%m-%d')

    name = fields.Char("Student Name")
    gender = fields.Selection([("male", "Male"),
        ("female", "Female"), ("other", "Other")],
        string="Gender", help="Student gender")
    active = fields.Boolean("Active", default=True,
        help="Activate/Deactivate hostel record")
    hostel_id = fields.Many2one("hostel.hostel", "hostel", help="Name of hostel")
    room_id = fields.Many2one("hostel.room", "Room",
        help="Select hostel room")
    status = fields.Selection([("draft", "Draft"),
        ("reservation", "Reservation"), ("pending", "Pending"),
        ("paid", "Done"),("discharge", "Discharge"), ("cancel", "Cancel")],
        string="Status", copy=False, default="draft",
        help="State of the student hostel")
    admission_date = fields.Date("Admission Date",
        help="Date of admission in hostel",
        default=fields.Datetime.today)
    discharge_date = fields.Date("Discharge Date",
        help="Date on which student discharge")
    duration = fields.Integer("Duration", compute="_compute_check_duration", inverse="_inverse_duration",
                               help="Enter duration of living")

    def action_assign_room(self):
        return {
            'type': 'ir.actions.act_window',
            'name': _('Assign Room'),
            'res_model': 'assign.room.student.wizard',
            'view_type': 'form',
            'view_mode': 'form',
            'views': [[False, 'form']],
            'target': 'new',
        }

    def action_remove_room(self):
        if self.env.context.get("is_hostel_room"):
            self.room_id = False

    @api.onchange('admission_date', 'discharge_date')
    def onchange_duration(self):
        if self.discharge_date and self.admission_date:
            self.duration = (self.discharge_date.year - \
                            self.admission_date.year) * 12 + \
                            (self.discharge_date.month - \
                            self.admission_date.month)
