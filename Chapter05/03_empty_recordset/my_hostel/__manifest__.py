# -*- coding: utf-8 -*-
{
    'name': "My Hostel",  # Module title
    'summary': "Manage Hostel easily",  # Module subtitle phrase
    'description': """
Manage Library
==============
Description related to Hostel.
    """,  # Supports reStructuredText(RST) format
    "version": "1.0",
    "author": "Serpent Consulting Services Pvt. Ltd.",
    "category": "Tools",
    "website": "http://www.serpentcs.com",
    "depends": ['base'],
    "license": "AGPL-3",
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/hostel_room.xml',
    ],
}
