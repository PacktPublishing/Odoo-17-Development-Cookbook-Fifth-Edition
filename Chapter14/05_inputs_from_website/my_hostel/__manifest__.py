{
    "name": "Hostel Management",  # Module title
    "summary": "Manage Hostel easily",  # Module subtitle phrase
    "description": """
Manage Hostel
==============
Display Hostel records in the web page.
    """,  # Supports reStructuredText(RST) format (description is Deprecated)
    "version": "17.0.1.0.0",
    "author": "Serpent Consulting Services Pvt. Ltd.",
    "category": "Tools",
    "website": "http://www.serpentcs.com",
    "license": "AGPL-3",
    "depends": ['base','website'],
    "data": [
        "security/hostel_security.xml",
        "security/ir.model.access.csv",
        "views/hostel.xml",
        "views/hostel_template.xml",
        "views/custom_template.xml",
        "views/snippets.xml",
        "views/inquiries_view.xml",
        "views/form_template.xml",
    ],
    # This demo data files will be loaded if db initialize with demo data (commented because file is not added in this example)
    # 'demo': [
    #     'demo.xml'
    # ],
    'assets': {
        'web.assets_frontend': [
            # 'my_hostel/static/src/js/snippets.js',
        ],
    },
    "installable": True,
}
