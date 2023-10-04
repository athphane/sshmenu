import argparse
import json
import os
import time

from colorama import init as colorama_init
from simple_term_menu import TerminalMenu

from helpers.connection import run_ssh_command
from helpers.host_modification import add_host, remove_host

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
        data = json.load(f)['hosts']

    parser = argparse.ArgumentParser(description='SSH Host Management')
    parser.add_argument('--add', action='store_true', help='Add a new host')
    parser.add_argument('--remove', action='store_true', help='Remove an existing host')

    args = parser.parse_args()

    if args.add:
        add_host(data)
    elif args.remove:
        remove_host(data)
    else:
        options = [record['name'] for record in data]

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

        print(f"Connecting to {data[menu_entry_index]['name']}")
        time.sleep(0.5)

        run_ssh_command(data[menu_entry_index])


if __name__ == '__main__':
    main()
