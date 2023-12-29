/** @odoo-module **/

import { visitXML } from "@web/core/utils/xml";

export class M2mGroupArchParser {
    parse(arch, fields = {}) {
        const archInfo = { fields, fieldAttrs: {} };
        visitXML(arch, (node) => {
            switch (node.tagName) {
                case "m2m_group": {
                    const m2m_field = node.getAttribute("m2m_field");
                    if (m2m_field) {
                        archInfo.m2m_field = m2m_field;
                    }
                    const title = node.getAttribute("string");
                    if (title) {
                        archInfo.title = title;
                    }
                    break;
                }
                case "field": {
                    const fieldName = node.getAttribute("name"); // exists (rng validation)
                    if (fieldName === "id") {
                        break;
                    }
                    const string = node.getAttribute("string");
                    if (string) {
                        if (!archInfo.fieldAttrs[fieldName]) {
                            archInfo.fieldAttrs[fieldName] = {};
                        }
                        archInfo.fieldAttrs[fieldName].string = string;
                    }
                    const modifiers = JSON.parse(node.getAttribute("modifiers") || "{}");
                    if (modifiers.invisible === true) {
                        if (!archInfo.fieldAttrs[fieldName]) {
                            archInfo.fieldAttrs[fieldName] = {};
                        }
                        archInfo.fieldAttrs[fieldName].isInvisible = true;
                        break;
                    }
                    break;
                }
            }
        });
        return archInfo;
    }
}
