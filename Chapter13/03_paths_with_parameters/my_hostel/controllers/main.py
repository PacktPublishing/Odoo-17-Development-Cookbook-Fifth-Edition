from odoo import http
from odoo.http import request


class Main(http.Controller):

    @http.route('/my_hostel/student_details', type='http', auth='none')
    def student_details(self, student_id):
        record = request.env['hostel.student'].sudo().browse(int(student_id))
        return u'<html><body><h1>%s</h1>Room No: %s' % (
            record.name,
            str(record.room_id.room_no) or 'none',
        )

    @http.route("/my_hostel/student_details/<model('hostel.student'):student>",  
            type='http', auth='none')
    def student_details_in_path(self, book):
        return self.student_details(student.id)

