from datetime import timedelta
from odoo import _, api, models, fields
from odoo.exceptions import UserError
import re
from odoo.tools import email_split, email_escape_char


class HostelStudent(models.Model):
    _name = "hostel.student"
    _description = "Hostel Student Information"
    _inherit = ['mail.thread', 'mail.activity.mixin']

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

    name = fields.Char("Student Name")
    email = fields.Char("Student Email")
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
        self.ensure_one()
        if self.status != "paid":
            raise UserError(_("You can't assign a room if it's not paid."))
        room_as_superuser = self.env['hostel.room'].sudo()
        room_rec = room_as_superuser.create({
            "name": "Room A-103",
            "room_no": "A-103",
            "floor_no": 1,
            "room_category_id": self.env.ref("my_hostel.single_room_categ").id,
            "hostel_id": self.hostel_id.id,
        })
        if room_rec:
            self.room_id = room_rec.id

    @api.model
    def create(self, values):
        result = super().create(values)
        self.env['res.partner'].create({
            'name': result.name,
            'email': result.email
        })
        return result

    def send_mail_assign_room(self):
        template_id = self.env.ref('my_hostel.assign_room_to_student')
        self.message_post_with_template(template_id.id)

    def send_mail_assign_room_qweb(self):
        self.message_post_with_view('my_hostel.assign_room_to_student_qweb')

    @api.model
    def message_new(self, msg_dict, custom_values=None):
        self = self.with_context(default_user_id=False)
        if custom_values is None:
            custom_values = {}
        custom_values['name'] = re.match(r"(.+?)\s*<(.+?)>", msg_dict.get('from')).group(1)
        custom_values['email'] = email_escape_char(email_split(msg_dict.get('from'))[0])
        return super(HostelStudent, self).message_new(msg_dict, custom_values)
