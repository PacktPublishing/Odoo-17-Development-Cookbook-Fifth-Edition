# -*- coding: utf-8 -*-
from odoo import fields, models, api


class Base(models.AbstractModel):
    _inherit = 'base'

    @api.model
    def get_m2m_group_data(self, domain, m2m_field):
        records = self.search(domain)
        result_dict = {}
        for record in records:
            for m2m_record in record[m2m_field]:
                if m2m_record.id not in result_dict:
                    result_dict[m2m_record.id] = {
                        'name': m2m_record.name,
                        'children': [],
                        'model': m2m_record._name
                    }
                result_dict[m2m_record.id]['children'].append({
                    'name': record.display_name,
                    'id': record.id,
                })
        return result_dict
