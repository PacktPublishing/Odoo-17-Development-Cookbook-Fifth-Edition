# -*- coding: utf-8 -*-
{
    'name': "My Hostel",  # Module title
    'summary': "Manage Hostel easily",  # Module subtitle phrase
    'description': """
Manage Library
==============
Description related to Hostel.
    """,  # Supports reStructuredText(RST) format
    "version": "16.0.1.0.0",
    "author": "Serpent Consulting Services Pvt. Ltd.",
    "category": "Tools",
    "website": "http://www.serpentcs.com",
    "depends": ['web', 'base', 'web_tour',],
    "license": "AGPL-3",
    'data': [
        'data/data.xml',
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/hostel_room.xml',
        'views/hostel_room_category_view.xml'
    ],
    'assets': {
        'web.assets_backend': [
            'my_hostel/static/src/scss/field_widget.scss',
            'my_hostel/static/src/js/field_widget.js',
            'my_hostel/static/src/js/tours/my_hostel_tour.js',
            'my_hostel/static/src/xml/field_widget.xml',
        ],
        'web.qunit_suite_tests': [
            'my_hostel/static/tests/**/*',
        ],
     },
    'installable': True,
    'application': True,
}
