/** @odoo-module **/
import { getFixture } from "@web/../tests/helpers/utils";
import { makeView, setupViewRegistries } from "@web/../tests/views/helpers";

QUnit.module('IntColorField Tests', {}, function() {

    QUnit.module("Fields");

    QUnit.test('render color field', async function (assert) {
        assert.expect(1);
        let target = getFixture();
        setupViewRegistries();

        await makeView({
            type: "form",
            resModel: "hostel.room",
            serverData: {
                models: {
                    'hostel.room': {
                        fields: {
                            name: { string: "Hostel Name", type: "char" },
                            room_no: { string: "Room Number", type: "char" },
                            color: { string: "color", type: "integer"},
                        },
                        records: [
                            {
                                id: 1,
                                name: "Hostel Room 01",
                                room_no: 1,
                                color: 1,
                            },
                            {
                                id: 2,
                                name: "Hostel Room 02",
                                room_no: 2,
                                color: 3
                            }
                        ],
                    },
                },
                views: { },
            },
            arch: `
            <form>
                <field name="name"/>
                <field name="room_no"/>
                <field name="color" widget="int_color"/>
            </form>`,
        });
        assert.containsN(
            target,
            ".o_field_int_color",
            1,
            "Both records are rendered"
        );
    });
});
