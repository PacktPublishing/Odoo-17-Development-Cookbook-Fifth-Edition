# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
from odoo.addons.iap.tools import iap_tools


class Main(http.Controller):
    @http.route('/call_utilities', type='json', auth="public")
    def call_utilities_services(self, account_token):
        service_key = request.env['ir.config_parameter'].sudo().get_param('iap.utilities_service_key', False)
        if not service_key:
            return {
                'status': 'service is not active'
            }
        credits_to_reserve = 1
        data = {}
        with iap_tools.iap_charge(request.env, service_key, account_token, credits_to_reserve):
            data = request.env['request.utilities'].sudo()._request_service_utilities(service_key, account_token)
            data['status'] == 'success'
            if data['status'] == 'failure':
                raise Exception('Request not process')
        return data
