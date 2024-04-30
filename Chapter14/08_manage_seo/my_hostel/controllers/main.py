from odoo import http
from odoo.http import request
from odoo.addons.http_routing.models.ir_http import slug
from odoo.addons.website.models.ir_http import sitemap_qs2dom



class Main(http.Controller):

    def sitemap_hostels(env, rule, qs):
        Hostels = env['hostel.hostel']
        dom = sitemap_qs2dom(qs, '/hostels', Hostels._rec_name)
        #to filter urls
        #dom += [('name', 'ilike', 'abc')]
        for f in Hostels.search(dom):
            loc = '/hostels/%s' % slug(f)
            if not qs or qs.lower() in loc:
                yield {'loc': loc}

    @http.route('/hostels', type='http', auth='public', website = True)
    def hostel(self):
        hostels = request.env['hostel.hostel'].sudo().search([])
        return request.render(
        'my_hostel.hostels', {
            'hostels': hostels,
        })

    @http.route('/hostels/<model("hostel.hostel"):hostel>', type='http', auth='public', website = True, sitemap=sitemap_hostels)
    def hostel_detail(self, hostel):
        return request.render(
        'my_hostel.hostel_detail', {
            'hostel': hostel,
            'main_object': hostel
        })

