from xmlrpc import client

# room data with search method
server_url = 'http://localhost:8017'
db_name = 'cookbook_17e'
username = 'admin'
password = 'admin'

common = client.ServerProxy('%s/xmlrpc/2/common' % server_url)
user_id = common.authenticate(db_name, username, password, {})

models = client.ServerProxy('%s/xmlrpc/2/object' % server_url)

if user_id:
    search_domain = [['name', 'ilike', 'Standard']]
    rooms_ids = models.execute_kw(db_name, user_id, password,
        'hostel.room', 'search',
        [search_domain],
        {'limit': 5})
    print('Rooms ids found:', rooms_ids)

    rooms_data = models.execute_kw(db_name, user_id, password,
        'hostel.room', 'read',
        [rooms_ids, ['name', 'room_no']])
    print("Rooms data:", rooms_data)
else:
    print('Wrong credentials')
