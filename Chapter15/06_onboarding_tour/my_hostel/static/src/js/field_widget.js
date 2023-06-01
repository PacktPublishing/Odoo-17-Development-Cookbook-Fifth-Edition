/** @odoo-module */

import { Component, onWillStart , onWillUpdateProps} from "@odoo/owl";
import { registry } from "@web/core/registry";
import { qweb } from 'web.core';

export class CategColorField extends Component {
    setup() {
        this.totalColors = [1,2,3,4,5,6];
        onWillStart(() => {
            this.loadCategInformation();
        });
        onWillUpdateProps(() => {
            this.loadCategInformation();
        });
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
    async loadCategInformation() {
        var self = this;
        self.categoryInfo = {};
        var resModel = self.env.model.root.resModel;
        var domain = [];
        var fields = ['category'];
        var groupby = ['category'];
        const categInfoPromise = await self.env.services.orm.readGroup(
            resModel,
            domain,
            fields,
            groupby
        );
        categInfoPromise.map((info) => {
            self.categoryInfo[info.category] = info.category_count;
        });
    }
}
CategColorField.template = "CategColorField";
CategColorField.supportedTypes = ["integer"];
registry.category("fields").add("category_color", CategColorField);

