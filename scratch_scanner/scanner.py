# Objectives:
# 1. Auto-detect what network (i assume the range of ip addresses) we are on
# 2. Auto-detect what devices/individual ip addresses are on the network
# 3. Auto-detect what ports and services are on each ip addresses
# 4. Auto-detect what vulnerabilities are on each ip addresses

import netifaces
import ipaddress
import subprocess
from tqdm import tqdm
import socket

def get_wifi_interface():
    gateways = netifaces.gateways()
    default_gateway = gateways.get('default', {})
    default_gateway_info = default_gateway.get(netifaces.AF_INET)
    if default_gateway_info:
        _, interface = default_gateway_info
        return interface
    return None

def get_ip_addresses():
    wifi_interface = get_wifi_interface()
    interfaces = netifaces.interfaces()
    ip_addresses = []

    for interface in interfaces:
        if_addresses = netifaces.ifaddresses(interface)
        if interface == wifi_interface:
            is_wifi = True
        else:
            is_wifi = False

        for addr_family in (netifaces.AF_INET, netifaces.AF_INET6):
            if addr_family in if_addresses:
                addresses = if_addresses[addr_family]
                for address_info in addresses:
                    ip_address = address_info['addr']
                    subnet_mask = address_info.get('netmask')
                    ip_addresses.append((ip_address, subnet_mask, is_wifi))

    return ip_addresses

def is_common_ip_address(ip_address):
    common_ip_prefixes = ['192.168', '10.0', '172.16']
    for prefix in common_ip_prefixes:
        if ip_address.startswith(prefix):
            return True
    return False

def get_ip_range(ip_address, subnet_mask):
    network = ipaddress.IPv4Network(f"{ip_address}/{subnet_mask}", strict=False)
    return str(network.network_address), str(network.broadcast_address)

def perform_network_scan(ip_range):
    ip_start, ip_end = ip_range.split('-')

    ip_start = ipaddress.IPv4Address(ip_start)
    ip_end = ipaddress.IPv4Address(ip_end)

    total_ips = int(ip_end) - int(ip_start) + 1
    online_hosts = []

    with tqdm(total=total_ips, desc="Scanning", unit="IP") as pbar:
        current_ip = ip_start

        while current_ip <= ip_end:
            response = subprocess.run(["ping", "-n", "1", "-w", "200", str(current_ip)], stdout=subprocess.DEVNULL)
            if response.returncode == 0:
                online_hosts.append(str(current_ip))

            current_ip += 1
            pbar.update(1)

    return online_hosts

def scan_ports(ip_address):
    open_ports = []
    port_range = 21, 22, 23, 53, 80, 443, 3389, 5900, 8080 # Adjust port range as required, range(1, 65535) will scan all ports

    with tqdm(total=len(port_range), desc="Scanning Ports", unit="port") as pbar:
        for port in port_range:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect_ex((ip_address, port))
            if result == 0:
                open_ports.append(port)
            sock.close()
            pbar.update(1)

    return open_ports

ip_addresses = get_ip_addresses()

for ip_address, subnet_mask, is_wifi in ip_addresses:
    if is_wifi and is_common_ip_address(ip_address):
        network_address, broadcast_address = get_ip_range(ip_address, subnet_mask)
        print(f"Wi-Fi Network: {ip_address} - {network_address}/{subnet_mask}")
        print(f"IP Range: {network_address} - {broadcast_address}")

        response = input("Do you want to scan this network? (yes/no): ")
        if response.lower() == "yes":
            ip_range = f"{network_address}-{broadcast_address}"
            print(f"Starting scan for IP range: {ip_range}")
            online_hosts = perform_network_scan(ip_range)

            for host in online_hosts:
                print(f"\nHost: {host}       Status: Online")
                open_ports = scan_ports(host)
                if open_ports:
                    print(f"Open ports for {host}: {open_ports}")
                else:
                    print(f"No open ports found for {host}")

            break
        else:
            print("Skipping network scan.")


# --------------------------------------------------------------------------------


# import netifaces
# import ipaddress
# import subprocess
# from tqdm import tqdm
# import socket

# def get_wifi_interface():
#     gateways = netifaces.gateways()
#     default_gateway = gateways.get('default', {})
#     default_gateway_info = default_gateway.get(netifaces.AF_INET)
#     if default_gateway_info:
#         _, interface = default_gateway_info
#         return interface
#     return None

# def get_ip_addresses():
#     wifi_interface = get_wifi_interface()
#     interfaces = netifaces.interfaces()
#     ip_addresses = []

#     for interface in interfaces:
#         if_addresses = netifaces.ifaddresses(interface)
#         if interface == wifi_interface:
#             is_wifi = True
#         else:
#             is_wifi = False

#         for addr_family in (netifaces.AF_INET, netifaces.AF_INET6):
#             if addr_family in if_addresses:
#                 addresses = if_addresses[addr_family]
#                 for address_info in addresses:
#                     ip_address = address_info['addr']
#                     subnet_mask = address_info.get('netmask')
#                     ip_addresses.append((ip_address, subnet_mask, is_wifi))

#     return ip_addresses

# def is_common_ip_address(ip_address):
#     common_ip_prefixes = ['192.168', '10.0', '172.16']
#     for prefix in common_ip_prefixes:
#         if ip_address.startswith(prefix):
#             return True
#     return False

# def get_ip_range(ip_address, subnet_mask):
#     network = ipaddress.IPv4Network(f"{ip_address}/{subnet_mask}", strict=False)
#     return str(network.network_address), str(network.broadcast_address)

# def perform_network_scan(ip_range):
#     ip_start, ip_end = ip_range.split('-')

#     ip_start = ipaddress.IPv4Address(ip_start)
#     ip_end = ipaddress.IPv4Address(ip_end)

#     total_ips = int(ip_end) - int(ip_start) + 1

#     with tqdm(total=total_ips, desc="Scanning", unit="IP") as pbar:
#         current_ip = ip_start

#         while current_ip <= ip_end:
#             response = subprocess.run(["ping", "-n", "1", "-w", "200", str(current_ip)], stdout=subprocess.DEVNULL)
#             if response.returncode == 0:
#                 print(f"Host: {current_ip}\tStatus: Online")
#                 scan_ports(str(current_ip))
#                 # Perform additional processing for each online host

#             current_ip += 1
#             pbar.update(1)

# def scan_ports(ip_address):
#     open_ports = []
#     port_range = 21, 22, 23, 53, 80, 443, 3389, 5900, 8080 # Adjust port range as required, range(1, 65535) will scan all ports

#     with tqdm(total=len(port_range), desc="Scanning Ports", unit="port") as pbar:
#         for port in port_range:
#             sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#             sock.settimeout(0.5)
#             result = sock.connect_ex((ip_address, port))
#             if result == 0:
#                 open_ports.append(port)
#             sock.close()
#             pbar.update(1)

#     if open_ports:
#         print(f"Open ports for {ip_address}: {open_ports}")
#     else:
#         print(f"No open ports found for {ip_address}")

# ip_addresses = get_ip_addresses()

# for ip_address, subnet_mask, is_wifi in ip_addresses:
#     if is_wifi and is_common_ip_address(ip_address):
#         network_address, broadcast_address = get_ip_range(ip_address, subnet_mask)
#         print(f"Wi-Fi Network: {ip_address} - {network_address}/{subnet_mask}")
#         print(f"IP Range: {network_address} - {broadcast_address}")

#         response = input("Do you want to scan this network? (yes/no): ")
#         if response.lower() == "yes":
#             ip_range = f"{network_address}-{broadcast_address}"
#             print(f"Starting scan for IP range: {ip_range}")
#             perform_network_scan(ip_range)
#             break
#         else:
#             print("Skipping network scan.")


# --------------------------------------------------------------------------------


# def get_wifi_interface():
#     gateways = netifaces.gateways()
#     default_gateway = gateways.get('default', {})
#     default_gateway_info = default_gateway.get(netifaces.AF_INET)
#     if default_gateway_info:
#         _, interface = default_gateway_info
#         return interface
#     return None

# def get_ip_addresses():
#     wifi_interface = get_wifi_interface()
#     interfaces = netifaces.interfaces()
#     ip_addresses = []

#     for interface in interfaces:
#         if_addresses = netifaces.ifaddresses(interface)
#         if interface == wifi_interface:
#             is_wifi = True
#         else:
#             is_wifi = False

#         for addr_family in (netifaces.AF_INET, netifaces.AF_INET6):
#             if addr_family in if_addresses:
#                 addresses = if_addresses[addr_family]
#                 for address_info in addresses:
#                     ip_address = address_info['addr']
#                     subnet_mask = address_info.get('netmask')
#                     ip_addresses.append((ip_address, subnet_mask, is_wifi))

#     return ip_addresses

# def is_common_ip_address(ip_address):
#     common_ip_prefixes = ['192.168', '10.0', '172.16']
#     for prefix in common_ip_prefixes:
#         if ip_address.startswith(prefix):
#             return True
#     return False

# def get_ip_range(ip_address, subnet_mask):
#     network = ipaddress.IPv4Network(f"{ip_address}/{subnet_mask}", strict=False)
#     return str(network.network_address), str(network.broadcast_address)

# def perform_network_scan(ip_range):
#     ip_start, ip_end = ip_range.split('-')

#     ip_start = ipaddress.IPv4Address(ip_start)
#     ip_end = ipaddress.IPv4Address(ip_end)

#     total_ips = int(ip_end) - int(ip_start) + 1

#     with tqdm(total=total_ips, desc="Scanning", unit="IP") as pbar:
#         current_ip = ip_start

#         while current_ip <= ip_end:
#             response = subprocess.run(["ping", "-n", "1", "-w", "200", str(current_ip)], stdout=subprocess.DEVNULL)
#             if response.returncode == 0:
#                 print(f"Host: {current_ip}\tStatus: Online")
#                 # Perform additional processing for each online host

#             current_ip += 1
#             pbar.update(1)

# ip_addresses = get_ip_addresses()

# for ip_address, subnet_mask, is_wifi in ip_addresses:
#     if is_wifi and is_common_ip_address(ip_address):
#         network_address, broadcast_address = get_ip_range(ip_address, subnet_mask)
#         print(f"Wi-Fi Network: {ip_address} - {network_address}/{subnet_mask}")
#         print(f"IP Range: {network_address} - {broadcast_address}")

#         response = input("Do you want to scan this network? (yes/no): ")
#         if response.lower() == "yes":
#             ip_range = f"{network_address}-{broadcast_address}"
#             print(f"Starting scan for IP range: {ip_range}")
#             perform_network_scan(ip_range)
#             break
#         else:
#             print("Skipping network scan.")


# --------------------------------------------------------------------------------


# import socket
# import struct

# ip_address = socket.gethostbyname(socket.gethostname())
# subnet_mask = "255.255.255.0"  # Assuming a /24 subnet

# ip_address_bytes = socket.inet_aton(ip_address)
# subnet_mask_bytes = socket.inet_aton(subnet_mask)

# # Perform the bitwise AND operation on the bytes objects
# network_address_bytes = struct.pack('!I', (struct.unpack('!I', ip_address_bytes)[0] & struct.unpack('!I', subnet_mask_bytes)[0]))

# # Convert the network address bytes back to the IP address format
# network_address = socket.inet_ntoa(network_address_bytes)

# # Calculate the broadcast address by flipping all host bits to 1
# broadcast_address_bytes = struct.pack('!I', (struct.unpack('!I', network_address_bytes)[0] | ~struct.unpack('!I', subnet_mask_bytes)[0] & 0xffffffff))
# broadcast_address = socket.inet_ntoa(broadcast_address_bytes)

# print("Hostname:", socket.gethostname())
# print("IP Address:", ip_address)
# print("Subnet Mask:", subnet_mask)
# print("Network Address:", network_address)
# print("Broadcast Address:", broadcast_address)
