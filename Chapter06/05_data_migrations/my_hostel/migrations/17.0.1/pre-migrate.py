# -*- coding: utf-8 -*-

# NOTE: This is just for demo purpose
# This function invoked only if system already have 14.0.0 version installed
def migrate(cr, version):
    cr.execute("""
        ALTER TABLE hostel_room
        RENAME COLUMN allocation_date TO allocation_date_char""")
