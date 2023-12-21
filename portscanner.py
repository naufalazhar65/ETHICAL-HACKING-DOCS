import socket
from termcolor import colored
import re

def scan(ipaddress, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            sock.connect((ipaddress, port))
            service_version = sock.recv(1024).decode('utf-8').strip('\n')
            port_state = f'Port {port} is open'
            print(colored(port_state, 'yellow'), end='    ')
            print(service_version)
    except (ConnectionRefusedError, socket.timeout):
        print(colored(f'Port {port} is closed', 'red'))
    except Exception as e:
        print(colored(f'Error scanning port {port}: {str(e)}', 'red'))

def validate_ip(ip):
    ip_pattern = re.compile(r'^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.'
                           r'(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.'
                           r'(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.'
                           r'(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$')
    return re.match(ip_pattern, ip)

def validate_port(port):
    return 1 <= port <= 65535

target = input('Target: ')
ports = input('Port: ')

if validate_ip(target):
    if ',' in ports:
        port_list = ports.split(',')
        for port in port_list:
            if validate_port(int(port)):
                scan(target, int(port))
            else:
                print(colored(f'Invalid port number: {port}', 'red'))
    elif '-' in ports:
        port_range = ports.split('-')
        start = int(port_range[0])
        end = int(port_range[1])
        if validate_port(start) and validate_port(end):
            for port in range(start, end + 1):
                scan(target, port)
        else:
            print(colored('Invalid port range', 'red'))
    elif validate_port(int(ports)):
        scan(target, int(ports))
    else:
        print(colored(f'Invalid port number: {ports}', 'red'))
else:
    print(colored('Invalid IP address', 'red'))


