
{
    # Module information
    'name': 'My Hostel',
    'version': '17.0.1.0.1',
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
        "security/hostel_security.xml",
        "security/ir.model.access.csv",
        "views/hostel.xml",
        "views/hostel_room.xml",
        "views/hostel_student.xml",
    ],

    'assets': {
        'web.assets_backend': [
            'my_hostel/static/src/js/component.js',
        ],
    },

    # Technical
    'installable': True,
    'auto_install': False,
}

