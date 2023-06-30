import os
import subprocess
import sys

from helpers.path import expand_path
from helpers.tracking import track_access


def construct_ssh_command(selected_record):
    """
    Construct the SSH command
    :param selected_record:
    :return:
    """
    ssh_command = ["ssh", "-p", str(selected_record['port'])]

    # Include path to identity file if provided
    if 'key' in selected_record:
        ssh_command.append("-i")
        ssh_command.append(expand_path(selected_record['key']))

    ssh_command.append(f"{selected_record['username']}@{selected_record['address']}")

    return ssh_command


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console


def run_ssh_command(selected_record):
    # Track the access
    track_access(selected_record)

    # Construct the SSH command with
    ssh_command = construct_ssh_command(selected_record)

    # Clear the console and run the SSH command
    clear_console()
    subprocess.run(ssh_command)

    # Exit the program
    sys.exit()
