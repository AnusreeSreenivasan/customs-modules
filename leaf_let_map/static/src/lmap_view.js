/** @odoo-module **/

import { registry } from "@web/core/registry";
import { Component } from "@odoo/owl";
import { xml } from "@odoo/owl";

class LeafletMapController extends Component {
    
    setup() {
        console.log("LeafletMapController is initialized");
    }
    
    static template = xml`<div>Leaflet Map View</div>`;
}

const leafletMapView = {
    type: "lmap",
    display_name: "Leaflet Map",
    icon: "fa fa-map-maker",
    multiRecord: true,
    controller: LeafletMapController, }

registry.category("views").add("lmap", leafletMapView);