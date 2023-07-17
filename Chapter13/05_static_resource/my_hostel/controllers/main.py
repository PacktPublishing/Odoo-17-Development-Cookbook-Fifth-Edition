from odoo import http
from odoo.http import request


class Main(http.Controller):

    @http.route('/demo_page', type='http', auth='none')
    def students(self):
        image_url = '/my_hostel/static/src/image/odoo.png'
        html_result = """<html>
            <body>
                <img src="%s"/>
            </body>
        </html>""" % image_url
        return html_result

