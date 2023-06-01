/** @odoo-module **/

import { Model } from "@web/views/model";

export class M2mGroupModel extends Model {
    setup(params) {
        const metaData = Object.assign({}, params.metaData, {});
        this.data = params.data || {};
        this.metaData = this._buildMetaData(metaData);
        this.m2m_field = this.metaData.m2m_field;
    }
    _buildMetaData(params) {
        const metaData = Object.assign({}, this.metaData, params);
        return metaData;
    }
    async load(searchParams) {
        var self = this;
        const model = self.metaData.resModel;
        const method = 'get_m2m_group_data'
        const m2m_field = self.m2m_field
        const result = await this.orm.call(
            model,
            method,
            [searchParams.domain, m2m_field]
        )
        self.data = result;
        return result;
    }
}
