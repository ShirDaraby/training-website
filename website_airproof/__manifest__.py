{
   'name': 'Airproof Theme',
   'description': 'Airproof Theme',
   # add the version of Odoo
   'category': 'Theme/Hidden',
   # dependencies: add 'website_sale' and 'website_sale_wishlist' ('website' will be installed by default as a dependency)
   'depends': ['website'],
   # add the licence : OEEL-1 (Odoo Enterprise Edition License v1.0)
   # I think you need to add your thumbnail here: to test
   #'images': [
        #'static/description/clean_screenshot.jpg',
    #],
   'data': [
      # 'data/ir_asset.xml',
      'data/menu.xml',
      'data/presets.xml',
      'data/images.xml',
      'views/website_templates.xml', 
   ],
    'assets': {
    'web._assets_primary_variables': [
      'website_airproof/static/src/scss/primary_variables.scss',
      'website_airproof/static/src/scss/fonts.scss',
      'website_airproof/static/src/scss/bootstrap_overridden.scss',
      'website_airproof/static/src/scss/theme.scss',
      # 'website_airproof/static/src/scss/theme.scss',
   ],
},
}
