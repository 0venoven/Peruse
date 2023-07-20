from PySide6.QtWidgets import QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget

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