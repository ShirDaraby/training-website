{
    'name': 'Airproof E-Commerce Theme',
    'summary': '',
    'description': '',
    'category': 'Website/Theme',
    'version': '15.2.0',
    'depends': ['website_sale', 'website_sale_wishlist'],
    # 'depends': ['website', 'website_sale', 'website_sale_comparison', 'website_sale_wishlist', 'website_sale_product_configurator'],
    'license': 'OEEL-1',
    'data': [
        # Options
        'data/presets.xml',
        # Menu
        'data/menu.xml',
        # Shapes 
        'data/shapes.xml', 
        # Pages
        'data/pages/home.xml',
        'data/pages/about.xml',
        'data/pages/contact.xml',
        'data/pages/404.xml',
        # Frontend
        'views/website_templates.xml',
        'views/website_sale_templates.xml',
        'views/portal_templates.xml',
        # Snippets
        'views/snippets/options.xml',
        'views/snippets/s_airproof_newsletter.xml',
        # Data
        'data/data.xml',
        # Images
        'data/images.xml',
    ],
    'assets': {
        'web._assets_primary_variables': [
            'website_airproof_ecommerce/static/src/scss/primary_variables.scss',
        ],
        'web._assets_frontend_helpers': [
            ('prepend', 'website_airproof_ecommerce/static/src/scss/bootstrap_overridden.scss'),
        ],
        'web.assets_frontend': [
            #SCSS
            'website_airproof_ecommerce/static/src/scss/homepage.scss',
            'website_airproof_ecommerce/static/src/scss/header.scss',
            'website_airproof_ecommerce/static/src/scss/carousels.scss',
            'website_airproof_ecommerce/static/src/scss/eshop.scss',
            'website_airproof_ecommerce/static/src/scss/product_page.scss',
            'website_airproof_ecommerce/static/src/scss/theme.scss',
            'website_airproof_ecommerce/static/src/snippets/s_airproof_newsletter/000.scss',
            # JS
            'website_airproof_ecommerce/static/src/js/theme.js',
        ],
    },
}
