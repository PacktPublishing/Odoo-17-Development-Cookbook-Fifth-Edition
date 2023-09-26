/** @odoo-module **/

import FormView from 'web.FormView';
import testUtils from 'web.test_utils';
import { makeView, setupViewRegistries } from "@web/../tests/views/helpers";
import { getFixture } from "@web/../tests/helpers/utils";

const createView = testUtils.createView;
let target;

QUnit.module('fields', {
    beforeEach: function () {
        this.data = {
            'hostel.room': {
                fields: {
                    name: { string: "Hostel Name", type: "char" },
                    room_no: { string: "Room Number", type: "char" },
                    color: { string: "color", type: "integer"},
                },
                records: [{
                    id: 1,
                    name: "Hostel Room 01",
                    room_no: 1,
                    color: 1,
                }, {
                    id: 2,
                    name: "Hostel Room 02",
                    room_no: 2,
                    color: 3
                }],
            },
        };
        setupViewRegistries();
        this.target = getFixture();
    }
}, function () {

    QUnit.module('IntColorField');

    QUnit.test('int_color field test cases', async function (assert) {
        var form = await createView({
            View: FormView,
            model: 'hostel.room',
            data: this.data,
            debug:true,
            res_id: 1,
            arch: '<form><field name="name"/><field name="room_no"/><field name="color" widget="int_color"/></form>',
        });

        form.destroy();
    });
});
