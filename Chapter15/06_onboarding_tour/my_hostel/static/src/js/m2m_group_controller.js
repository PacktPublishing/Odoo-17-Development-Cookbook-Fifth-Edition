/** @odoo-module **/

import { useService } from "@web/core/utils/hooks";
import { Layout } from "@web/search/layout";
import { useModelWithSampleData } from "@web/model/model";
import { standardViewProps } from "@web/views/standard_view_props";
import { Component } from "@odoo/owl";

export class M2mGroupController extends Component {
    setup() {
        this.actionService = useService("action");
        this.model = useModelWithSampleData(this.props.Model, this.props.modelParams);
    }
    _onBtnClicked(domain) {
        this.actionService.doAction({
            type: 'ir.actions.act_window',
            name: this.model.metaData.title,
            res_model: this.props.resModel,
            views: [[false, 'list'], [false, 'form']],
            domain: domain,
        });
    }
    _onAddButtonClick(ev) {
        this.actionService.doAction({
            type: 'ir.actions.act_window',
            name: this.model.metaData.title,
            res_model: this.props.resModel,
            views: [[false, 'form']],
            target: 'new'
        });
    }
}
M2mGroupController.template = "M2mGroupView";
M2mGroupController.components = { Layout };

M2mGroupController.props = {
    ...standardViewProps,
    Model: Function,
    modelParams: Object,
    Renderer: Function,
    buttonTemplate: String,
};

