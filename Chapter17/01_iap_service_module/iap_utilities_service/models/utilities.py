# -*- coding: utf-8 -*-# -*- coding: utf-8 -*-
from odoo import models, fields, api


class RequestUtilities(models.Model):
    _name = 'request.utilities'

    name = fields.Char('Name', required=True)

    @api.model
    def _request_service_utilities(self, service_key, account_token):
        if service_key and account_token:
            return {
                'status': 'success',
                'data': {
                    
                }
            }
        else:
            return {
                'status': 'failure',
            }
            
