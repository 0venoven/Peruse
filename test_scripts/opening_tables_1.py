import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Vulnerability Scanner")
        self.setGeometry(100, 100, 800, 600)

        # Create the table widget
        self.table_widget = QTableWidget(self)
        self.table_widget.setColumnCount(2)
        self.table_widget.setHorizontalHeaderLabels(["Scan ID", "Scan Result"])
        self.table_widget.doubleClicked.connect(self.on_row_double_clicked)

        # Add sample data (you will replace this with data from your SQLite DB)
        self.add_sample_data()

        layout = QVBoxLayout()
        layout.addWidget(self.table_widget)

        central_widget = QWidget(self)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def add_sample_data(self):
        # This is just an example to populate the table widget, you'll replace this with data from your SQLite DB.
        scan_data = [
            (1, "Vulnerable"),
            (2, "Clean"),
            (3, "Vulnerable"),
        ]

        for row, (scan_id, scan_result) in enumerate(scan_data):
            self.table_widget.insertRow(row)
            self.table_widget.setItem(row, 0, QTableWidgetItem(str(scan_id)))
            self.table_widget.setItem(row, 1, QTableWidgetItem(scan_result))

    def on_row_double_clicked(self, index):
        # Get the selected scan ID
        selected_scan_id = self.table_widget.item(index.row(), 0).text()

        # Open another window with host information using the selected scan ID
        self.host_info_window = HostInfoWindow(selected_scan_id)
        self.host_info_window.show()

class HostInfoWindow(QMainWindow):
    def __init__(self, scan_id):
        super().__init__()
        self.setWindowTitle("Host Information")
        self.setGeometry(200, 200, 600, 400)

        # Create the table widget for host information
        self.table_widget = QTableWidget(self)
        self.table_widget.setColumnCount(2)
        self.table_widget.setHorizontalHeaderLabels(["Host ID", "Host Info"])
        self.table_widget.doubleClicked.connect(self.on_row_double_clicked)

        # Add sample data (you will replace this with data from your SQLite DB based on the provided scan_id)
        self.add_sample_data(scan_id)

        layout = QVBoxLayout()
        layout.addWidget(self.table_widget)

        central_widget = QWidget(self)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def add_sample_data(self, scan_id):
        # This is just an example to populate the table widget, you'll replace this with data from your SQLite DB.
        host_data = [
            (f"{scan_id}-1", "Host 1 Info"),
            (f"{scan_id}-2", "Host 2 Info"),
        ]

        for row, (host_id, host_info) in enumerate(host_data):
            self.table_widget.insertRow(row)
            self.table_widget.setItem(row, 0, QTableWidgetItem(host_id))
            self.table_widget.setItem(row, 1, QTableWidgetItem(host_info))

    def on_row_double_clicked(self, index):
        # Get the selected host ID
        selected_host_id = self.table_widget.item(index.row(), 0).text()

        # Open another window with services (and vulnerabilities) information using the selected host ID
        self.services_window = ServicesWindow(selected_host_id)
        self.services_window.show()

class ServicesWindow(QMainWindow):
    def __init__(self, host_id):
        super().__init__()
        self.setWindowTitle("Services Information")
        self.setGeometry(300, 300, 500, 300)

        # Create the table widget for services information
        self.table_widget = QTableWidget(self)
        self.table_widget.setColumnCount(2)
        self.table_widget.setHorizontalHeaderLabels(["Service ID", "Service Info"])

        # Add sample data (you will replace this with data from your SQLite DB based on the provided host_id)
        self.add_sample_data(host_id)

        layout = QVBoxLayout()
        layout.addWidget(self.table_widget)

        central_widget = QWidget(self)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def add_sample_data(self, host_id):
        # This is just an example to populate the table widget, you'll replace this with data from your SQLite DB.
        service_data = [
            (f"{host_id}-1", "Service 1 Info"),
            (f"{host_id}-2", "Service 2 Info"),
        ]

        for row, (service_id, service_info) in enumerate(service_data):
            self.table_widget.insertRow(row)
            self.table_widget.setItem(row, 0, QTableWidgetItem(service_id))
            self.table_widget.setItem(row, 1, QTableWidgetItem(service_info))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
