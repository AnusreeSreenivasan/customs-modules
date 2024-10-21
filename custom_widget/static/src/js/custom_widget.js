odoo.define('custom_widget.ColorPickerWidget', function (require) {
    "use strict";

    var AbstractField = require('web.AbstractField');
    var fieldRegistry = require('web.field_registry');

    var ColorPickerWidget = AbstractField.extend({
        supportedFieldTypes: ['char'],  // Adjust based on your needs

        _render: function () {
            this.$el.html('<input type="color" class="color-picker" value="' + (this.value || '#ffffff') + '"/>');
            this.$('.color-picker').on('input', this._onColorChange.bind(this)); // Bind event
        },

        _onColorChange: function (event) {
            var colorValue = event.target.value;
            this._setValue(colorValue);  // Update the field value
            this.trigger_up('field_changed', { changes: { your_color_field: colorValue } }); // Notify Odoo
        },

        _setValue: function (value) {
            this._super(value);
        },
    });

    fieldRegistry.add('color_picker_widget', ColorPickerWidget);
});
