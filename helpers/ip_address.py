import re


def is_ip_address(address):
    """
    Check if input address is an IP Address
    :param address:
    :return:
    """
    # Regular expression pattern for IP address validation
    pattern = r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$'

    # Check if the address matches the IP address pattern
    if re.match(pattern, address):
        parts = address.split(".")
        for part in parts:
            if not 0 <= int(part) <= 255:
                return False
        return True

    return False


def obfuscate_ip(ip_address):
    # Split the IP address into octets
    octets = ip_address.split(".")

    # Obfuscate the last two octets
    octets[-2:] = ["***", "***"]

    # Join the octets back into an obfuscated IP address
    obfuscated_ip = ".".join(octets)

    return obfuscated_ip
