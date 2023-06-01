/** @odoo-module **/

import { _lt } from "@web/core/l10n/translation";
import { registry } from "@web/core/registry";
import { M2mGroupArchParser } from "./m2m_group_arch_parser";
import { M2mGroupController } from "./m2m_group_controller";
import {  M2mGroupModel } from "./m2m_group_model";
import { M2mGroupRenderer } from "./m2m_group_renderer";

const viewRegistry = registry.category("views");

export const M2mGroupView = {
    type: "m2m_group",
    display_name: _lt("Author"),
    icon: "fa fa-id-card-o",
    multiRecord: true,
    Controller: M2mGroupController,
    Renderer: M2mGroupRenderer,
    Model: M2mGroupModel,
    ArchParser: M2mGroupArchParser,
    searchMenuTypes: ["filter", "favorite"],
    buttonTemplate: "ViewM2mGroup.buttons",
    props: (genericProps, view) => {
        const modelParams = {};
        const { arch, fields, resModel } = genericProps;
        // parse arch
        const archInfo = new view.ArchParser().parse(arch);
        modelParams.metaData = {
            m2m_field: archInfo.m2m_field,
            fields: fields,
            fieldAttrs: archInfo.fieldAttrs,
            resModel: resModel,
            title: archInfo.title || _lt("Untitled"),
            widgets: archInfo.widgets,
        };
        return {
            ...genericProps,
            Model: view.Model,
            modelParams,
            Renderer: view.Renderer,
            buttonTemplate: view.buttonTemplate,
        };
    },
};
viewRegistry.add("m2m_group", M2mGroupView);

