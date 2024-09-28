from scapy.all import ARP, Ether, srp
import socket
import json 

from getmac import get_mac_address

def scan(ip):
    try:
        # Sending an ARP discovery in the network to get all the IP and MAC addresses
        arp_request = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=ip)
        result = srp(arp_request, timeout=1, verbose=False)[0]
        devices = [{'ip': received.psrc, 'mac': received.hwsrc} for sent, received in result]
       
        return devices
    except Exception as e:
        print(f"Error during scanning: {e}")
        return []

    
def get_device_names(devices):
    device_names = []
    for device in devices:
        try:
            host_name, _, _ = socket.gethostbyaddr(device['ip'])
            device_names.append({'ip': device['ip'], 'mac': device['mac'], 'name': host_name})
        except socket.herror:
            device_names.append({'ip': device['ip'], 'mac': device['mac'], 'name': 'Unknown'})
    return device_names

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

def get_ip_and_mac():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    mac_address = get_mac_address(ip=ip_address)
    return ip_address, mac_address

def send_data(user, server_ip):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, 9990))

    user_data = json.dumps(user.to_dict())
    client_socket.send(user_data.encode())

    response = client_socket.recv(1024).decode()
    print(f"Response from server: {response}")

    client_socket.close()

if __name__ == "__main__":
    server_ip = "127.0.0.1"
    try:
        username = input("Enter your username: ")
        sender_hostname = input('Enter the sender hostname: ')
        target_ip = input("Enter the target IP address or range (e.g., 192.168.1.1 or 192.168.1.1/24): ")
        devices_list = scan(target_ip)
        devices_with_names = get_device_names(devices_list)
        
    except Exception as e:
        print(f"An error occurred: {e}")
    ip_address, mac_address = get_ip_and_mac()
    user = User(user_id=2, username=username, ip_address=ip_address, mac_address=mac_address)
    """ for device in devices_with_names:
        if device['name'] == sender_hostname:
            server_ip = device['ip']"""
    
    
    send_data(user, server_ip)
