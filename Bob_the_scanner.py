import scapy.all as scapy
import argparse
import re
from colorama import Fore, Back, Style, init


def main():
    """
    Input:
        - No direct input, but requires a command-line argument:
          --ip_address_CIDR (IP address in CIDR format).

    Output:
        - Prints the network scan results or an error message if the CIDR address is invalid.
    """
    parser = argparse.ArgumentParser(description='A program that scans and provides the IPs of all accessible machines on the network')
    parser.add_argument('-IP_CIDR', '--ip_address_CIDR', type=str, required=True, help='IP address CIDR (required)')
    args = parser.parse_args()

    if args.ip_address_CIDR and validate_ip_cidr(args.ip_address_CIDR):
        IP = args.ip_address_CIDR
        print(f'{Fore.BLUE}IP address CIDR provided: {IP} {Style.RESET_ALL}')
        print(Fore.GREEN +"========== Start of Scan ==========\n"+ Style.RESET_ALL)
        scan_network(IP)
    else:
        print("Invalid IP address CIDR")


def scan_network(ip_range):
    """
    Input:
        - ip_range (str): A range of IP addresses in CIDR format.

    Output:
        - Displays ARP scan results, identifying devices on the network.
    """
    scapy.arping(ip_range, verbose=True)


def validate_ip_cidr(ip_cidr):
    """
    Input:
        - ip_cidr (str): An IP address in CIDR format.

    Output:
        - bool: Returns True if the CIDR address is valid, False otherwise.
    """
    pattern = r"^((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])/(3[0-2]|[1-2]?[0-9])$"
    return bool(re.match(pattern, ip_cidr))


def print_logo():
    """
    Input:
        - None.

    Output:
        - Prints an ASCII logo on the screen.
    """
    logo = Fore.YELLOW + r"""
     ____        _       _______ _               _____                                 
    |  _ \      | |     |__   __| |             / ____|                                
    | |_) | ___ | |__      | |  | |__   ___    | (___   ___ __ _ _ __  _ __   ___ _ __ 
    |  _ < / _ \| '_ \     | |  | '_ \ / _ \    \___ \ / __/ _` | '_ \| '_ \ / _ \ '__|
    | |_) | (_) | |_) |    | |  | | | |  __/    ____) | (_| (_| | | | | | | |  __/ |   
    |____/ \___/|_.__/     |_|  |_| |_|\___|   |_____/ \___\__,_|_| |_|_| |_|\___|_|   

        v1.0    Using argparse, scapy, re & colorama.                                                                  
    """ + Style.RESET_ALL
    print(logo)


if __name__ == '__main__':
    init()
    print_logo()
    main()
    print(Fore.GREEN +"\n=========== End of Scan ===========\n"+ Style.RESET_ALL)
