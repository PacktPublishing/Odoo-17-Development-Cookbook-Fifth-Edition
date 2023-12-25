/** @odoo-module */

import { Component } from "@odoo/owl";
import { ErrorPopup } from "@point_of_sale/app/errors/popups/error_popup";
import { ProductScreen } from "@point_of_sale/app/screens/product_screen/product_screen";
import { SelectionPopup } from "@point_of_sale/app/utils/input_popups/selection_popup";
import { usePos } from "@point_of_sale/app/store/pos_hook";
import { useService } from "@web/core/utils/hooks";
import { sprintf } from "@web/core/utils/strings";
import { patch } from "@web/core/utils/patch";

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

export class PosLastOrderButton extends Component {
    static template = "PosLastOrderButton";
    setup() {
        this.pos = usePos();
        this.popup = useService("popup");
    }
    async onClick() {
        var self = this;
        const order = this.pos.get_order();
        const client = order.get_partner();
        if (client) {
            var domain = [['partner_id', '=', client.id]];
            const orders = await this.pos.orm.call(
                "pos.order",
                "search_read",
                [],
                {
                    domain: domain,
                    fields: ['name', 'amount_total'],
                    limit:5
                }
            );
            if (orders.length > 0) {
                var order_list = orders.map((o) => {
                    return { 'label': sprintf("%s -TOTAL: %s", o.name, o.amount_total) };
                });
                await this.popup.add(SelectionPopup, {
                    title: 'Last 5 orders',
                    list: order_list
                });
            } else {
                await this.popup.add(ErrorPopup, {
                    body: "No previous orders found"
                });
            }
        } else {
            await this.popup.add(ErrorPopup, {
                body: "No previous orders found"
            });
        }
    }
}
ProductScreen.addControlButton({
    component: PosLastOrderButton,
    condition: function () {
        return true;
    },
});
patch(ProductScreen.prototype, {
    _setValue(val) {
        super._setValue(val);
        const orderline = this.currentOrder.get_selected_orderline();
        if (orderline && orderline.product.standard_price) {
            var price_unit = orderline.get_unit_price() * (1.0 - (orderline.get_discount() / 100.0));
            if (orderline.product.standard_price > price_unit) {
                this.popup.add(ErrorPopup, {
                    title: 'Warning', 
                    body: 'Product price set below cost of product.' 
                });
            }
        }
    }
});
