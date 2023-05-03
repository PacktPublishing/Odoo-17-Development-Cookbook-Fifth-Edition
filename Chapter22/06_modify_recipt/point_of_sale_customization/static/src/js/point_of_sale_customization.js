odoo.define('point_of_sale_customization.point_of_sale_customization', function (require) {
    "use strict";

    const { Order } = require('point_of_sale.models');
    const PosComponent = require('point_of_sale.PosComponent');
    const ProductScreen = require('point_of_sale.ProductScreen');
    const Registries = require('point_of_sale.Registries');
    const { sprintf } = require("web.utils");

    class PosDiscountButton extends PosComponent {
        async onClick() {
            const order = this.env.pos.get_order();
            if (order.selected_orderline) {
                order.selected_orderline.set_discount(5);
            }
        }
    }
    PosDiscountButton.template = 'PosDiscountButton';
    ProductScreen.addControlButton({
        component: PosDiscountButton,
        condition: function () {
            return true;
        },
    });
    Registries.Component.add(PosDiscountButton);

    class PosLastOrderButton extends PosComponent {
        async onClick() {
            var self = this;
            const order = this.env.pos.get_order();
            const client = order.get_partner();
            if (client) {
                var domain = [['partner_id', '=', client.id]];
                this.rpc({
                    model: 'pos.order',
                    method: 'search_read',
                    args: [domain, ['name', 'amount_total']],
                    kwargs: { limit: 5 },
                }).then(function (orders) {
                    if (orders.length > 0) {
                        var order_list = orders.map((o) => {
                            return { 'label': sprintf("%s -TOTAL: %s", o.name, o.amount_total) };
                        });
                        self.showPopup('SelectionPopup', { title:'Last 5 orders', list:order_list });
                    } else {
                        self.showPopup('ErrorPopup', { body: 'No previous orders found' });
                    }
                });
            } else {
                self.showPopup('ErrorPopup', { body: 'Please select the customer' });
            }
        }
     }
     PosLastOrderButton.template = 'PosLastOrderButton';
     ProductScreen.addControlButton({
         component: PosLastOrderButton,
         condition: function () {
             return true;
         },
     });
     Registries.Component.add(PosLastOrderButton);

     const UpdatedProductScreen = ProductScreen =>
     class extends ProductScreen {
         _setValue(val) {
             super._setValue(val);
             const orderline = this.env.pos.get_order().selected_orderline;
             if (orderline && orderline.product.standard_price) {
                 var price_unit = orderline.get_unit_price() * (1.0 - (orderline.get_discount() / 100.0));
                 if (orderline.product.standard_price > price_unit) {
                     this.showPopup('ErrorPopup', { 
                         title: 'Warning', 
                         body: 'Product price set below cost of product.' 
                     });
                 }
             }
         }
     };
     Registries.Component.extend(ProductScreen, UpdatedProductScreen);

     const PosDemoOrder = (Order) => class PosDemoOrder extends Order {
         export_for_printing() {
             const json = super.export_for_printing(...arguments);
             var savedAmount = this.saved_amount();
             if (savedAmount > 0) {
                 json.saved_amount = this.pos.format_currency(savedAmount);
             }
             return json;
         }
         saved_amount(){
             const order = this.pos.get_order();
             return order.orderlines.reduce((rem, line) => {
                 var diffrence = (line.product.lst_price * line.quantity) - line.get_base_price();
                 return rem + diffrence;
             }, 0);
         }
     };
     Registries.Model.extend(Order, PosDemoOrder);

    return PosDiscountButton;

});
