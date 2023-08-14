odoo.define('my_hostel.tour', function(require) {
    "use strict";

    const {_t} = require('web.core');
    const {Markup} = require('web.utils');
    var tour = require('web_tour.tour');

    tour.register('hostel_tour', {
        url: "/web",
        rainbowMan: false,
        sequence: 5,
    }, [tour.stepUtils.showAppsMenuItem(), {
        trigger: '.o_app[data-menu-xmlid="my_hostel.hostel_main_menu"]',
        content: Markup(_t("Ready to launch your <b>hostel</b>?")),
        position: 'bottom',
    },{
        trigger: '.o_list_button_add',
        content: Markup(_t("Let's create new room.")),
        position: "bottom"
    },{
        trigger: '.o_form_button_save',
        content: Markup(_t('Save this room record')),
        position: 'bottom',
    }]);

});