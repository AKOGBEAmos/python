import socket
from scapy.all import ARP, Ether, srp
from getmac import get_mac_address

import json

CLIENT = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def scan(ip):
    try:
        # Sending an ARP discovery in the network to get all the IP and MAC addresses
        arp_request = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=ip)
        result = srp(arp_request, timeout=1, verbose=False)[0]
        devices = [{'ip': received.psrc, 'mac': received.hwsrc} for sent, received in result]
        
        # Filter clients that are listening on port 9990
        clients = [{'ip': device['ip'], 'mac': device['mac']} for device in devices ]

        """ if check_port(device['ip']) 
            We will try to see if it is possible to open port 9990  on the client dide once they open the app to get the file(s)        
        """

        return clients
    except Exception as e:
        print(f"Error during scanning: {e}")
        return []

def check_port(ip):
    """Scan each machine to see if they are listening on the target port 9990.
       This helps to narrow down the target of the transfer in the network.
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(1)  # Set a timeout of 1 second
        result = s.connect_ex((ip, 9990))  # Try to connect to port 9990
        return result == 0  # Return True if the port is open

def get_device_names(devices):
    device_names = []
    for device in devices:
        try:
            host_name, _, _ = socket.gethostbyaddr(device['ip'])
            device_names.append({'ip': device['ip'], 'mac': device['mac'], 'name': host_name})
        except socket.herror:
            device_names.append({'ip': device['ip'], 'mac': device['mac'], 'name': 'Unknown'})
    return device_names

def print_results(devices):
    print("IP Address\t\tMAC Address\t\tDevice Name")
    print("--------------------------------------------------------")
    for device in devices:
        print(f"{device['ip']}\t\t{device['mac']}\t\t{device['name']}")


#Creating the user class

class User:
    def __init__(self, user_id, username, ip_address, mac_address):
        self.user_id = user_id
        self.username = username
        self.ip_address = ip_address
        self.mac_address = mac_address

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'username': self.username,
            'ip_address': self.ip_address,
            'mac_address': self.mac_address
        }

    # Method to display user details (without password for security reasons)
    def display_user_info(self):
        print(f"User ID: {self.user_id}")
        print(f"Username: {self.username}")
        print(f"IP Address: {self.ip_address}")
        print(f"MAC Address: {self.mac_address}")

def start_server(user):
    
    SERVER_HOST = '0.0.0.0'
    SERVER_PORT = 9990
    CLIENT.bind((SERVER_HOST, SERVER_PORT))

    CLIENT.listen(1)  # Écoute pour une connexion en attente
    print("Server listening on port 9990...")

    conn, addr = CLIENT.accept()
    #once the connexion established, the server send his user-data to the client receiving the file
    print(f"Connection accepted from {addr}")

    user_data = json.dumps(user.to_dict())
    conn.send(user_data.encode())

    received_data = conn.recv(1024).decode()
    #And here it receives the data of the client.
    client_user = json.loads(received_data)
    print("Received data from client:")
    print(client_user)

    conn.close()
    CLIENT.close()

if __name__ == "__main__":
    try:
        target_ip = input("Enter the target IP address or range (e.g: 192.168.1.1 or 192.168.1.1/24): ")
        devices_list = scan(target_ip)
        devices_with_names = get_device_names(devices_list)
        print_results(devices_with_names)
    except Exception as e:
        print(f"An error occurred: {e}")

    username = input('Provide your username: ')
    hostname = input('Give the hostname of the receiver: ')
    # default values for the user
    user = User(user_id=1, username=username, ip_address="Unknown", mac_address="Unknown")

    # Looking for the device with the corresponding hostname provided.
    for device in devices_with_names:
        if hostname == device['name']:
            user.ip_address = device['ip']
            user.mac_address = device['mac']

    # Afficher les informations de l'utilisateur
    user.display_user_info()

    start_server(user)
