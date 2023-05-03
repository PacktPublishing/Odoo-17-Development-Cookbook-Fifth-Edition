
{
    'name': 'POS Customization',
    'version': '16.0.1.0.0',
    'category': 'Point of Sale',
    'description': """
        POS Customization
    """,
    'summary': """
        POS Customization
    """,
    "author": "Serpent Consulting Services Pvt. Ltd.",
    "website": "http://www.serpentcs.com",
    "license": "AGPL-3",
    'depends': ['point_of_sale'],
    'assets': {
        'point_of_sale.assets': [
            'point_of_sale_customization/static/src/js/point_of_sale_customization.js',
            'point_of_sale_customization/static/src/scss/point_of_sale_customization.scss',
            'point_of_sale_customization/static/src/xml/point_of_sale_customization.xml',
        ],
    },
    'installable': True,
    'auto_install': False,
}
