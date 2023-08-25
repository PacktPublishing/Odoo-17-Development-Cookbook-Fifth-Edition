from odoo import fields, models, api, _


class HostelRoom(models.Model):

    _name = "hostel.room"
    _description = "Hostel Room Information"
    _rec_name = "room_no"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    @api.depends("student_per_room", "student_ids")
    def _compute_check_availability(self):
        """Method to check room availability"""
        for rec in self:
            rec.availability = rec.student_per_room - len(rec.student_ids.ids)

    @api.model
    def _default_room_stage(self):
        Stage = self.env['hostel.room.stage']
        return Stage.search([], limit=1)

    name = fields.Char(string="Room Name", required=True)
    room_no = fields.Char("Room No.", required=True)
    floor_no = fields.Integer("Floor No.", default=1, help="Floor Number")
    currency_id = fields.Many2one('res.currency', string='Currency')
    rent_amount = fields.Monetary('Rent Amount', help="Enter rent amount per month") # optional attribute: currency_field='currency_id' incase currency field have another name then 'currency_id'
    hostel_id = fields.Many2one("hostel.hostel", "hostel", help="Name of hostel")
    student_ids = fields.One2many("hostel.student", "room_id",
        string="Students", help="Enter students")
    hostel_amenities_ids = fields.Many2many("hostel.amenities",
        "hostel_room_amenities_rel", "room_id", "amenitiy_id",
        string="Amenities", domain="[('active', '=', True)]",
        help="Select hostel room amenities")
    student_per_room = fields.Integer("Student Per Room", required=True,
        help="Students allocated per room")
    availability = fields.Float(compute="_compute_check_availability",
        store=True, string="Availability", help="Room availability in hostel")
    stage_id = fields.Many2one(
        'hostel.room.stage',
        default=_default_room_stage
    )
    color = fields.Integer()
    popularity = fields.Selection([('no', 'No Demand'), ('low', 'Low Demand'), ('medium', 'Average Demand'), ('high', 'High Demand'),])

    _sql_constraints = [
       ("room_no_unique", "unique(room_no)", "Room number must be unique!")]

    @api.constrains("rent_amount")
    def _check_rent_amount(self):
        """Constraint on negative rent amount"""
        if self.rent_amount < 0:
            raise ValidationError(_("Rent Amount Per Month should not be a negative value!"))


class HostelRoomState(models.Model):
    _name = 'hostel.room.stage'
    _order = 'sequence,name'

    name = fields.Char("Name")
    sequence = fields.Integer("Sequence")
    fold = fields.Boolean("Fold?")
