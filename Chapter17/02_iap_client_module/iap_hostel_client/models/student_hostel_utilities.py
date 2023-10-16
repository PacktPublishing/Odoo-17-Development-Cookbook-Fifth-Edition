# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError
from odoo.addons.iap.tools import iap_tools


class HostelStudent(models.Model):
    _inherit = 'hostel.student'

    def call_laundry_facilities(self):
        self.ensure_one()
        user_token = self.env['iap.account'].get('hostel_utilities')
        params = {
            'account_token': user_token.account_token,
        }
        service_endpoint = 'http://localhost:8049'
        result = iap_tools.iap_jsonrpc(service_endpoint + '/call_utilities', params=params)
        if result.get('status') == 'success':
            # Do operations here...
            print("__success__status__")
        return True
