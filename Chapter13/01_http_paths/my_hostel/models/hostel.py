from odoo import api, fields, models


class Hostel(models.Model):
    _name = 'hostel.hostel'
    _description = "Information about hostel"
    _order = "id desc, name"
    _rec_name = 'hostel_code'

    name = fields.Char(string="hostel Name", required=True)
    hostel_code = fields.Char(string="Code", required=True)
    street = fields.Char('Street')
    street2 = fields.Char('Street2')
    zip = fields.Char('Zip', change_default=True)
    city = fields.Char('City')
    state_id = fields.Many2one("res.country.state", string='State')
    country_id = fields.Many2one('res.country', string='Country')
    phone = fields.Char('Phone',required=True)
    mobile = fields.Char('Mobile',required=True)
    email = fields.Char('Email')
    hostel_floors = fields.Integer(string="Total Floors")
    image = fields.Binary('Hostel Image')
    active = fields.Boolean("Active", default=True,
        help="Activate/Deactivate hostel record")
    type = fields.Selection([("male", "Boys"), ("female", "Girls"),
        ("common", "Common")], "Type", help="Type of Hostel",
        required=True, default="common")
    other_info = fields.Text("Other Information",
        help="Enter more information")
    description = fields.Html('Description')
    hostel_rating = fields.Float('Hostel Average Rating', 
                                # digits=(14, 4) # Method 1: Optional precision (total, decimals),
                                 digits='Rating Value' # Method 2
                                 )
    category_id = fields.Many2one('hostel.category')

    @api.depends('hostel_code')
    def _compute_display_name(self):
        for record in self:
            name = record.name
            if record.hostel_code:
                name = f'{name} ({record.hostel_code})'
            record.display_name = name
