import socket
from termcolor import colored
import re

def scan(ipaddress, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)  # Set timeout to 1 second
            sock.connect((ipaddress, port))
            service_version = sock.recv(1024).decode('utf-8', 'ignore').strip('\n')
            port_state = f'Port {port} is open'
            print(colored(port_state, 'yellow'), end='    ')
            print(service_version)
    except (ConnectionRefusedError, socket.timeout):
        pass  # Port is closed or timeout, do nothing
    except UnicodeDecodeError:
        # Try decoding with 'latin-1' if 'utf-8' fails
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            sock.connect((ipaddress, port))
            service_version = sock.recv(1024).decode('latin-1').strip('\n')
            port_state = f'Port {port} is open'
            print(colored(port_state, 'yellow'), end='    ')
            print(service_version)
        except Exception as e:
            print(colored(f'Error scanning port {port}: {str(e)}', 'red'))
    except Exception as e:
        print(colored(f'Error scanning port {port}: {str(e)}', 'red'))

def validate_ip(ip):
    ip_pattern = re.compile(r'^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.'
                           r'(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.'
                           r'(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.'
                           r'(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$')
    return re.match(ip_pattern, ip)

def scan_ports(ipaddress, start_port, end_port):
    for port in range(start_port, end_port + 1):
        scan(ipaddress, port)

target = input('Target: ')

if validate_ip(target):
    scan_ports(target, 1, 63000)  # Scan ports 1 to 63000
else:
    print(colored('Invalid IP address', 'red'))
