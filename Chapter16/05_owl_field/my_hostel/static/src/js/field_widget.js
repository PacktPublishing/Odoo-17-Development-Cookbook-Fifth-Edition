/** @odoo-module */

import { Component, onWillStart , onWillUpdateProps} from "@odoo/owl";
import { registry } from "@web/core/registry";

class ColorPill extends Component {
    static template = 'OWLColorPill';
    pillClicked() {
        this.props.onClickColorUpdated(this.props.color);
    }
}

export class OWLCategColorField extends Component {
    static supportedFieldTypes = ['integer'];
    static template = 'OWLFieldColorPills';
    static components = { ColorPill };
    setup() {
        this.totalColors = [1,2,3,4,5,6];
        onWillStart(async() => {
            await this.loadCategInformation();
        });
        onWillUpdateProps(async() => {
            await this.loadCategInformation();
        });
        super.setup();
    }
    colorUpdated(value) {
        this.props.update(value);
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
registry.category("fields").add("category_color", OWLCategColorField);

