from PySide6.QtWidgets import QVBoxLayout, QDialog, QLabel, QVBoxLayout, QPushButton, QDialogButtonBox
from PySide6.QtCore import Signal

class ScanConfirmWindow(QDialog):
    confirmed = Signal()  # Signal emitted when the user confirms the scan
    canceled = Signal()   # Signal emitted when the user cancels the scan

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Scan Confirmation")

        self.confirm_label = QLabel("Make sure that the IP range is correct and that the network is correct.\n If not, please change them. If correct, click on 'Confirm and start scanning'.\n Otherwise, click on 'Cancel scan'")

        self.button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.button_box.accepted.connect(self.confirm_scan)
        self.button_box.rejected.connect(self.cancel_scan)

        layout = QVBoxLayout()
        layout.addWidget(self.confirm_label)
        layout.addWidget(self.button_box)
        self.setLayout(layout)

    def confirm_scan(self):
        self.confirmed.emit()  # Emit the confirmed signal
        self.close()

    def cancel_scan(self):
        self.canceled.emit()   # Emit the canceled signal
        self.close()


# from PySide6.QtWidgets import QVBoxLayout, QDialog, QLabel, QVBoxLayout, QPushButton

# class ScanConfirmWindow(QDialog):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Scan Confirmation")

#         # Qlabel for the confirmation window
#         self.confirm_label = QLabel("This window is to confirm the scan, start scanning, and that if need be, to cancel the scan one has to close the window thereby terminating the nmap process")

#         # Button to confirm the scan
#         self.confirm_button = QPushButton("Confirm and start scanning")
#         self.confirm_button.clicked.connect(self.confirm_scan)

#         # Button to cancel the scan
#         self.cancel_button = QPushButton("Cancel scan")
#         self.cancel_button.clicked.connect(self.cancel_scan)

#         layout = QVBoxLayout()
#         layout.addWidget(self.confirm_label)
#         layout.addWidget(self.confirm_button)
#         self.setLayout(layout)

#     def confirm_scan(self):
#         self.close()
#         return 1

#     def cancel_scan(self):
#         self.close()
#         return 0