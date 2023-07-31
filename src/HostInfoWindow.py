from PySide6.QtWidgets import QMainWindow, QTableWidget, QVBoxLayout, QWidget, QMenu, QTableWidgetItem
from ServicesWindow import ServicesWindow
from Database import Database

class HostInfoWindow(QMainWindow):
    def __init__(self, scan_id, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Host Information")
        self.setGeometry(200, 200, 600, 400)

        # Create the table widget for host information
        self.table_widget = QTableWidget(self)
        self.table_widget.setColumnCount(7)
        self.table_widget.setHorizontalHeaderLabels(["Host ID", "Scan ID", "Host IP", "Device Type", "MAC address", "Vendor", "Device Status"])

        # Disable editing
        self.table_widget.setEditTriggers(QTableWidget.NoEditTriggers)

        # Populate table
        self.populate_table(scan_id)

        layout = QVBoxLayout()
        layout.addWidget(self.table_widget)

        central_widget = QWidget(self)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def populate_table(self, scan_id):

        # get actual data from the database
        host_data = Database.get_hosts(scan_id)

        for row, (host_id, scan_id, host_ip, device_type, mac_address, vendor, device_status) in enumerate(host_data):
            self.table_widget.insertRow(row)
            self.table_widget.setItem(row, 0, QTableWidgetItem(str(host_id)))
            self.table_widget.setItem(row, 1, QTableWidgetItem(str(scan_id)))
            self.table_widget.setItem(row, 2, QTableWidgetItem(host_ip))
            self.table_widget.setItem(row, 3, QTableWidgetItem(device_type))
            self.table_widget.setItem(row, 4, QTableWidgetItem(mac_address))
            self.table_widget.setItem(row, 5, QTableWidgetItem(vendor))
            self.table_widget.setItem(row, 6, QTableWidgetItem(device_status))

    def contextMenuEvent(self, event):
        menu = QMenu(self)
        selected_row = self.table_widget.currentRow()
        if selected_row >= 0:
            host_id = self.table_widget.item(selected_row, 0).text()
            menu.addAction("View Services Information", lambda: self.show_services_info(host_id))

        menu.exec(event.globalPos())

    def show_services_info(self, host_id):
        # Check if the services_window already exists for the selected host
        for services_window in self.parent().services_windows:
            if services_window.host_id == host_id:
                services_window.show()
                services_window.activateWindow()
                break
        else:
            services_window = ServicesWindow(host_id, parent=self.parent())
            self.parent().services_windows.append(services_window)
            services_window.show()