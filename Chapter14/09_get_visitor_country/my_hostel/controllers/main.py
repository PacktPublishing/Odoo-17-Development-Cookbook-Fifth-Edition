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
        country_id = False
        country_code = request.geoip and request.geoip.get('country_code') or False
        if country_code:
            country_ids = request.env['res.country'].sudo().search([('code', '=', country_code)])
            if country_ids:
                country_id = country_ids[0].id
        domain = ['|', ('restrict_country_ids', '=', False), ('restrict_country_ids', 'not in', [country_id])]
        hostels = request.env['hostel.hostel'].sudo().search(domain)
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

