{
    "name": "Hostel Management",  # Module title
    "summary": "Manage Hostel easily",  # Module subtitle phrase
    "description": """
Manage Hostel
==============
Efficiently manage the entire residential facility in the school
    """,  # Supports reStructuredText(RST) format (description is Deprecated)
    "version": "16.0.1.0.0",
    "author": "Serpent Consulting Services Pvt. Ltd.",
    "category": "Hostel",
    "website": "http://www.serpentcs.com",
    "license": "AGPL-3",
    "depends": ["base_setup"],
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'security/security_rules.xml',
        'views/hostel_room.xml',
        'views/hostel_room_category.xml'
    ],
    "installable": True,
}
