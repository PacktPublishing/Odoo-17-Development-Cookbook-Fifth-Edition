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
    "depends": ["base"],
    'data': [
        'security/groups.xml',

    ],
    # This demo data files will be loaded if db initialize with demo data (commented because file is not added in this example)
    # 'demo': [
    #     'demo.xml'
    # ],
    "installable": True,
}
