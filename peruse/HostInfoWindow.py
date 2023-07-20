from PySide6.QtWidgets import QMainWindow, QTableWidget, QVBoxLayout, QWidget

class HostInfoWindow(QMainWindow):
    def __init__(self, scan_id, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Host Information")
        self.setGeometry(200, 200, 600, 400)

        # Create the table widget for host information
        self.table_widget = QTableWidget(self)
        self.table_widget.setColumnCount(2)
        self.table_widget.setHorizontalHeaderLabels(["Host ID", "Host Info"])

        # Disable editing
        self.table_widget.setEditTriggers(QTableWidget.NoEditTriggers)

        # Add sample data (you will replace this with data from your SQLite DB based on the provided scan_id)
        self.add_sample_data(scan_id)

        layout = QVBoxLayout()
        layout.addWidget(self.table_widget)

        central_widget = QWidget(self)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)