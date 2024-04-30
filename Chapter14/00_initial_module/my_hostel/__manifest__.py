# -*- coding: utf-8 -*-
{
    'name': "My Hostel",
    'summary': "Manage the Hostel",
    'website': "",
    'category': 'Website',
    'version': '16.0.1',
    'author': "",
    'depends': ['base', 'website'],
    'data': [
        # load views and templates here...
    ],
    'assets': {
        'web.assets_frontend': [
            'my_hostel/static/src/scss/hostel.scss',
            'my_hostel/static/src/js/hostel.js',
        ],
    },
}
