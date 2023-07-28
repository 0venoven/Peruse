from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QPushButton, QGridLayout, QSizePolicy, QLineEdit, QTableWidget, QFrame
from PySide6.QtCore import Qt

class PeruseApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Peruse")
        self.resize(1179, 735)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Create the grid layout
        grid_layout = QGridLayout(central_widget)
        grid_layout.setSizeConstraint(QGridLayout.SetMinAndMaxSize)
        grid_layout.setContentsMargins(20, 20, 20, 20)  # Set some margins for better appearance

        # Add widgets to the layout
        scan_title_label = QLabel("Scan a network")
        grid_layout.addWidget(scan_title_label, 0, 0, 1, 3, alignment=Qt.AlignCenter)

        scan_button = QPushButton("Scan")
        scan_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        grid_layout.addWidget(scan_button, 1, 2)

        # Add more widgets and rows/columns as needed
        current_network_label = QLabel("Current network:")
        current_network_line_edit = QLineEdit()
        ip_range_label = QLabel("IP range:")
        ip_range_line_edit = QLineEdit()

        grid_layout.addWidget(current_network_label, 2, 0)
        grid_layout.addWidget(current_network_line_edit, 2, 1, 1, 2)
        grid_layout.addWidget(ip_range_label, 3, 0)
        grid_layout.addWidget(ip_range_line_edit, 3, 1, 1, 2)

        network_tip_label = QLabel("If this is not a network that you own/want to scan, please change to the desired network. Also, as dictionary attacks (multiple login attempts) are used, please take note that it could potentially lock up your devices or cause other forms of harm.")
        network_tip_label.setWordWrap(True)
        grid_layout.addWidget(network_tip_label, 4, 0, 1, 3)

        horizontal_line_1 = QFrame()
        horizontal_line_1.setFrameShape(QFrame.HLine)
        horizontal_line_1.setFrameShadow(QFrame.Sunken)
        grid_layout.addWidget(horizontal_line_1, 5, 0, 1, 3)

        is_scanning_label = QLabel("Not scanning currently, start a scan?")
        grid_layout.addWidget(is_scanning_label, 6, 0, 1, 3)

        scan_details_label = QLabel("Scan details:")
        grid_layout.addWidget(scan_details_label, 7, 0)

        scan_details_table = QTableWidget(2, 5)  # Example table with 2 rows and 5 columns
        grid_layout.addWidget(scan_details_table, 8, 0, 1, 3)

        save_button = QPushButton("Save")
        save_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        grid_layout.addWidget(save_button, 9, 0)

        clear_button = QPushButton("Clear")
        clear_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        grid_layout.addWidget(clear_button, 9, 1)

        host_details_label = QLabel("Host details:")
        grid_layout.addWidget(host_details_label, 10, 0)

        host_details_table = QTableWidget(3, 6)  # Example table with 3 rows and 6 columns
        grid_layout.addWidget(host_details_table, 11, 0, 1, 3)

        horizontal_line_2 = QFrame()
        horizontal_line_2.setFrameShape(QFrame.HLine)
        horizontal_line_2.setFrameShadow(QFrame.Sunken)
        grid_layout.addWidget(horizontal_line_2, 12, 0, 1, 3)

        is_searching_label = QLabel("Not searching currently, start a search?")
        grid_layout.addWidget(is_searching_label, 13, 0, 1, 3)

        # Add more widgets and rows/columns as needed

        # Set stretch factors for rows and columns to control resizing behavior
        grid_layout.setRowStretch(0, 0)  # Scan title label
        grid_layout.setRowStretch(1, 0)  # Scan button
        grid_layout.setRowStretch(2, 0)  # Current network label and line edit
        grid_layout.setRowStretch(3, 0)  # IP range label and line edit
        grid_layout.setRowStretch(4, 0)  # Network tip label
        grid_layout.setRowStretch(5, 0)  # Horizontal line 1
        grid_layout.setRowStretch(6, 0)  # Is scanning label
        grid_layout.setRowStretch(7, 0)  # Scan details label
        grid_layout.setRowStretch(8, 1)  # Scan details table (Expanding row)
        grid_layout.setRowStretch(9, 0)  # Save and clear buttons
        grid_layout.setRowStretch(10, 0)  # Host details label
        grid_layout.setRowStretch(11, 1)  # Host details table (Expanding row)
        grid_layout.setRowStretch(12, 0)  # Horizontal line 2
        grid_layout.setRowStretch(13, 0)  # Is searching label

        grid_layout.setColumnStretch(0, 1)  # Column 0
        grid_layout.setColumnStretch(1, 1)  # Column 1
        grid_layout.setColumnStretch(2, 1)  # Column 2


if __name__ == "__main__":
    app = QApplication([])
    window = PeruseApp()
    window.show()
    app.exec()
