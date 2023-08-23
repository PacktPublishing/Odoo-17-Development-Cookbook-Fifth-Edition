# -*- coding: utf-8 -*-
{
    'name': "My Hostel",  # Module title
    'summary': "Manage Hostel easily",  # Module subtitle phrase
    'description': """
Long description
    """,  # Supports reStructuredText(RST) format
    "version": "15.0.1.0.0",
    "author": "Serpent Consulting Services Pvt. Ltd.",
    "category": "Uncategorized",
    "website": "http://www.serpentcs.com",
    "depends": ['base'],
    "license": "AGPL-3",
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/hostel_room_category_view.xml',
        'views/hostel_room.xml',
    ],
}
