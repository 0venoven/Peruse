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

        # Disable editing
        self.scan_details_tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)
        self.host_details_tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)

        # Insert the data into the TableWidget here
        # self.save_button.clicked.connect(self.save)?
        # self.view_all_button.clicked.connect(self.view_all)?
        # self.delete_button.clicked.connect(self.delete)?
        # Take from db

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

        self.host_details_tableWidget.clearContents()
        # self.scan_output_text_browser.clear()
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
            "nmap":{
                "command_line":"nmap -oX - 192.168.5.0/24",
                "scaninfo":{
                    "tcp":{
                        "method":"syn",
                        "services":"1,3-4,6-7,9,13,17,19-26,30,32-33,37,42-43,49,53,70,79-85,88-90,99-100,106,109-111,113,119,125,135,139,143-144,146,161,163,179,199,211-212,222,254-256,259,264,280,301,306,311,340,366,389,406-407,416-417,425,427,443-445,458,464-465,481,497,500,512-515,524,541,543-545,548,554-555,563,587,593,616-617,625,631,636,646,648,666-668,683,687,691,700,705,711,714,720,722,726,749,765,777,783,787,800-801,808,843,873,880,888,898,900-903,911-912,981,987,990,992-993,995,999-1002,1007,1009-1011,1021-1100,1102,1104-1108,1110-1114,1117,1119,1121-1124,1126,1130-1132,1137-1138,1141,1145,1147-1149,1151-1152,1154,1163-1166,1169,1174-1175,1183,1185-1187,1192,1198-1199,1201,1213,1216-1218,1233-1234,1236,1244,1247-1248,1259,1271-1272,1277,1287,1296,1300-1301,1309-1311,1322,1328,1334,1352,1417,1433-1434,1443,1455,1461,1494,1500-1501,1503,1521,1524,1533,1556,1580,1583,1594,1600,1641,1658,1666,1687-1688,1700,1717-1721,1723,1755,1761,1782-1783,1801,1805,1812,1839-1840,1862-1864,1875,1900,1914,1935,1947,1971-1972,1974,1984,1998-2010,2013,2020-2022,2030,2033-2035,2038,2040-2043,2045-2049,2065,2068,2099-2100,2103,2105-2107,2111,2119,2121,2126,2135,2144,2160-2161,2170,2179,2190-2191,2196,2200,2222,2251,2260,2288,2301,2323,2366,2381-2383,2393-2394,2399,2401,2492,2500,2522,2525,2557,2601-2602,2604-2605,2607-2608,2638,2701-2702,2710,2717-2718,2725,2800,2809,2811,2869,2875,2909-2910,2920,2967-2968,2998,3000-3001,3003,3005-3007,3011,3013,3017,3030-3031,3052,3071,3077,3128,3168,3211,3221,3260-3261,3268-3269,3283,3300-3301,3306,3322-3325,3333,3351,3367,3369-3372,3389-3390,3404,3476,3493,3517,3527,3546,3551,3580,3659,3689-3690,3703,3737,3766,3784,3800-3801,3809,3814,3826-3828,3851,3869,3871,3878,3880,3889,3905,3914,3918,3920,3945,3971,3986,3995,3998,4000-4006,4045,4111,4125-4126,4129,4224,4242,4279,4321,4343,4443-4446,4449,4550,4567,4662,4848,4899-4900,4998,5000-5004,5009,5030,5033,5050-5051,5054,5060-5061,5080,5087,5100-5102,5120,5190,5200,5214,5221-5222,5225-5226,5269,5280,5298,5357,5405,5414,5431-5432,5440,5500,5510,5544,5550,5555,5560,5566,5631,5633,5666,5678-5679,5718,5730,5800-5802,5810-5811,5815,5822,5825,5850,5859,5862,5877,5900-5904,5906-5907,5910-5911,5915,5922,5925,5950,5952,5959-5963,5987-5989,5998-6007,6009,6025,6059,6100-6101,6106,6112,6123,6129,6156,6346,6389,6502,6510,6543,6547,6565-6567,6580,6646,6666-6669,6689,6692,6699,6779,6788-6789,6792,6839,6881,6901,6969,7000-7002,7004,7007,7019,7025,7070,7100,7103,7106,7200-7201,7402,7435,7443,7496,7512,7625,7627,7676,7741,7777-7778,7800,7911,7920-7921,7937-7938,7999-8002,8007-8011,8021-8022,8031,8042,8045,8080-8090,8093,8099-8100,8180-8181,8192-8194,8200,8222,8254,8290-8292,8300,8333,8383,8400,8402,8443,8500,8600,8649,8651-8652,8654,8701,8800,8873,8888,8899,8994,9000-9003,9009-9011,9040,9050,9071,9080-9081,9090-9091,9099-9103,9110-9111,9200,9207,9220,9290,9415,9418,9485,9500,9502-9503,9535,9575,9593-9595,9618,9666,9876-9878,9898,9900,9917,9929,9943-9944,9968,9998-10004,10009-10010,10012,10024-10025,10082,10180,10215,10243,10566,10616-10617,10621,10626,10628-10629,10778,11110-11111,11967,12000,12174,12265,12345,13456,13722,13782-13783,14000,14238,14441-14442,15000,15002-15004,15660,15742,16000-16001,16012,16016,16018,16080,16113,16992-16993,17877,17988,18040,18101,18988,19101,19283,19315,19350,19780,19801,19842,20000,20005,20031,20221-20222,20828,21571,22939,23502,24444,24800,25734-25735,26214,27000,27352-27353,27355-27356,27715,28201,30000,30718,30951,31038,31337,32768-32785,33354,33899,34571-34573,35500,38292,40193,40911,41511,42510,44176,44442-44443,44501,45100,48080,49152-49161,49163,49165,49167,49175-49176,49400,49999-50003,50006,50300,50389,50500,50636,50800,51103,51493,52673,52822,52848,52869,54045,54328,55055-55056,55555,55600,56737-56738,57294,57797,58080,60020,60443,61532,61900,62078,63331,64623,64680,65000,65129,65389"
                    }
                },
                "scanstats":{
                    "downhosts":"253",
                    "elapsed":"10.70",
                    "timestr":"Mon Jul 24 17:04:43 2023",
                    "totalhosts":"256",
                    "uphosts":"3"
                }
            },
            "scan":{
                "192.168.5.1":{
                    "hostnames":[
                        {
                            "name":"",
                            "type":""
                        }
                    ],
                    "addresses":{
                        "ipv4":"192.168.5.1"
                    },
                    "vendor":{
                        
                    },
                    "status":{
                        "state":"up",
                        "reason":"localhost-response"
                    },
                    "tcp":{
                        "135":{
                            "state":"open",
                            "reason":"syn-ack",
                            "name":"msrpc",
                            "product":"",
                            "version":"",
                            "extrainfo":"",
                            "conf":"3",
                            "cpe":""
                        },
                        "139":{
                            "state":"open",
                            "reason":"syn-ack",
                            "name":"netbios-ssn",
                            "product":"",
                            "version":"",
                            "extrainfo":"",
                            "conf":"3",
                            "cpe":""
                        },
                        "445":{
                            "state":"open",
                            "reason":"syn-ack",
                            "name":"microsoft-ds",
                            "product":"",
                            "version":"",
                            "extrainfo":"",
                            "conf":"3",
                            "cpe":""
                        },
                        "902":{
                            "state":"open",
                            "reason":"syn-ack",
                            "name":"iss-realsecure",
                            "product":"",
                            "version":"",
                            "extrainfo":"",
                            "conf":"3",
                            "cpe":""
                        },
                        "912":{
                            "state":"open",
                            "reason":"syn-ack",
                            "name":"apex-mesh",
                            "product":"",
                            "version":"",
                            "extrainfo":"",
                            "conf":"3",
                            "cpe":""
                        }
                    }
                },
                "192.168.5.129":{
                    "hostnames":[
                        {
                            "name":"",
                            "type":""
                        }
                    ],
                    "addresses":{
                        "ipv4":"192.168.5.129",
                        "mac":"00:0C:29:2A:D6:F7"
                    },
                    "vendor":{
                        "00:0C:29:2A:D6:F7":"VMware"
                    },
                    "status":{
                        "state":"up",
                        "reason":"arp-response"
                    }
                },
                "192.168.5.254":{
                    "hostnames":[
                        {
                            "name":"",
                            "type":""
                        }
                    ],
                    "addresses":{
                        "ipv4":"192.168.5.254",
                        "mac":"00:50:56:F2:BA:7B"
                    },
                    "vendor":{
                        "00:50:56:F2:BA:7B":"VMware"
                    },
                    "status":{
                        "state":"up",
                        "reason":"arp-response"
                    }
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
            self.scan_details_tableWidget.setColumnWidth(col, min(column_width, 200))

        # Set items for host_details_tableWidget
        self.host_details_tableWidget.setColumnCount(1)
        self.host_details_tableWidget.setRowCount(1)
        self.host_details_tableWidget.setHorizontalHeaderLabels(["Host Details"])

        # Dump the scan output to the table widget, set entire scan output into one cell
        self.host_details_tableWidget.setItem(0, 0, QTableWidgetItem(str(scan_output['scan'])))
        

        # for host, result in scan_output['scan'].items():
        #     self.scan_output_text_browser.append(f"Scan results for {host}:\n")

        #     # Check if 'tcp' key is present in the result dictionary
        #     if 'tcp' in result:
        #         # Iterate over the scan result items
        #         for port, port_result in result['tcp'].items():
        #             service_name = port_result['name']
        #             state = port_result['state']
        #             self.scan_output_text_browser.append(f"Port: {port}\tService: {service_name}\t\tState: {state}")

        #             # Check if the service is SSH
        #             if service_name.lower() == 'ssh' and state.lower() == 'open':
        #                 self.scan_output_text_browser.append("Running Hydra to check SSH login...\n")

        #                 # Run Hydra for SSH service
        #                 self.run_hydra(host)

        #     else:
        #         self.scan_output_text_browser.append("No TCP port information available")

        #     self.scan_output_text_browser.append("\n")  # Add a new line after each host

    def get_hydra_directory(self):
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

    # def update_hydra_output(self, output):
    #     self.scan_output_text_browser.append(output)

    def about(self):
        QMessageBox.information(
            self,
            "About Peruse",
            "Peruse is a Proof-of-Concept IoT Vulnerability Scanner, created to empower non-technical users to identify and mitigate vulnerabilities in their IoT devices and networks and to better study Singapore's IoT security landscape with the use of anonymized data. By using this software, you are agreeing to send your anonymized data to us for use in national security.\n\nNote: Any legal issues arising from using this software will be the sole responsibility of the user. Please use this software only on devices and networks that you own or are authorized to test."
        )

    def aboutQt(self):
        QApplication.aboutQt()
