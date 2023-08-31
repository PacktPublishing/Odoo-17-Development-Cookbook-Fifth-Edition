from xmlrpc import client

server_url = 'http://localhost:8016'
db_name = 'cookbook_16e'
username = 'admin'
password = 'admin'

common = client.ServerProxy('%s/xmlrpc/2/common' % server_url)
user_id = common.authenticate(db_name, username, password, {})

models = client.ServerProxy('%s/xmlrpc/2/object' % server_url)

if user_id:
    # Create room with state draft
    room_id = models.execute_kw(db_name, user_id, password,
        'hostel.room', 'create',
        [{
            'name': 'New Room',
            'room_no': '35',
            'state': 'draft'
        }])
    print('\n\n\n room_id',room_id)
    # Call make_available method on new room
    models.execute_kw(db_name, user_id, password,
        'hostel.room', 'make_available',
        [[room_id]])

    # check room status after method call
    room_data = models.execute_kw(db_name, user_id, password,
        'hostel.room', 'read',
        [[room_id], ['name', 'state']])
    print('Room state after method call:', room_data[0]['state'])
else:
    print('Wrong credentials')
