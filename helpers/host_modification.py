import json


def add_host(data):
    name = input("Enter the name: ")
    username = input("Enter the username: ")
    address = input("Enter the address: ")
    port = int(input("Enter the port: "))

    new_host = {
        'name': name,
        'username': username,
        'address': address,
        'port': port
    }

    data.append(new_host)

    with open('hosts.json', 'w') as f:
        json.dump({'hosts': data}, f, indent=4)

    print("New host added successfully!")
