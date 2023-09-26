/** @odoo-module **/

import { _t } from 'web.core';
import { Markup } from 'web.utils';
import tour from 'web_tour.tour';


tour.register('hostel_tour', {
    url: "/web",
    rainbowManMessage: false,
    sequence: 5,
}, [tour.stepUtils.showAppsMenuItem(), {
    trigger: '.o_app[data-menu-xmlid="my_hostel.hostel_base_menu"]',
    content: Markup(_t("Ready to launch your <b>Hostel</b>?")),
    position: 'bottom',
    edition: 'community',
}, {
    trigger: '.o_app[data-menu-xmlid="my_hostel.hostel_base_menu"]',
    content: Markup(_t("Ready to launch your <b>Hostel</b>?")),
    position: 'bottom',
    edition: 'enterprise',
}, {
    trigger: '.o_list_button_add',
    content: Markup(_t("Let's create new room.")),
    position: 'bottom',
}, {
    trigger: ".o_form_view .o_field_char[name='name']",
    content: Markup(_t('Add a new <b> Hostel Room </b>.')),
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
    }
}]);
