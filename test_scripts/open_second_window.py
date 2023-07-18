import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window")
        
        # Create the button
        button = QPushButton("Open Second Window")
        button.clicked.connect(self.open_second_window)
        
        # Set the layout
        layout = QVBoxLayout()
        layout.addWidget(button)
        
        # Create a central widget and set the layout
        central_widget = QWidget()
        central_widget.setLayout(layout)
        
        # Set the central widget of the main window
        self.setCentralWidget(central_widget)
    
    def open_second_window(self):
        self.second_window = SecondWindow()
        self.second_window.show()

class SecondWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Second Window")
        self.setGeometry(100, 100, 300, 200)

if __name__ == "__main__":
    # Create the application
    app = QApplication(sys.argv)
    
    # Create and show the main window
    main_window = MainWindow()
    main_window.show()
    
    # Start the event loop
    sys.exit(app.exec())
