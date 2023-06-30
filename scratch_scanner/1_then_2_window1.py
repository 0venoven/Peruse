import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget

class PasswordWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Password Window")
        
        # Create password label and line edit
        password_label = QLabel("Password:")
        self.password_edit = QLineEdit()
        self.password_edit.setEchoMode(QLineEdit.Password)
        
        # Create submit button
        submit_button = QPushButton("Submit")
        submit_button.clicked.connect(self.check_password)
        
        # Set the layout
        layout = QVBoxLayout()
        layout.addWidget(password_label)
        layout.addWidget(self.password_edit)
        layout.addWidget(submit_button)
        self.setLayout(layout)
    
    def check_password(self):
        password = self.password_edit.text()
        if password == "secret":
            self.accept()  # Accept the dialog and close it
        else:
            self.password_edit.clear()

class SecondWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Second Window")
        self.setGeometry(100, 100, 300, 200)

if __name__ == "__main__":
    # Create the application
    app = QApplication(sys.argv)
    
    # Create and show the password window
    password_window = PasswordWindow()
    if password_window.exec() == QDialog.Accepted:
        # Create and show the second window
        second_window = SecondWindow()
        second_window.show()
    
    # Start the event loop
    sys.exit(app.exec())
