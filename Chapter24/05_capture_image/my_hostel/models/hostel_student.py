from datetime import datetime, timedelta
from odoo import fields, models, api


class HostelStudent(models.Model):
    _name = "hostel.student"
    _description = "Hostel Student Information"

    @api.depends("admission_date", "discharge_date")
    def _compute_check_duration(self):
        """Method to check duration"""
        for rec in self:
            if rec.discharge_date and rec.admission_date:
                rec.duration = (rec.discharge_date - rec.admission_date).days

    def _inverse_duration(self):
        for stu in self:
            if stu.discharge_date and stu.admission_date:
                duration = (stu.discharge_date - stu.admission_date).days
                if duration != stu.duration:
                    stu.discharge_date = (stu.admission_date + timedelta(days=stu.duration)).strftime('%Y-%m-%d')

    def _get_default_test_type_id(self):
        return self.env['quality.point.test_type'].search([('technical_name', '=','picture')], limit=1).id

    name = fields.Char("Student Name")
    gender = fields.Selection([("male", "Male"),
        ("female", "Female"), ("other", "Other")],
        string="Gender", help="Student gender")
    active = fields.Boolean("Active", default=True,
        help="Activate/Deactivate hostel record")
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
    device_id = fields.Many2one('iot.device', string='IoT Device', domain="[('type', '=', 'camera')]")
    test_type_id = fields.Many2one('quality.point.test_type', 'Test Type',
                                   help="Defines the type of the quality control point.",
                                   required=True, default=_get_default_test_type_id)
    test_type = fields.Char(related='test_type_id.technical_name', readonly=True)
    ip = fields.Char(related="device_id.iot_id.ip")
    identifier = fields.Char(related='device_id.identifier')
    picture = fields.Binary()

