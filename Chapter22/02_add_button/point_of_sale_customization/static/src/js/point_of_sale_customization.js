/** @odoo-module */

import { Component } from "@odoo/owl";
import { ProductScreen } from "@point_of_sale/app/screens/product_screen/product_screen";
import { usePos } from "@point_of_sale/app/store/pos_hook";

export class PosDiscountButton extends Component {
    static template = "PosDiscountButton";
    setup() {
        this.pos = usePos();
    }
    async onClick() {
        const order = this.pos.get_order();
        if (order.selected_orderline) {
            order.selected_orderline.set_discount(5);
        }
    }
}
ProductScreen.addControlButton({
    component: PosDiscountButton,
    condition: function () {
        return true;
    },
});

