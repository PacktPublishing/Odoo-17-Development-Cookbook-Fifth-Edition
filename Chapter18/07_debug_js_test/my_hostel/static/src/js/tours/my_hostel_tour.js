/** @odoo-module **/

import { _t } from "@web/core/l10n/translation";
import { registry } from "@web/core/registry";
import { stepUtils } from "@web_tour/tour_service/tour_utils";
import { markup } from "@odoo/owl";


registry.category("web_tour.tours").add("hostel_tour", {
    url: "/web",
    rainbowMan: false,
    sequence: 20,
    steps: () => [stepUtils.showAppsMenuItem(), {
    trigger: '.o_app[data-menu-xmlid="my_hostel.hostel_base_menu"]',
    content: markup(_t("Ready to launch your <b>Hostel</b>?")),
    position: 'bottom',
    edition: 'community',
}, {
    trigger: '.o_app[data-menu-xmlid="my_hostel.hostel_base_menu"]',
    content: markup(_t("Ready to launch your <b>Hostel</b>?")),
    position: 'bottom',
    edition: 'enterprise',
}, {
    trigger: '.o_list_button_add',
    content: markup(_t("Let's create new room.")),
    position: 'bottom',
}, {
    trigger: ".o_form_view .o_field_char[name='name']",
    content: markup(_t('Add a new <b> Hostel Room </b>.')),
    position: "top",
    run: function (actions) {
        actions.text("Hostel Room 01", this.$anchor.find("input"));
    },
}, {
    trigger: ".ui-menu-item > a",
    auto: true,
    in_modal: false,
}, {
    trigger: ".breadcrumb-item:not(.active):first",
    content: _t("Click on the breadcrumb to go back to your Pipeline. Odoo will save all modifications as you navigate."),
    position: "bottom",
    run: function (actions) {
        actions.auto(".breadcrumb-item:not(.active):last");
    },
},]});
