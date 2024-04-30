/** @odoo-module **/

import { _t } from "@web/core/l10n/translation";
import publicWidget from "@web/legacy/js/public/public_widget";


publicWidget.registry.HostelSnippet = publicWidget.Widget.extend({
    selector: '.hostel_snippet',
    disabledInEditableMode: false,
    
    start: function () {
        var self = this;
        var rows = this.$el[0].dataset.numberOfRooms || '5';
        /*this.$el.find('td').parents('tr').remove();*/
        this.orm.call("hostel.hostel", "search_read", [
        ]).then(function (data) {
            _.each(data, function (hostel) {
                self.$el.append(
                    $('<tr />').append(
                        $('<td />').text(hostel.name),
                        $('<td />').text(hostel.hostel_code)
                    ));
            });
        });
    },
});