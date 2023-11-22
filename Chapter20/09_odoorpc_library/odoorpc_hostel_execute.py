import odoorpc

db_name = 'cookbook_17e'
user_name = 'admin'
password = 'admin'

# Prepare the connection to the server
odoo = odoorpc.ODOO('localhost', port=8017)
odoo.login(db_name, user_name, password)  # login

rooms_info = odoo.execute('hostel.room', 'search_read',
    [['name', 'ilike', 'Standard']])
print(rooms_info)
