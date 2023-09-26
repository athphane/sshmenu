import json
import os
import sys

from helpers.table import display_table


def add_host(data):
    """
    Add a new host to the list
    :param data:
    :return:
    """
    name = input("Enter the name: ")
    username = input("Enter the username: ")
    address = input("Enter the address: ")

    # get the port from input, and if not provided, use the default port 22
    port = input("Enter the port (default: 22): ")
    if port == "":
        port = 22
    else:
        port = int(port)

    # get the identiy file from input, default to none
    identity_file = input("Enter the identity file (default: none): ")
    if identity_file == "":
        identity_file = None

    new_host = {
        'name': name,
        'username': username,
        'address': address,
        'port': port
    }

    data.append(new_host)

    file_data = json.loads(open(os.environ['PATH_TO_HOSTS'], 'r').read())
    file_data['hosts'] = data

    with open(os.environ['PATH_TO_HOSTS'], 'w') as f:
        json.dump(data, f, indent=4)

    print("New host added successfully!")

    sys.exit()


def remove_host(data):
    display_table(data)

    idx = int(input('Enter the ID of the host to remove: '))

    # ask user for confirmation to remove yes or no
    confirmation = input(f'Are you sure you want to remove host with ID {idx}? (y/n): ')
    if confirmation.lower() != 'y':
        print('Aborting...')
        sys.exit()

    print('Removing host...')

    # remove the idx-th element from the list
    data.pop(idx - 1)

    # write the updated data to the file
    with open(os.environ['PATH_TO_HOSTS'], 'w') as f:
        json.dump({'hosts': data}, f, indent=4)

    print(f"Host with ID {idx} removed successfully!")

    sys.exit()
