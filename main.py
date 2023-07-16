import json
import os

from colorama import init as colorama_init
from simple_term_menu import TerminalMenu

from helpers.connection import run_ssh_command
from helpers.ip_address import obfuscate_ip, is_ip_address

colorama_init()

PATH_TO_HOSTS = os.path.expanduser('~/.ssh/hosts.json')
# PATH_TO_HOSTS = 'hosts.json'
os.environ['PATH_TO_HOSTS'] = PATH_TO_HOSTS

# create the json file it doesn't exist
if not os.path.exists(PATH_TO_HOSTS):
    with open(PATH_TO_HOSTS, 'w') as f:
        json.dump({"hosts": [], "accesses": []}, f)


def main():
    # Load data from the JSON file
    with open(os.environ['PATH_TO_HOSTS']) as f:
        data = json.load(f)["hosts"]

    options = []

    for index, record in enumerate(data, start=1):
        if 'hide_address' in record.keys() and record['hide_address'] is True:
            obfuscated_address = '*' * len(record['address'])
        else:
            obfuscated_address = obfuscate_ip(record['address']) if is_ip_address(record['address']) else record[
                'address']

        values = record['name']
        options.append(values)

    main_menu_title = "  Main Menu.\n  Press Q or Esc to quit. \n"
    main_menu_cursor = "> "
    main_menu_cursor_style = ("fg_blue", "bold")
    main_menu_style = ("bg_blue", "fg_black")
    menu_highlight_style = ("bg_blue", "fg_black")
    terminal_menu = TerminalMenu(
        options,
        title=main_menu_title,
        menu_cursor=main_menu_cursor,
        menu_cursor_style=main_menu_cursor_style,
        menu_highlight_style=main_menu_style,
        search_highlight_style=menu_highlight_style,
        cycle_cursor=True,
        clear_screen=True,
    )
    menu_entry_index = terminal_menu.show()

    print(f"Connecting to {data[menu_entry_index]}")

    run_ssh_command(data[menu_entry_index])
    # print(f"You have selected {options[menu_entry_index]}!")


if __name__ == '__main__':
    main()
