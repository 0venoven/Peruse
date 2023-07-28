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

        # Keep track of open ServicesWindows
        self.services_windows = []

        # Keep track of current scan output
        self.scan_dict = None

        self.scan_thread = None
        self.os = platform.system()

        # Get IP range from user's OS, set to PATH environment variable automatically
        ip_obj = IPRange(self.os)
        ip_range = ip_obj.get_ip_range()

		# Call the function to get the connected SSID
        connected_ssid = self.get_connected_ssid()

        self.actionQuit.triggered.connect(self.quit)
        self.actionSearch.triggered.connect(self.search)
        self.actionFilter.triggered.connect(self.filter)
        self.actionAbout.triggered.connect(self.about)
        self.actionAbout_QT.triggered.connect(self.aboutQt)
        self.scan_button.clicked.connect(self.scan_confirm)
        # self.view_all_button.clicked.connect(self.view_all)
        # self.delete_button.clicked.connect(self.delete)      ?

        # clear button clears both scan_details_tableWidget and host_details_tableWidget
        self.clear_button.clicked.connect(self.scan_details_tableWidget.clearContents)
        self.clear_button.clicked.connect(self.host_details_tableWidget.clearContents)

        # Disable editing
        self.scan_details_tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)
        self.host_details_tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)

        self.current_network_lineEdit.setText(connected_ssid)
        self.ip_range_lineEdit.setText(ip_range)

        Database.main()
        # add data if any
        self.populate_table()

    def populate_table(self):

        # Configure the table widget
        self.scans_tableWidget.setColumnCount(3)
        self.scans_tableWidget.setHorizontalHeaderLabels(["Scan ID", "Network Name", "Date/Time"])

        # Disable editing
        self.scans_tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)

        # Add sample data
        scan_data = [
            (1, "network1", "2021-09-01 12:00:00"),
            (2, "network2", "2021-09-02 12:00:00"),
            (3, "network3", "2021-09-03 12:00:00"),
        ]

        # get actual data from db (uncomment the below after integration with db)
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
        Database.insert_scan(self.current_network_lineEdit.text(), self.scan_dict)
    
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

        # Clear the table widgets
        self.scan_details_tableWidget.clearContents()
        self.host_details_tableWidget.clearContents()
        # self.scan_output_text_browser.append(f"Scanning {ip_range}...")

        # if ip_range is None:
        #     self.scan_output_text_browser.append(f"No IP range detected. Please make sure you are connected to the network.")

        # Create and start the scanning thread
        #else:
        self.scan_thread = ScanThread(ip_range)
        self.scan_thread.scanFinished.connect(self.process_scan_results)
        self.scan_thread.start()

    def process_scan_results(self, scan_output):
        # sample scan_output
        """
{
  'nmap': {
    'command_line': 'nmap -oX - -A -T4 192.168.158.0/24',
    'scaninfo': {
      'tcp': {
        'method': 'syn'
      }
    },
    'scanstats': {
      'timestr': 'Tue Jul 25 13:00:15 2023',
      'elapsed': '77.20',
      'uphosts': '3',
      'downhosts': '253',
      'totalhosts': '256'
    }
  },
  'scan': {
    '192.168.158.146': {
      'hostnames': [
        {
          'name': '',
          'type': ''
        }
      ],
      'addresses': {
        'ipv4': '192.168.158.146',
        'mac': '00:0C:29:50:CD:DB'
      },
      'vendor': {
        '00:0C:29:50:CD:DB': 'VMware'
      },
      'status': {
        'state': 'up',
        'reason': 'arp-response'
      },
      'uptime': {
        'seconds': '3038809',
        'lastboot': 'Tue Jun 20 08:52:45 2023'
      },
      'tcp': {
        21: {
          'state': 'open',
          'reason': 'syn-ack',
          'name': 'ftp',
          'product': 'vsftpd',
          'version': '3.0.3',
          'extrainfo': '',
          'conf': '10',
          'cpe': 'cpe:/a:vsftpd:vsftpd:3.0.3',
          'script': {
            'ftp-anon': 'Anonymous FTP login allowed (FTP code 230)\n-rw-r--r--    1 1000     1000          776 May 30  2021 note.txt',
            'ftp-syst': '\n  STAT:  \nFTP server status:\n     Connected to ::ffff:192.168.158.1\n     Logged in as ftp\n     TYPE: ASCII\n      No session bandwidth limit\n     Session timeout in seconds is 300\n     Control connection is plain text\n     Data connections will be plain text\n     At session startup, client count was 4\n     vsFTPd 3.0.3 - secure, fast, stable\nEnd of status'
          }
        },
        22: {
          'is_cracked': True,
          'state': 'open',
          'reason': 'syn-ack',
          'name': 'ssh',
          'product': 'OpenSSH',
          'version': '7.9p1 Debian 10+deb10u2',
          'extrainfo': 'protocol 2.0',
          'conf': '10',
          'cpe': 'cpe:/o:linux:linux_kernel',
          'script': {
            'ssh-hostkey': '\n  2048 c7:44:58:86:90:fd:e4:de:5b:0d:bf:07:8d:05:5d:d7 (RSA)\n  256 78:ec:47:0f:0f:53:aa:a6:05:48:84:80:94:76:a6:23 (ECDSA)\n  256 99:9c:39:11:dd:35:53:a0:29:11:20:c7:f8:bf:71:a4 (ED25519)'
          }
        },
        80: {
          'state': 'open',
          'reason': 'syn-ack',
          'name': 'http',
          'product': 'Apache httpd',
          'version': '2.4.38',
          'extrainfo': '(Debian)',
          'conf': '10',
          'cpe': 'cpe:/a:apache:http_server:2.4.38',
          'script': {
            'http-server-header': 'Apache/2.4.38 (Debian)',
            'http-title': 'Apache2 Debian Default Page: It works'
          }
        }
      },
      'osmatch': [
        {
          'name': 'Linux 4.15 - 5.8',
          'accuracy': '100',
          'line': '67250',
          'osclass': [
            {
              'type': 'general purpose',
              'vendor': 'Linux',
              'osfamily': 'Linux',
              'osgen': '4.X',
              'accuracy': '100',
              'cpe': [
                'cpe:/o:linux:linux_kernel:4'
              ]
            },
            {
              'type': 'general purpose',
              'vendor': 'Linux',
              'osfamily': 'Linux',
              'osgen': '5.X',
              'accuracy': '100',
              'cpe': [
                'cpe:/o:linux:linux_kernel:5'
              ]
            }
          ]
        }
      ]
    }
  }
}
        """

        # Set items for scan_details_tableWidget
        self.scan_details_tableWidget.insertRow(0)
        self.scan_details_tableWidget.setItem(0, 0, QTableWidgetItem(str(scan_output['nmap']['command_line'])))
        self.scan_details_tableWidget.setItem(0, 1, QTableWidgetItem(str(scan_output['nmap']['scaninfo']['tcp']['method'])))
        self.scan_details_tableWidget.setItem(0, 2, QTableWidgetItem(str(scan_output['nmap']['scanstats']['timestr'])))
        self.scan_details_tableWidget.setItem(0, 3, QTableWidgetItem(str(scan_output['nmap']['scanstats']['elapsed']) + "s"))
        self.scan_details_tableWidget.setItem(0, 4, QTableWidgetItem(str(scan_output['nmap']['scanstats']['uphosts'] + " / " + scan_output['nmap']['scanstats']['totalhosts'])))

        # Resize columns to fit contents
        self.scan_details_tableWidget.resizeColumnsToContents()
        for col in range(self.scan_details_tableWidget.columnCount()):
            column_width = self.scan_details_tableWidget.columnWidth(col)
            self.scan_details_tableWidget.setColumnWidth(col, min(column_width, 300))
        
        # Set items for host_details_tableWidget based on number of hosts detected, row count = number of services detected
        for row, host in enumerate(scan_output['scan']):
            if 'tcp' in scan_output['scan'][host]:
                for service in scan_output['scan'][host]['tcp']:
                    self.host_details_tableWidget.insertRow(row)

                    # Device IP
                    self.host_details_tableWidget.setItem(row, 0, QTableWidgetItem(str(scan_output['scan'][host]['addresses']['ipv4'])))

                    # Device Type from os match name
                    if 'osmatch' in scan_output['scan'][host]:
                        self.host_details_tableWidget.setItem(row, 1, QTableWidgetItem(str(scan_output['scan'][host]['osmatch'][0]['name'])))
                    else:
                        self.host_details_tableWidget.setItem(row, 1, QTableWidgetItem(str("N.A.")))

                    # MAC address
                    if 'mac' in scan_output['scan'][host]['addresses']:
                        mac_address = scan_output['scan'][host]['addresses']['mac']
                        self.host_details_tableWidget.setItem(row, 2, QTableWidgetItem(str(mac_address)))
                    else:
                        self.host_details_tableWidget.setItem(row, 2, QTableWidgetItem(str("N.A.")))
                    
                    # Vendor
                    if 'vendor' in scan_output['scan'][host]:
                        if scan_output['scan'][host]['vendor'] == {}:
                            self.host_details_tableWidget.setItem(row, 3, QTableWidgetItem(str("N.A.")))
                        else:
                            self.host_details_tableWidget.setItem(row, 3, QTableWidgetItem(str(scan_output['scan'][host]['vendor'][mac_address])))

                    # Device Status remove brackets
                    self.host_details_tableWidget.setItem(row, 4, QTableWidgetItem(str(scan_output['scan'][host]['status']['state'] + " due to " + scan_output['scan'][host]['status']['reason'])))

                    # Service Name
                    self.host_details_tableWidget.setItem(row, 5, QTableWidgetItem(str(scan_output['scan'][host]['tcp'][service]['name'])))

                    # Service Port
                    self.host_details_tableWidget.setItem(row, 6, QTableWidgetItem(str(service)))

                    # State
                    self.host_details_tableWidget.setItem(row, 7, QTableWidgetItem(str(scan_output['scan'][host]['tcp'][service]['state'])))

                    # Software Product
                    if 'product' in scan_output['scan'][host]['tcp'][service]:
                        self.host_details_tableWidget.setItem(row, 8, QTableWidgetItem(str(scan_output['scan'][host]['tcp'][service]['product'])))
                    else:
                        self.host_details_tableWidget.setItem(row, 8, QTableWidgetItem(str("N.A.")))

                    # Service Version
                    if 'version' in scan_output['scan'][host]['tcp'][service]:
                        self.host_details_tableWidget.setItem(row, 9, QTableWidgetItem(str(scan_output['scan'][host]['tcp'][service]['version'])))
                    else:
                        self.host_details_tableWidget.setItem(row, 9, QTableWidgetItem(str("N.A.")))

                    # version information
                    if 'extrainfo' in scan_output['scan'][host]['tcp'][service]:
                        self.host_details_tableWidget.setItem(row, 10, QTableWidgetItem(str(scan_output['scan'][host]['tcp'][service]['extrainfo'])))
                    else:
                        self.host_details_tableWidget.setItem(row, 10, QTableWidgetItem(str("N.A.")))

                    # cpe
                    if 'cpe' in scan_output['scan'][host]['tcp'][service]:
                        self.host_details_tableWidget.setItem(row, 11, QTableWidgetItem(str(scan_output['scan'][host]['tcp'][service]['cpe'])))
                    else:
                        self.host_details_tableWidget.setItem(row, 11, QTableWidgetItem(str("N.A.")))

                    # script
                    if 'script' in scan_output['scan'][host]['tcp'][service]:
                        self.host_details_tableWidget.setItem(row, 12, QTableWidgetItem(str(scan_output['scan'][host]['tcp'][service]['script'])))
                    else:
                        self.host_details_tableWidget.setItem(row, 12, QTableWidgetItem(str("N.A.")))

                    # Password Cracked
                    # Run hydra if service is ssh otherwise put "N.A."
                    if scan_output['scan'][host]['tcp'][service]['name'] == 'ssh':
                        self.run_hydra(host, row, scan_output)
                    else:
                        self.host_details_tableWidget.setItem(row, 13, QTableWidgetItem(str("N.A.")))
                        # Add to scan_output dict: "is_cracked": "" under service
                        scan_output['scan'][host]['tcp'][service]['is_cracked'] = ""

                    # TODO: Reccomendation

        # Resize columns to fit contents
        self.host_details_tableWidget.resizeColumnsToContents()
        for col in range(self.host_details_tableWidget.columnCount()):
            column_width = self.host_details_tableWidget.columnWidth(col)
            self.host_details_tableWidget.setColumnWidth(col, min(column_width, 300))
        
        # Save scan output to self.scan_dict
        self.scan_dict = scan_output
        self.save_button.clicked.connect(self.save)

    def get_hydra_directory(self):
        # hydra folder ("thc-hydra-windows-master") is now in the same directory as peruse.py, check if it exists before returning
        if os.path.exists("thc-hydra-windows-master") and os.path.isdir("thc-hydra-windows-master"):
            return os.path.join(os.getcwd(), "thc-hydra-windows-master")

    def run_hydra(self, host, row, scan_output):

        # Before running Hydra, save the current working directory of peruse.py
        peruse_cwd = os.getcwd()

        target = host
        # ssh
        port = 22
        # grimmie:My_V3ryS3cur3_P4ss
        username = "grimmie"
        password = "My_V3ryS3cur3_P4ss"

        hydra_dir = self.get_hydra_directory()
        if hydra_dir is None:
            self.update_hydra_output("Hydra binaries are not found. Please make sure it is downloaded and extracted to Downloads/thc-hydra-windows-master\n", row)
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
            self.update_hydra_output(output, row)

            # cd back to previous working directory of peruse.py
            os.chdir(peruse_cwd)

            # Check if output contains successful login message
            if "1 of 1 target successfully completed, 1 valid password found" in output:
                self.update_hydra_output("Yes", row)
                # Add to scan_output dict: "is_cracked": True under service
                scan_output['scan'][host]['tcp'][port]['is_cracked'] = "Yes"
            else:
                self.update_hydra_output("No", row)
                # Add to scan_output dict: "is_cracked": False under service
                scan_output['scan'][host]['tcp'][port]['is_cracked'] = "No"
        except FileNotFoundError:
            self.update_hydra_output("Hydra command not found. Make sure the path to the Hydra application directory is correct.\n")
        except subprocess.CalledProcessError as e:
            self.update_hydra_output(f"Hydra command execution failed with error:\n{e}\n")
        except Exception as e:
            self.update_hydra_output(f"An unexpected error has occurred:\n{e}\n")

    def update_hydra_output(self, output, row):
        self.host_details_tableWidget.setItem(row, 13, QTableWidgetItem(str(output)))

    def about(self):
        QMessageBox.information(
            self,
            "About Peruse",
            "Peruse is a Proof-of-Concept IoT Vulnerability Scanner, created to empower non-technical users to identify and mitigate vulnerabilities in their IoT devices and networks and to better study Singapore's IoT security landscape with the use of anonymized data. By using this software, you are agreeing to send your anonymized data to us for use in national security.\n\nNote: Any legal issues arising from using this software will be the sole responsibility of the user. Please use this software only on devices and networks that you own or are authorized to test."
        )

    def aboutQt(self):
        QApplication.aboutQt()
