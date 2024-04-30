
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
            'my_hostel/static/src/scss/field_widget.scss',
            'my_hostel/static/src/js/field_widget.js',
            'my_hostel/static/src/xml/field_widget.xml',
            'my_hostel/static/src/js/m2m_group_arch_parser.js',
            'my_hostel/static/src/js/m2m_group_view.js',
            'my_hostel/static/src/js/m2m_group_renderer.js',
            'my_hostel/static/src/js/m2m_group_model.js',
            'my_hostel/static/src/js/m2m_group_controller.js',
            'my_hostel/static/src/xml/m2m_group_controller.xml',
            'my_hostel/static/src/xml/m2m_group_renderer.xml',
            'my_hostel/static/src/xml/m2m_group_view.xml',
        ],
     },

    # Technical
    'installable': True,
    'auto_install': False,
}

