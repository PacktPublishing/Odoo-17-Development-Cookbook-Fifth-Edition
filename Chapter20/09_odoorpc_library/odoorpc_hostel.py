import odoorpc

db_name = 'cookbook_16e'
user_name = 'admin'
password = 'admin'

# Prepare the connection to the server
odoo = odoorpc.ODOO('localhost', port=8016)
odoo.login(db_name, user_name, password)  # login

# User information
user = odoo.env.user
print(user.name)             # name of the user connected
print(user.company_id.name)  # the name of user's company
print(user.email)            # the email of usser

RoomModel = odoo.env['hostel.room']
search_domain = [['name', 'ilike', 'Standard']]
rooms_ids = RoomModel.search(search_domain, limit=5)
for room in RoomModel.browse(rooms_ids):
    print(room.name, room.room_no)

# create the room and update the state
room_id = RoomModel.create({
    'name': 'Test Room',
    'room_no': '103',
    'state': 'draft'
})
print("Room state before make_available:", room.state)
room = RoomModel.browse(room_id)
room.make_available()
room = RoomModel.browse(room_id)
print("Room state after make_available:", room.state)
