odoo.define('tree_view_header_buttons_assets.tree_view_button', function (require){
    "use strict";
    console.log('require=', require);
    var ajax = require('web.ajax');
    var ListController = require('web.ListController');
    var rpc = require('web.rpc')

    ListController.include({
        renderButtons: function($node) {
            this._super.apply(this, arguments);
            var self = this;
            console.log('this.$buttons=', this.$buttons);
            if (this.$buttons) {
                $(this.$buttons).find('.oe_new_custom_button').on('click', function() {
                    //custom code
                    // console.log('===============', self);
                    // let rows = self.getSelectedIds()
                    // console.log('self.getSelectedIds()=,', rows.length, rows);
                    rpc.query({
                        model: 'log.book',
                        method: 'action_print_pdf',
                        args: [self.getSelectedIds()],
                    }).then(function(res){
                        // console.log(res)
                        // self.reload();
                    })
                });
            }
        },
    });
});