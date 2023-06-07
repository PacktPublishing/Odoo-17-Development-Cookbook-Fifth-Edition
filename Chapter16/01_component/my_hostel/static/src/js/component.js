odoo.define('my_hostel.component', function (require) {
    "use strict";

    console.log("Load component......");
    const {  Component, mount, xml, whenReady } = owl;

    class MyComponent extends Component {
        static template = xml`
            <div class="bg-info text-white text-center p-3">
                <b> Welcome To Odoo </b>
            </div>`
    }
    whenReady().then(() => {
        mount(MyComponent, document.body);
    });

});