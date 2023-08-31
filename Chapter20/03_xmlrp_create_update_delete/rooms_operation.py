from xmlrpc import client

server_url = 'http://localhost:8016'
db_name = 'cookbook_16e'
username = 'admin'
password = 'admin'

common = client.ServerProxy('%s/xmlrpc/2/common' % server_url)
user_id = common.authenticate(db_name, username, password, {})

models = client.ServerProxy('%s/xmlrpc/2/object' % server_url)

if user_id:
    # create new room records.
    create_data = [
        {'name': 'Room 1', 'room_no': '101'},
        {'name': 'Room 3', 'room_no': '102'},
        {'name': 'Room 5', 'room_no': '103'},
        {'name': 'Room 7', 'room_no': '104'}
    ]
    rooms_ids = models.execute_kw(db_name, user_id, password,
        'hostel.room', 'create',
        [create_data])
    print("Rooms created:", rooms_ids)

    # Write in existing room record
    room_to_write = rooms_ids[1]  # We will use ids of recently created rooms
    write_data = {'name': 'Room 2'}
    written = models.execute_kw(db_name, user_id, password,
        'hostel.room', 'write',
        [room_to_write, write_data])
    print("Rooms written", written)

    # Delete the room record
    rooms_to_delete = rooms_ids[2:]
    deleted = models.execute_kw(db_name, user_id, password,
        'hostel.room', 'unlink',
        [rooms_to_delete])
    print('Rooms unlinked:', deleted)

else:
    print('Wrong credentials')
