import json
import subprocess
from threading import Thread

from consolemenu import *
from consolemenu.items import *

hosts_file = json.loads(open('hosts.json', 'r').read())
hosts = hosts_file['hosts']


def run_ssh(username, address):
    connection = f"{username}@{address}"
    command = ['ssh', connection]
    subprocess.call(' '.join(command), creationflags=subprocess.CREATE_NEW_CONSOLE)


def execute_ssh(username, address):
    thread = Thread(target=run_ssh, args=(username, address))
    thread.start()


if __name__ == '__main__':
    menu = ConsoleMenu("SSH Host Selector")

    for host in hosts:
        function_item = FunctionItem(host['name'], execute_ssh, [host['username'], host['address']])
        menu.append_item(function_item)

    menu.show()
