/** @odoo-module **/

import { _t } from "@web/core/l10n/translation";
import publicWidget from "@web/legacy/js/public/public_widget";


publicWidget.registry.MyHostel = publicWidget.Widget.extend({
    selector: '#wrapwrap',

    init() {
        this._super(...arguments);
        this.orm = this.bindService("orm");
        alert(_t('Hello world'));
    },
});