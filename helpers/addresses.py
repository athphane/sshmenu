import json
import os
import sys

from helpers.table import display_table


def toggle_address_visibility(data):
    display_table(data)

    while True:
        # Get user input for the selected record
        selected_index = int(input("Enter the ID of the record to toggle address visibility (or -1 to exit): "))
        if selected_index == -1:
            sys.exit()

        # Validate the selected index
        if selected_index < 1 or selected_index > len(data):
            print("Invalid ID!")
            continue

        # Get the selected record
        selected_record = data[selected_index - 1]
        hide_address = not selected_record.get('hide_address', False)
        selected_record['hide_address'] = hide_address

        with open(os.environ['PATH_TO_HOSTS'], 'w') as f:
            json.dump({'hosts': data}, f, indent=4)

        print(f"Address visibility toggled for host with ID {selected_index}")
