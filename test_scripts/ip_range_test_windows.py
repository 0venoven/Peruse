import subprocess
import re
import ipaddress

def get_ipconfig_details():
    try:
        ipconfig_output = subprocess.check_output(['ipconfig', '/all']).decode('utf-8')
        return ipconfig_output
    except subprocess.CalledProcessError:
        return None

def extract_ip_address(ipconfig_output):
    ip_address_pattern = r'Wireless LAN adapter Wi-Fi.*?IPv4 Address.*?: (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
    match = re.search(ip_address_pattern, ipconfig_output, re.DOTALL)
    if match:
        return match.group(1)
    else:
        return None

def extract_subnet_mask(ipconfig_output):
    subnet_mask_pattern = r'Wireless LAN adapter Wi-Fi.*?Subnet Mask.*?: (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
    match = re.search(subnet_mask_pattern, ipconfig_output, re.DOTALL)
    if match:
        return match.group(1)
    else:
        return None

def get_ip_range(ip_address, subnet_mask):
    network = ipaddress.IPv4Network(f"{ip_address}/{subnet_mask}", strict=False)
    return str(network.network_address) + "/" + str(network.prefixlen)


ipconfig_output = get_ipconfig_details()

if ipconfig_output:
    ip_address = extract_ip_address(ipconfig_output)
    subnet_mask = extract_subnet_mask(ipconfig_output)

    if ip_address and subnet_mask:
        print(f"IP Address: {ip_address}")
        print(f"Subnet Mask: {subnet_mask}")
        ip_range = get_ip_range(ip_address, subnet_mask)
        print("IP Range:", ip_range)
    else:
        print("Unable to get IP address and subnet mask, please make sure you are connected to a network.")
else:
    print("Error executing ipconfig command.")