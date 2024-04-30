import json
import random
import requests


server_url = 'http://localhost:8017'
db_name = 'cookbook_17e'
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
    # Create the room record in draft state
    payload = get_json_payload("object", "execute_kw",
        db_name, user_id, password,
        'hostel.room', 'create', [{
            'name': 'Room 1',
            'room_no': '101',
            'state': 'draft'
        }])
    res = requests.post(json_endpoint, data=payload, headers=headers).json()
    print("Room created with id:", res['result'])
    room_id = res['result']

    # Change the room state by calling make_available method
    payload = get_json_payload("object", "execute_kw",
        db_name, user_id, password,
        'hostel.room', 'make_available', [room_id])
    res = requests.post(json_endpoint, data=payload, headers=headers).json()

    # Check the room status after method call
    payload = get_json_payload("object", "execute_kw",
        db_name, user_id, password,
        'hostel.room', 'read', [room_id, ['name', 'state']])
    res = requests.post(json_endpoint, data=payload, headers=headers).json()
    print("Room state after the method call:", res['result'])

else:
    print("Failed: wrong credentials")
