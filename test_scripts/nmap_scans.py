import os
import platform
import subprocess
import sys

# Check if Nmap is installed
def is_nmap_installed():
    nmap_executable = r"C:\Program Files (x86)\Nmap\nmap.exe"  # Update with the correct path
    return os.path.isfile(nmap_executable)

# def is_nmap_installed():
#     try:
#         subprocess.run(['C:\\Program Files (x86)\\Nmap', '-h'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
#         return True
#     except FileNotFoundError:
#         return False

# Function to get the Nmap installation directory
def get_nmap_directory():
    return r"C:\Program Files (x86)\Nmap"  # Replace with the correct Nmap installation directory

# def get_nmap_directory():
#     try:
#         nmap_output = subprocess.check_output(['nmap', '-v'], universal_newlines=True)
#         for line in nmap_output.splitlines():
#             if line.startswith('Nmap executable path:'):
#                 return line.split(':', 1)[1].strip()
#     except (FileNotFoundError, subprocess.CalledProcessError):
#         pass
#     return None

# Check if Nmap is installed
if not is_nmap_installed():
    print("Nmap is not installed. Please install Nmap and try again.")
    sys.exit(1)

# Get Nmap installation directory
nmap_dir = get_nmap_directory()
if not nmap_dir:
    print("Failed to determine Nmap installation directory.")
    sys.exit(1)

# Add Nmap directory to PATH temporarily
if platform.system() == 'Windows':
    os.environ['PATH'] = nmap_dir + ';' + os.environ['PATH']
else:
    os.environ['PATH'] = nmap_dir + ':' + os.environ['PATH']

# Proceed with your Nmap scanning tasks using python-nmap
#-------------------------------------------------------------------------------
import nmap

nm = nmap.PortScanner()

target_ip = "192.168.1.0/24"  # Replace with your desired network range

# Perform host discovery
nm.scan(hosts=target_ip, arguments="-sn")

# Get a list of all discovered hosts
hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]

# Print the list of discovered hosts
for host, status in hosts_list:
    print(f"Host: {host}\tStatus: {status}")

    # Check if the host is up
    if status == 'up':
        # Perform a more detailed scan on the host
        nm.scan(hosts=host, arguments="-p1-65535 -sV -O")

        # Print the scan results for the host
        for proto in nm[host].all_protocols():
            print(f"\nProtocol: {proto}")
            ports = nm[host][proto].keys()
            for port in ports:
                print(f"Port: {port}\tState: {nm[host][proto][port]['state']}\tService: {nm[host][proto][port]['name']}")