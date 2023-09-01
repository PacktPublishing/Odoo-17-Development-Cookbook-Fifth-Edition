import json
import random
import requests


server_url = 'http://localhost:8016'
db_name = 'cookbook_16e'
username = 'admin'
password = 'admin'

json_endpoint = "%s/jsonrpc" % server_url
headers = {"Content-Type": "application/json"}


def get_json_payload(service, method, *args, **kwargs):
    kwargs = kwargs or {}
    return json.dumps({
        "jsonrpc": "2.0",
        "method": 'call',
        "params": {
            "service": service,
            "method": method,
            "args": args
        },
        "id": random.randint(0, 1000000000),
    })

payload = get_json_payload("common", "login", db_name, username, password)
response = requests.post(json_endpoint, data=payload, headers=headers)
user_id = response.json()['result']

if user_id:
    # creates the room's records
    create_data = [
        {'name': 'Room 1', 'room_no': '201'},
        {'name': 'Room 3', 'room_no': '202'},
        {'name': 'Room 5', 'room_no': '205'},
        {'name': 'Room 7', 'room_no': '207'}
    ]
    payload = get_json_payload("object", "execute_kw", db_name, user_id, password, 'hostel.room', 'create', [create_data])
    res = requests.post(json_endpoint, data=payload, headers=headers).json()
    print("Rooms created:", res)
    rooms_ids = res['result']

    # Write in existing room record
    room_to_write = rooms_ids[1]  # We will use ids of recently created rooms
    write_data = {'name': 'Room 2'}
    payload = get_json_payload("object", "execute_kw", db_name, user_id, password, 'hostel.room', 'write', [room_to_write, write_data])
    res = requests.post(json_endpoint, data=payload, headers=headers).json()
    print("Rooms written:", res)

    # Delete in existing room record
    room_to_unlink = rooms_ids[2:]  # We will use ids of recently created rooms
    payload = get_json_payload("object", "execute_kw", db_name, user_id, password, 'hostel.room', 'unlink', [room_to_unlink])
    res = requests.post(json_endpoint, data=payload, headers=headers).json()
    print("Rooms deleted:", res)

else:
    print("Failed: wrong credentials")
