import socket
import requests
import pprint
import json

def get_ip_address(hostname):
    try:
        ip_address = socket.gethostbyname(hostname)
        return ip_address
    except socket.gaierror:
        print("Error: Unable to get IP address for the provided domain.")
        return None

def get_geolocation(ip_address):
    if ip_address:
        request_url = 'https://geolocation-db.com/jsonp/' + ip_address
        response = requests.get(request_url)
        
        if response.status_code == 200:
            geolocation = response.content.decode()
            geolocation = geolocation.split("(")[1].strip(")")
            geolocation = json.loads(geolocation)
            
            for k, v in geolocation.items():
                pprint.pprint(str(k) + ' : ' + str(v))
        else:
            print("Error: Unable to fetch geolocation data. Status code:", response.status_code)
    else:
        print("Error: Unable to fetch geolocation data. Invalid IP address.")

if __name__ == "__main__":
    hostname = input('Enter A Domain: ')
    ip_address = get_ip_address(hostname)
    get_geolocation(ip_address)
