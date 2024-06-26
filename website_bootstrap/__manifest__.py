{
   'name': 'bootstrap Theme',
   'description': 'bootstrap Theme',
   # add the version of Odoo
   'category': 'website/theme',
   # dependencies: add 'website_sale' and 'website_sale_wishlist' ('website' will be installed by default as a dependency)
   'depends': ['website','website_sale', 'website_sale_wishlist'],
   # add the licence : OEEL-1 (Odoo Enterprise Edition License v1.0)
   # I think you need to add your thumbnail here: to test
   'images': [
        'static/description/clean_screenshot.jpg',
    ],
   # 'license': ['OEEL-1'],
   'data': [
      # 'views/website_templates.xml', 
   ],

    'assets': {
    'web._assets_primary_variables': [
      ('prepend', 'website_bootstrap/static/src/scss/primary_variables.scss'),
   ],
},
}