from odoo import fields, models


class Inquiries(models.Model):
    _name = 'hostel.inquiries'
    _description = "Inquiries about hostel"
    # _order = "id desc,"

    name = fields.Char(string="Student Name", required=True)
    phone = fields.Char(string="Phone", required=True)
    email = fields.Char(string="Email")
    book_fy = fields.Char(string="Book for Year")
    queries = fields.Html(string="Your Question")