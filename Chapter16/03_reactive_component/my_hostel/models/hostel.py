from odoo import fields, models


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

    def name_get(self):
        result = []
        for record in self:
            rec_name = "%s (%s)" % (record.name, record.hostel_code)
            result.append((record.id, rec_name))
        return result
