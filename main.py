import argparse
import json
import os
import subprocess
import sys
import time

from helpers.addresses import toggle_address_visibility
from helpers.ascii_art import ASCII_ART
from helpers.host_modification import add_host
from helpers.table import display_table

PATH_TO_HOSTS = os.path.expanduser('~/.ssh/hosts.json')
os.environ['PATH_TO_HOSTS'] = PATH_TO_HOSTS


def run_ssh_command(selected_record):
    # Run the SSH command
    ssh_command = ["ssh", "-p", str(selected_record['port']),
                   f"{selected_record['username']}@{selected_record['address']}"]
    subprocess.run(ssh_command)
    sys.exit()


def select_record(data, filter_tag=None):
    while True:
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console
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
    parser.add_argument('--toggle', action='store_true', help='Toggle address visibility')
    parser.add_argument('--filter', metavar='TAG', help='Filter hosts by tag')

    args = parser.parse_args()

    if args.add:
        add_host(data)
    elif args.toggle:
        toggle_address_visibility(data)
    else:
        select_record(data, args.filter)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
