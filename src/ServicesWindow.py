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
        self.table_widget.setColumnCount(12)
        self.table_widget.setHorizontalHeaderLabels(["Service ID", "Host ID", "Service Name", "Port Number", "State", "Software Product", "Service Version", "Version Information", "CPE", "Script Output", "Password Cracked", "Recommendation"])

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

        # get actual data from the database
        service_data = Database.get_services(host_id)

        for row, (service_id, host_id, service_name, service_port, state, software_product, service_version, version_information, cpe, script, pw_cracked, recommendation) in enumerate(service_data):
            self.table_widget.insertRow(row)
            self.table_widget.setItem(row, 0, QTableWidgetItem(str(service_id)))
            self.table_widget.setItem(row, 1, QTableWidgetItem(str(host_id)))
            self.table_widget.setItem(row, 2, QTableWidgetItem(service_name))
            self.table_widget.setItem(row, 3, QTableWidgetItem(str(service_port)))
            self.table_widget.setItem(row, 4, QTableWidgetItem(state))
            self.table_widget.setItem(row, 5, QTableWidgetItem(software_product))
            self.table_widget.setItem(row, 6, QTableWidgetItem(service_version))
            self.table_widget.setItem(row, 7, QTableWidgetItem(version_information))
            self.table_widget.setItem(row, 8, QTableWidgetItem(cpe))
            self.table_widget.setItem(row, 9, QTableWidgetItem(script))

            if(pw_cracked == 0):
                pw_cracked = "No"
            elif(pw_cracked == 1):
                pw_cracked = "Yes"

            self.table_widget.setItem(row, 10, QTableWidgetItem(pw_cracked))
            self.table_widget.setItem(row, 11, QTableWidgetItem(recommendation))