from PySide6.QtWidgets import QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
from Database import Database

class ServicesWindow(QMainWindow):
    def __init__(self, host_id, parent=None):
        super().__init__(parent)
        self.host_id = host_id
        self.setWindowTitle("Services Information")
        self.setGeometry(300, 300, 500, 300)

        # Create the table widget for services information
        self.table_widget = QTableWidget(self)
        self.table_widget.setColumnCount(2)
        self.table_widget.setHorizontalHeaderLabels(["Service ID", "Service Info"])

        # Disable editing
        self.table_widget.setEditTriggers(QTableWidget.NoEditTriggers)

        # populate table
        self.populate_table(host_id)

        layout = QVBoxLayout()
        layout.addWidget(self.table_widget)

        central_widget = QWidget(self)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def populate_table(self, host_id):
        # This is just an example to populate the table widget
        service_data = [
            (1, host_id, "ssh", 22, "yes"),
            (2, host_id, "ssh", 22, "no"),
        ]

        # get actual data from the database
        # service_data = Database.get_services(host_id)

        for row, (service_id, host_id, service_name, port_no, pw_cracked) in enumerate(service_data):
            self.table_widget.insertRow(row)
            self.table_widget.setItem(row, 0, QTableWidgetItem(service_id))
            self.table_widget.setItem(row, 1, QTableWidgetItem(host_id))
            self.table_widget.setItem(row, 2, QTableWidgetItem(service_name))
            self.table_widget.setItem(row, 3, QTableWidgetItem(port_no))
            self.table_widget.setItem(row, 4, QTableWidgetItem(pw_cracked))