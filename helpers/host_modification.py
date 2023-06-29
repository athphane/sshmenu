import json
import os
import sys

from helpers.table import display_table


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

    with open(os.environ['PATH_TO_HOSTS'], 'w') as f:
        json.dump({'hosts': data}, f, indent=4)

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
