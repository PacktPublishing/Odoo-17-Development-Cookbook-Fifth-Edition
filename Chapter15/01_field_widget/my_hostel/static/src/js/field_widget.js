/** @odoo-module */

import { Component } from "@odoo/owl";
import { registry } from "@web/core/registry";

export class CategColorField extends Component {
    setup() {
        this.totalColors = [1,2,3,4,5,6];
        super.setup();
    }
    clickPill(value) {
        this.props.record.update({ [this.props.name]: value });
    }
}
CategColorField.template = "CategColorField";
CategColorField.supportedTypes = ["integer"];
registry.category("fields").add("category_color", {
    component: CategColorField,
});

