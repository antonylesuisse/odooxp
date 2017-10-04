odoo.define('web.Tyrell', function (require) {
"use strict";

var core = require('web.core');

var Tyrell = Widget.extend({
    init: function(parent, action) {
        this._super(parent, action);
        var options = action.params || {};
        this.params = options;  // NOTE forwarded to embedded client action
    },
});


return Tyrell;

});
