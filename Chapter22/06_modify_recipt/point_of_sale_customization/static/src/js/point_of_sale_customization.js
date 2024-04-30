/** @odoo-module */

import { Order } from "@point_of_sale/app/store/models";
import { patch } from "@web/core/utils/patch";

patch(Order.prototype, {
    saved_amount(){
        const order = this;
        return order.orderlines.reduce((rem, line) => {
            var diffrence = (line.product.lst_price * line.quantity) - line.get_base_price();
            return rem + diffrence;
        }, 0);
    },
    export_for_printing() {
        const json = super.export_for_printing(...arguments);
        var savedAmount = this.saved_amount();
        if (savedAmount > 0) {
            json.saved_amount = this.env.utils.formatCurrency(savedAmount);
        }
        return json;
    }
})
