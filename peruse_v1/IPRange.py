import subprocess
import re
import ipaddress

class IPRange:
    def __init__(self):
        self.network_output = None
        self.ip_address = None
        self.subnet_mask = None

    def get_network_details(self):
        try:
            self.network_output = subprocess.check_output(['ipconfig', '/all']).decode('utf-8')
        except subprocess.CalledProcessError:
            self.network_output = None

    def extract_ip_address(self):
        ip_address_pattern = r'Wireless LAN adapter Wi-Fi.*?IPv4 Address.*?: (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
        match = re.search(ip_address_pattern, self.network_output, re.DOTALL)
        if match:
            self.ip_address = match.group(1)
        else:
            self.ip_address = None

    def extract_subnet_mask(self):
        subnet_mask_pattern = r'Wireless LAN adapter Wi-Fi.*?Subnet Mask.*?: (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
        match = re.search(subnet_mask_pattern, self.network_output, re.DOTALL)
        if match:
            self.subnet_mask = match.group(1)
        else:
            self.subnet_mask = None

    def get_ip_range(self):
        self.get_network_details()
        if self.network_output:
            self.extract_ip_address()
            self.extract_subnet_mask()
            if self.ip_address and self.subnet_mask:
                network = ipaddress.IPv4Network(f"{self.ip_address}/{self.subnet_mask}", strict=False)
                return str(network.network_address) + "/" + str(network.prefixlen)
            else:
                print("Unable to retrieve IP address, please make sure you are connected to a network.")
        else:
            print("Error executing ipconfig command.")