from xmlrpc import client

# room data with search_read method
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
        'hostel.room', 'search_read',
        [search_domain, ['name', 'room_no']],
        {'limit': 5})
    print('Rooms data:', rooms_ids)

else:
    print('Wrong credentials')
