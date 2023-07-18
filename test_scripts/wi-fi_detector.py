# This script is used to detect the available Wi-Fi networks and prompt the user to choose a Wi-Fi network to scan.
# It does not actually perform the scan itself however.
# It is not always reliable as it relies on the output of a subprocess.
# It seems that opening the wi-fi settings on your computer so that the computer actually scans before running this script makes it work more reliably.
# But this also somewhat means that the script is not particularly useful. :/

import subprocess
import re
import platform

# Function to get the available Wi-Fi networks
def get_available_wifi_networks():
    system = platform.system()
    networks = []
    
    if system == "Windows":
        try:
            output = subprocess.check_output(["netsh", "wlan", "show", "network"])
            output = output.decode("utf-8")
            networks = re.findall(r"SSID \d+ : (.+)", output)
        except subprocess.CalledProcessError:
            pass
    
    elif system == "Darwin":
        try:
            output = subprocess.check_output(["/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport", "-s"])
            output = output.decode("utf-8")
            networks = re.findall(r"\s+(\S+)\s+(-\d+)", output)
            networks = [ssid for ssid, _ in networks]
        except subprocess.CalledProcessError:
            pass
    
    elif system == "Linux":
        try:
            output = subprocess.check_output(["iwlist", "scan"])
            output = output.decode("utf-8")
            networks = re.findall(r"ESSID:\"(.+)\"", output)
        except subprocess.CalledProcessError:
            pass
    
    return networks

# Get available Wi-Fi networks
wifi_networks = get_available_wifi_networks()

# Prompt the user to choose a Wi-Fi network
if wifi_networks:
    print("Available Wi-Fi Networks:")
    for i, network in enumerate(wifi_networks):
        print(f"{i+1}. {network}")
    choice = int(input("Enter the number corresponding to the Wi-Fi network to scan: "))
    selected_wifi_network = wifi_networks[choice - 1]
    print("\nSelected Wi-Fi Network:", selected_wifi_network)
else:
    print("No Wi-Fi networks found.")


# The following script uses the wifi library to detect the available Wi-Fi networks and prompt the user to choose a Wi-Fi network to scan.
# It also does not actually perform the scan itself however.
# It may be more reliable than the previous script as it does not rely on the output of a subprocess.

# import wifi

# # Function to get the available Wi-Fi networks
# def get_available_wifi_networks():
#     networks = []
#     cells = wifi.Cell.all('wlan0')  # Adjust the interface name based on your system (e.g., wlan0, wlan1, etc.)
    
#     for cell in cells:
#         networks.append(cell.ssid)
    
#     return networks

# # Get available Wi-Fi networks
# wifi_networks = get_available_wifi_networks()

# # Prompt the user to choose a Wi-Fi network
# if wifi_networks:
#     print("Available Wi-Fi Networks:")
#     for i, network in enumerate(wifi_networks):
#         print(f"{i+1}. {network}")
#     choice = int(input("Enter the number corresponding to the Wi-Fi network to scan: "))
#     selected_wifi_network = wifi_networks[choice - 1]
#     print("\nSelected Wi-Fi Network:", selected_wifi_network)
# else:
#     print("No Wi-Fi networks found.")
