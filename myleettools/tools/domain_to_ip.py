# domain_to_ip.py

import socket


def get_ip_from_domain(domain):

    try:
        ip_address = socket.gethostbyname(domain)
        return ip_address
    except socket.gaierror as err:
        return f"Error: {err}"


def run():
    print("Domain to IP Converter")
    while True:
        domain = input("Enter a domain name (or 'exit' to quit): ")
        if domain.lower() == 'exit':
            break
        ip_address = get_ip_from_domain(domain)
        print(f"The IP address of {domain} is: {ip_address}")
