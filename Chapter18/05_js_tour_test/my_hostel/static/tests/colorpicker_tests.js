/** @odoo-module */

import { registry } from "@web/core/registry";
import { session } from "@web/session";
import { uiService } from "@web/core/ui/ui_service";
import { makeView, setupViewRegistries} from "@web/../tests/views/helpers";
import { click, getFixture, patchWithCleanup } from "@web/../tests/helpers/utils";

const serviceRegistry = registry.category("services");

QUnit.module("Color Picker Widget Tests", (hooks) => {
    let serverData;
    let target;
    hooks.beforeEach(async function (assert) {
        target = getFixture();
        serverData = {
            models: {
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
            },
            views: {
                "hostel.room,false,form": `<form>
                    <field name="name"/>
                    <field name="room_no"/>
                    <field name="color" widget="int_color"/>
                </form>`,
            },
        };
        serviceRegistry.add("ui", uiService);
        setupViewRegistries();
    });

    QUnit.module("IntColorField");

    QUnit.test("factor is applied in IntColorField", async function (assert) {
        const form = await makeView({
            serverData,
            type: "form",
            resModel: "hostel.room",
        });

        assert.containsOnce(target, '.o_field_int_color');

        assert.strictEqual(target.querySelectorAll(".o_int_color .o_color_pill").length, 10, "Color picker should have 10 pills");

        await click(target.querySelectorAll(".o_int_color .o_color_pill")[3]);

        assert.strictEqual(target.querySelector('.o_int_color .o_color_4').classList.contains("active"), true, "Click on pill should make pill active");
    });

});
