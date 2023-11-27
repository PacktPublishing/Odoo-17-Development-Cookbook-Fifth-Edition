# -*- coding: utf-8 -*-
from odoo import http
from odoo.addons.website.controllers.main import Website


class WebsiteInfo(Website):
    @http.route()
    def website_info(self):
        result = super(WebsiteInfo, self).website_info()
        print("\n \n result======>>>", result.qcontext)
        result.qcontext['apps'] = result.qcontext['apps'].filtered(
            lambda x: x.name != 'website'
        )
        print("\n \n result=$$$$$=====>>>", result.qcontext)
        return result