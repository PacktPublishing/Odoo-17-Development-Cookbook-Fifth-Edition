/** @odoo-module */

import { Component } from "@odoo/owl";
import { registry } from "@web/core/registry";

export class IntColorField extends Component {
    setup() {
        this.totalColors = [1,2,3,4,5,6,7,8,9,10];
        super.setup();
    }
    clickPill(ev) {
        var $target = $(ev.currentTarget);
        var data = $target.data();
        this.props.update(data.value);
    }
}
IntColorField.template = "IntColorField";
IntColorField.supportedTypes = ["integer"];
registry.category("fields").add("int_color", IntColorField);

