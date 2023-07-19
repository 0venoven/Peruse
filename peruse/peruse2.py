import os
import subprocess
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
import platform
# import sys
from ScanThread import ScanThread
from Database import Database
from IPRange import IPRange
import pywifi
from pywifi import const

from ui_peruse_2 import Ui_Peruse

class Peruse(QMainWindow, Ui_Peruse):
    def __init__(self, app):
        super().__init__()
        self.setupUi(self)
        self.app = app
        self.setWindowTitle("Peruse")

        self.actionQuit.triggered.connect(self.quit)
        self.actionSearch.triggered.connect(self.search)
        self.actionFilter.triggered.connect(self.filter)
        self.actionAbout.triggered.connect(self.about)
        self.actionAbout_QT.triggered.connect(self.aboutQt)
        self.scan_button.clicked.connect(self.scan)

        self.scan_thread = None
        self.db_path = r"results.db"
        self.os = platform.system()

        # Call the function to get the connected SSID
        connected_ssid = self.get_connected_ssid()

        # Get IP range from user's OS, set to PATH environment variable automatically
        ip_obj = IPRange(self.os)
        ip_range = ip_obj.get_ip_range()

        self.current_network_lineEdit.setText(connected_ssid)           # REPLACE WITH CONNECTED SSID after fixing it
        print("Connected SSID:", connected_ssid)
        self.ip_range_lineEdit.setText(ip_range)

        Database.main(self.db_path)

    def quit(self):
        self.app.quit()

    def search(self):
        self.app.quit()  # TODO: Replace with search function

    def filter(self):
        self.app.quit()  # TODO: Replace with filter function
    
    def save(self):
        # TODO: get values from UI
        Database.insert_result(self.db_path, "x of y passwords cracked", 1) # where 1 is the final score
    
    def view_all(self):
        final = Database.get_results(self.db_path)
        for row in final:
            print(row) # row is a tuple
            # TODO: show results in table properly on UI
    
    def delete(self):
        # TODO: get scan number from UI
        Database.delete_result(self.db_path, 1) # where 1 is scan number

    def get_connected_ssid(self):
        try:
            output = subprocess.check_output(["netsh", "wlan", "show", "interface"])
            output = output.decode("utf-8").replace("\r","")
            lines = output.split("\n")
            ssid = None

            for line in lines:
                if "SSID" in line:
                    ssid = line.split(":")[1].strip()
                    break

            return ssid
        except subprocess.CalledProcessError:
            return None

    def scan(self):
        def get_nmap_directory():
            return r"C:\Program Files (x86)\Nmap"

        # Users to enter their own IP range
        ip_range = self.ip_range_lineEdit.text()

        nmap_dir = get_nmap_directory()

        if self.os == 'Windows':
            os.environ['PATH'] = nmap_dir + ';' + os.environ['PATH']
        else:
            os.environ['PATH'] = nmap_dir + ':' + os.environ['PATH']

        self.scan_output_text_browser.clear()
        self.scan_output_text_browser.append(f"Scanning {ip_range}...")

        if ip_range is None:
            self.scan_output_text_browser.append(f"No IP range detected. Please make sure you are connected to the network.")

        # Create and start the scanning thread
        else:
            self.scan_thread = ScanThread(ip_range)
            self.scan_thread.scanFinished.connect(self.process_scan_results)
            self.scan_thread.start()

    def process_scan_results(self, scan_output):
        for host, result in scan_output['scan'].items():
            self.scan_output_text_browser.append(f"Scan results for {host}:\n")

            # Check if 'tcp' key is present in the result dictionary
            if 'tcp' in result:
                # Iterate over the scan result items
                for port, port_result in result['tcp'].items():
                    service_name = port_result['name']
                    state = port_result['state']
                    self.scan_output_text_browser.append(f"Port: {port}\tService: {service_name}\t\tState: {state}")

                    # Check if the service is SSH
                    if service_name.lower() == 'ssh' and state.lower() == 'open':
                        self.scan_output_text_browser.append("Running Hydra to check SSH login...\n")

                        # Run Hydra for SSH service
                        self.run_hydra(host)

            else:
                self.scan_output_text_browser.append("No TCP port information available")

            self.scan_output_text_browser.append("\n")  # Add a new line after each host

    def run_hydra(self, host):
        target = host
        port = 22
        # grimmie:My_V3ryS3cur3_P4ss
        username = "grimmie"
        password = "My_V3ryS3cur3_P4ss"

        hydra_dir = r"C:\Users\Ivan\Downloads\thc-hydra-windows-master"  # Replace with the path to hydra.exe on user's system

        try:
            # cd to hydra.exe directory
            os.chdir(hydra_dir)

            command = [
                "./hydra", "-l", username, "-p", password, f"ssh://{target}:{port}",
            ]

            # Run hydra and capture both stdout and stderr
            process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
            stdout, stderr = process.communicate()

            output = stdout + stderr
            self.update_hydra_output(output)

            # Check if output contains successful login message
            if "login successful" in output.lower():
                self.update_hydra_output("Login successful!\n")
            else:
                self.update_hydra_output("Login failed.\n")
        except FileNotFoundError:
            self.update_hydra_output("Hydra command not found. Make sure the path to the Hydra application directory is correct.\n")
        except subprocess.CalledProcessError as e:
            self.update_hydra_output(f"Hydra command execution failed with error:\n{e}\n")

    def update_hydra_output(self, output):
        self.scan_output_text_browser.append(output)

    def about(self):
        QMessageBox.information(
            self,
            "About Peruse",
            "Peruse is a Proof-of-Concept IoT Vulnerability Scanner, created to empower non-technical users to identify and mitigate vulnerabilities in their IoT devices and networks and to better study Singapore's IoT security landscape with the use of anonymized data. By using this software, you are agreeing to send your anonymized data to us for use in national security.\n\nNote: Any legal issues arising from using this software will be the sole responsibility of the user. Please use this software only on devices and networks that you own or are authorized to test."
        )

    def aboutQt(self):
        QApplication.aboutQt()