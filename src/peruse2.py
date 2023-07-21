import os
import subprocess
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem, QTableWidget, QMenu
import platform
from ScanThread import ScanThread
from Database import Database
from IPRange import IPRange
from HostInfoWindow import HostInfoWindow
from ScanConfirmWindow import ScanConfirmWindow

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
        self.scan_button.clicked.connect(self.scan_confirm)

        # Insert the data into the TableWidget here
        # self.save_button.clicked.connect(self.save)?
        # self.view_all_button.clicked.connect(self.view_all)?
        # self.delete_button.clicked.connect(self.delete)?
        # Take from db

        # add in the sample testing data
        self.add_sample_data()

        # Keep track of open ServicesWindows
        self.services_windows = []

        self.scan_thread = None
        self.os = platform.system()

        # Call the function to get the connected SSID
        connected_ssid = self.get_connected_ssid()

        # Get IP range from user's OS, set to PATH environment variable automatically
        ip_obj = IPRange(self.os)
        ip_range = ip_obj.get_ip_range()

        self.current_network_lineEdit.setText(connected_ssid)
        self.ip_range_lineEdit.setText(ip_range)

        Database.main()

    # REMOVE THIS AFTER THE INTEGRATION WITH DATABASE IS DONE
    def add_sample_data(self):

        # Configure the table widget
        self.scans_tableWidget.setColumnCount(3)
        self.scans_tableWidget.setHorizontalHeaderLabels(["Scan ID", "Scan Result"])

        # Disable editing
        self.scans_tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)

        # Add sample data
        scan_data = [
            (1, "network1", "2021-09-01 12:00:00"),
            (2, "network2", "2021-09-02 12:00:00"),
            (3, "network3", "2021-09-03 12:00:00"),
        ]

        # get actual data from db
        # scan_data = Database.get_all_scans()

        # Insert the data into the TableWidget
        for row, (scan_id, network_name, datetime) in enumerate(scan_data):
            self.scans_tableWidget.insertRow(row)
            self.scans_tableWidget.setItem(row, 0, QTableWidgetItem(str(scan_id)))
            self.scans_tableWidget.setItem(row, 1, QTableWidgetItem(network_name))
            self.scans_tableWidget.setItem(row, 2, QTableWidgetItem(datetime))

    
    def contextMenuEvent(self, event):
        menu = QMenu(self)
        selected_row = self.scans_tableWidget.currentRow()
        if selected_row >= 0:
            scan_id = int(self.scans_tableWidget.item(selected_row, 0).text())
            menu.addAction("View Host Information", lambda: self.show_host_info(scan_id))

        menu.exec(event.globalPos())

    def scan_confirm(self):
        self.scan_confirm_window = ScanConfirmWindow()
        self.scan_confirm_window.confirmed.connect(self.scan)
        self.scan_confirm_window.canceled.connect(self.scan_confirm_window.close)
        self.scan_confirm_window.show()

    def show_host_info(self, scan_id):
        self.host_info_window = HostInfoWindow(scan_id, parent=self)
        self.host_info_window.show()

    def quit(self):
        self.app.quit()

    def search(self):
        self.app.quit()  # TODO: Replace with search function

    def filter(self):
        self.app.quit()  # TODO: Replace with filter function
    
    def save(self):
        # TODO: edit this fn to get the necessary data from UI
        Database.insert_scan(self.db_path, self.current_network_lineEdit.text())
    
    def view_all(self):
        final = Database.get_all_scans(self.db_path)
        for row in final:
            print(row) # row is a tuple
            # TODO: show results in table properly on UI
    
    def delete(self):
        # TODO: get scan number from UI
        Database.delete_result(self.db_path, 1) # where 1 is scan id

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

    def get_hydra_directory():
        downloads_dir = os.path.join(os.path.expanduser('~'), 'Downloads')
        hydra_folder = os.path.join(downloads_dir, 'thc-hydra-windows-master')
        if os.path.exists(hydra_folder) and os.path.isdir(hydra_folder):
            return hydra_folder
        else:
            return None

    def run_hydra(self, host):
        target = host
        port = 22
        # grimmie:My_V3ryS3cur3_P4ss
        username = "grimmie"
        password = "My_V3ryS3cur3_P4ss"

        hydra_dir = self.get_hydra_directory()
        if hydra_dir is None:
            self.update_hydra_output("Hydra binaries are not found. Please make sure it is downloaded and extracted to Downloads/thc-hydra-windows-master\n")
            return

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
