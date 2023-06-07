
{
    # Module information
    'name': 'My Hostel',
    'version': '16.0.1.0.1',
    'category': 'Extra Tools',
    'license': 'LGPL-3',
    'summary': """
        Odoo16 Book
    """,

    # Author
    'author': 'Serpent Consulting Services Pvt. Ltd.',
    'website': 'http://www.serpentcs.com',

    # Dependancies
    'depends': ['web', 'base'],

    # Views
    'data': [
        "views/hostel_room.xml",
    ],

    # Technical
    'installable': True,
    'auto_install': False,
}

