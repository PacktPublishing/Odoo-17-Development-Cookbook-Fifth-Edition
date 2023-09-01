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
    "category": "Tools",
    "website": "http://www.serpentcs.com",
    "license": "AGPL-3",
    "depends": ["mail", "contacts"],
    "data": [
        "security/hostel_security.xml",
        "security/ir.model.access.csv",
        "data/categ_data.xml",
        "data/mail_template.xml",
        "views/hostel.xml",
        "views/hostel_room.xml",
        "views/hostel_amenities.xml",
        "views/hostel_student.xml",
        "views/hostel_categ.xml",
        "views/hostel_room_category_view.xml",
    ],
    # This demo data files will be loaded if db initialize with demo data (commented because file is not added in this example)
    "demo": [
        'data/room_demo.xml'
    ],
    "installable": True,
}
