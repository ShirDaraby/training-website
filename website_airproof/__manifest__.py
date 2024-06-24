{
   'name': 'Airproof Theme',
   'description': 'Airproof Theme',
   # add the version of Odoo
   'category': 'Theme/Hidden',
   'license': 'OEEL-1',
   # dependencies: add 'website_sale' and 'website_sale_wishlist' ('website' will be installed by default as a dependency)
   'depends': ['website','website_sale', 'website_sale_wishlist'],
   # add the licence : OEEL-1 (Odoo Enterprise Edition License v1.0)
   # I think you need to add your thumbnail here: to test
   #'images': [
        #'static/description/clean_screenshot.jpg',
    #],
   # 'license': ['OEEL-1'],
   'data': [
      # 'data/ir_asset.xml',
      'data/data.xml',
      'data/menu.xml',
      'data/presets.xml',
      'data/images.xml',
      'data/shapes.xml',
      'views/website_templates.xml', 
      # Snippets
      'views/snippets/options.xml',
      'views/snippets/s_airproof_newsletter.xml',
      # Pages
      'data/pages/home.xml',
      # 'data/pages/about.xml',
      # 'data/pages/contact.xml',
      # 'data/pages/404.xml',
   ],
    'assets': {
    'web._assets_primary_variables': [
      'website_airproof/static/src/scss/primary_variables.scss',
      'website_airproof/static/src/scss/fonts.scss',
      'website_airproof/static/src/scss/bootstrap_overridden.scss',
      'website_airproof/static/src/scss/theme.scss',
      'website_airproof/static/src/scss/homepage.scss',
      'website_airproof/static/src/snippets/s_airproof_newsletter/000.scss',
      'website_airproof/static/src/snippets/s_airproof_test/000.scss',
   ],
},
}
