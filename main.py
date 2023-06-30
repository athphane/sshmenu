import argparse
import json
import os
import sys
import time

from colorama import init as colorama_init

from helpers.addresses import toggle_address_visibility
from helpers.ascii_art import ASCII_ART
from helpers.connection import run_ssh_command, clear_console
from helpers.host_modification import add_host, remove_host
from helpers.table import display_table

colorama_init()

# PATH_TO_HOSTS = os.path.expanduser('~/.ssh/hosts.json')
PATH_TO_HOSTS = 'hosts.json'
os.environ['PATH_TO_HOSTS'] = PATH_TO_HOSTS

# create the json file it doesn't exist
if not os.path.exists(PATH_TO_HOSTS):
    with open(PATH_TO_HOSTS, 'w') as f:
        json.dump({"hosts": [], "accesses": []}, f)


def select_record(data, filter_tag=None):
    """
    Select a record from the table and run the SSH command
    :param data:
    :param filter_tag:
    :return:
    """
    while True:
        while True:
            # Clear the console and display the ASCII art
            clear_console()
            print(ASCII_ART)

            # Display the table
            display_table(data, filter_tag)

            # Get user input for the selected record
            selected_index = input("Enter the ID of the record to run the SSH command (or -1 to exit): ")
            if selected_index == "-1":
                sys.exit()

            # Validate the selected index
            if selected_index.isdigit() and 1 <= int(selected_index) <= len(data):
                break

            print("Invalid ID!")
            time.sleep(0.3)

        # Get the selected record
        selected_record = data[int(selected_index) - 1]

        print(f"Loading connection to {selected_record['address']}")

        run_ssh_command(selected_record)


def main():
    # Load data from the JSON file
    with open(os.environ['PATH_TO_HOSTS']) as f:
        data = json.load(f)["hosts"]

    parser = argparse.ArgumentParser(description='SSH Host Management')
    parser.add_argument('--add', action='store_true', help='Add a new host')
    parser.add_argument('--remove', action='store_true', help='Remove an existing host')
    parser.add_argument('--toggle', action='store_true', help='Toggle address visibility')
    parser.add_argument('--filter', metavar='TAG', help='Filter hosts by tag')

    args = parser.parse_args()

    if args.add:
        add_host(data)
    elif args.remove:
        remove_host(data)
    elif args.toggle:
        toggle_address_visibility(data)
    else:
        select_record(data, args.filter)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
