from odoo import fields, models, api


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
    phone = fields.Char('Phone',required=1)
    mobile = fields.Char('Mobile',required=1)
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
    ref_doc_id = fields.Reference(selection='_referencable_models', string='Reference Document')

    @api.model
    def _referencable_models(self):
        models = self.env['ir.model'].search([('field_id.name', '=', 'message_ids')])
        return [(x.model, x.name) for x in models]

    def name_get(self):
        result = []
        for record in self:
            rec_name = "%s (%s)" % (record.name, record.hostel_code)
            result.append((record.id, rec_name))
        return result
