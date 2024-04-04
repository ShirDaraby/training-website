odoo.define("website_airproof_ecommerce.AirproofNavActive", function (require) {
    "use strict";
    const publicWidget = require('web.public.widget');
  
    publicWidget.registry.Loading = publicWidget.Widget.extend({
        selector: '#wrapwrap',

        start: function () {

            var URL = window.location.pathname;
            var arr = URL.split('/');
            var current_url = arr[1];

            if (current_url) {
                var menu_item = document.querySelector('a[href*="/'+current_url+'"]')
                var menu_item2 = document.querySelector('a[href="'+URL+'"]')
                var menu_item3 = document.querySelector('span[data-oe-xpath="'+URL+'"]')
                console.log(menu_item3)
                if (menu_item.closest('.dropdown')) {
                    var parent_item = menu_item.closest('.dropdown')
                    if( parent_item && !(menu_item.closest('.js_language_selector'))) {
                        parent_item.classList.add('x_underline')
                    }
                }  else if (menu_item2.closest('.dropdown')) {
                    var parent_item = menu_item2.closest('.dropdown')
                    if( parent_item && !(menu_item.closest('.js_language_selector'))) {
                        parent_item.classList.add('x_underline')
                    }

                }
            }
        }
    });
});

