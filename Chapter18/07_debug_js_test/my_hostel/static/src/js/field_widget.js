/** @odoo-module */

import { Component, useState, onWillStart, onWillUnmount } from "@odoo/owl";
import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";
import { useRecordObserver } from "@web/model/relational_model/utils";
import { standardFieldProps } from "@web/views/fields/standard_field_props";

export class IntColorField extends Component {
    setup() {
        super.setup(...arguments);
        this.totalColors = [1,2,3,4,5,6,7,8,9,10];
    }
    async clickPill(ev) {
        const data = $(ev.currentTarget).data();
        this.props.record.update({ [this.props.name]: data.value });
    }
}

IntColorField.props = {
    ...standardFieldProps,
};

IntColorField.template = "IntColorField";

export const intColorField = {
    component: IntColorField,
    fieldDependencies: [ { name: "color", type: "integer" } ],
};

registry.category("fields").add("int_color", intColorField);

