from colorama import Fore, Style
from prettytable import PrettyTable

from helpers.ip_address import obfuscate_ip, is_ip_address


def display_table(data, filter_tag=None):
    table_column_headers = ['ID', 'Name', 'Address', 'Tags']

    # Create the table with variable columns
    table = PrettyTable(table_column_headers)

    table.align = 'l'

    for index, record in enumerate(data, start=1):
        if filter_tag:
            tags = record.get('tags', [])
            if filter_tag not in tags:
                continue

        if 'hide_address' in record.keys() and record['hide_address'] is True:
            obfuscated_address = '*' * len(record['address'])
        else:
            obfuscated_address = obfuscate_ip(record['address']) if is_ip_address(record['address']) else record[
                'address']

        tags = record['tags'] if 'tags' in record else []
        tags = ', '.join(tags)
        values = [wrap_in_cyclic_color(index, index), wrap_in_cyclic_color(record['name'], index),
                  wrap_in_cyclic_color(obfuscated_address, index), wrap_in_cyclic_color(tags, index)]
        table.add_row(values)

    # Print the table
    print(table)


def wrap_in_cyclic_color(text, idx):
    """
    Wrap the text in a color from the colorama library
    :param text:
    :param idx:
    :return:
    """
    colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]
    return colors[idx % len(colors)] + str(text) + Style.RESET_ALL
