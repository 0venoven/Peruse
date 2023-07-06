import subprocess
import re
import ipaddress

# i have yet to test this on mac as of 6/7/23

def get_ifconfig_output():
    try:
        ifconfig_output = subprocess.check_output(['ifconfig', 'en0']).decode('utf-8')
        return ifconfig_output
    except subprocess.CalledProcessError:
        return None

def extract_ip_address(ifconfig_output):
    ip_address_pattern = r'inet (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
    match = re.search(ip_address_pattern, ifconfig_output)
    if match:
        return match.group(1)
    else:
        return None

def extract_subnet_mask(ifconfig_output):
    subnet_mask_pattern = r'netmask (0x[a-fA-F0-9]+)'
    match = re.search(subnet_mask_pattern, ifconfig_output)
    if match:
        subnet_mask = match.group(1)
        subnet_mask = int(subnet_mask, 16)
        subnet_mask = str(ipaddress.ip_address(subnet_mask))
        return subnet_mask
    else:
        return None

# Usage
ifconfig_output = get_ifconfig_output()

if ifconfig_output:
    ip_address = extract_ip_address(ifconfig_output)
    subnet_mask = extract_subnet_mask(ifconfig_output)

    if ip_address and subnet_mask:
        print(f"IP Address: {ip_address}")
        print(f"Subnet Mask: {subnet_mask}")
        print("IP Range:" + ipaddress.ip_interface(f"{ip_address}/{subnet_mask}").network)
    else:
        print("Unable to retrieve IP address and subnet mask.")
else:
    print("Error executing ifconfig command.")
