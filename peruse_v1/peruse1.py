from PySide6.QtCore import QThread, Signal
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox

from ui_peruse import Ui_Peruse

import os
import platform
import sys
import nmap


class ScanThread(QThread):
    scanFinished = Signal(dict)

    def __init__(self, ip_range):
        super().__init__()
        self.ip_range = ip_range

    def run(self):
        nm = nmap.PortScanner()
        scan_output = nm.scan(hosts=self.ip_range, arguments="")
        self.scanFinished.emit(scan_output)


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
        self.ip_range_line_edit.returnPressed.connect(self.scan)
        self.scan_button.clicked.connect(self.scan)

    def quit(self):
        self.app.quit()

    def search(self):
        self.app.quit()  # TODO: Replace with search function

    def filter(self):
        self.app.quit()  # TODO: Replace with filter function

    def scan(self):
        def get_nmap_directory():
            return r"C:\Program Files (x86)\Nmap"

        ip_range = self.ip_range_line_edit.text()

        nmap_dir = get_nmap_directory()

        if platform.system() == 'Windows':
            os.environ['PATH'] = nmap_dir + ';' + os.environ['PATH']
        else:
            os.environ['PATH'] = nmap_dir + ':' + os.environ['PATH']

        self.scan_output_text_browser.clear()
        self.scan_output_text_browser.append(f"Scanning {ip_range}...")

        # Create and start the scanning thread
        self.scan_thread = ScanThread(ip_range)
        self.scan_thread.scanFinished.connect(self.display_scan_results)
        self.scan_thread.start()

    def display_scan_results(self, scan_output):
        for host, result in scan_output['scan'].items():
            self.scan_output_text_browser.append(f"Scan results for {host}:\n")

            # Check if 'tcp' key is present in the result dictionary
            if 'tcp' in result:
                # Iterate over the scan result items
                for port, port_result in result['tcp'].items():
                    service_name = port_result['name']
                    state = port_result['state']
                    self.scan_output_text_browser.append(f"Port: {port}\tService: {service_name}\t\tState: {state}")
            else:
                self.scan_output_text_browser.append("No TCP port information available")

            self.scan_output_text_browser.append("\n")  # Add a new line after each host

    def about(self):
        QMessageBox.information(
            self,
            "About Peruse",
            "Peruse is a Proof-of-Concept IoT Vulnerability Scanner, created to empower non-technical users to identify and mitigate vulnerabilities in their IoT devices and networks and to better study Singapore's IoT security landscape with the use of anonymized data. By using this software, you are agreeing to send your anonymized data to us for use in national security.\n\nNote: Any legal issues arising from using this software will be the sole responsibility of the user. Please use this software only on devices and networks that you own or are authorized to test."
        )

    def aboutQt(self):
        QApplication.aboutQt()
