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
        values = [index, record['name'], obfuscated_address, tags]
        table.add_row(values)

    # Print the table
    print(table)
