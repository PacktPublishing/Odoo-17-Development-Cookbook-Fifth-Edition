/** @odoo-module */

import { Component } from "@odoo/owl";
import { registry } from "@web/core/registry";
import { qweb } from 'web.core';

export class CategColorField extends Component {
    setup() {
        this.totalColors = [1,2,3,4,5,6];
        super.setup();
    }
    clickPill(ev) {
        var $target = $(ev.currentTarget);
        var data = $target.data();
        this.props.update(data.value);
    }
    categInfo(ev){
        var $target = $(ev.currentTarget);
        var data = $target.data();
        $target.parent().find(".categInformationPanel").html(
            $(qweb.render('CategInformation',{
                'value': data.value,
                'widget': this
            }))
        );
    }
}
CategColorField.template = "CategColorField";
CategColorField.supportedTypes = ["integer"];
registry.category("fields").add("category_color", CategColorField);

