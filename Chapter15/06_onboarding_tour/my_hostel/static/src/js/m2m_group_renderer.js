/** @odoo-module **/
import { Component } from "@odoo/owl";

export class M2mGroupRenderer extends Component {
    onClickViewButton(group) {
        var children_ids = _.map(group.children, function (group_id) {
            return group_id.id;
        });
        const domain =  [['id', 'in', children_ids]]
        this.props.onClickViewButton(domain);
    }
    get groups() {
        return this.props.model.data
    }
}
M2mGroupRenderer.template = "M2mGroupRenderer";
M2mGroupRenderer.props = ["model", "onClickViewButton"];
