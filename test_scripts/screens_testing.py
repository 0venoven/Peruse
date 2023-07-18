from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QStackedWidget


class HomePage(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Home Page")
        layout = QVBoxLayout()
        layout.addWidget(QPushButton("Go to Settings", clicked=self.go_to_settings))
        self.setLayout(layout)

    def go_to_settings(self):
        self.window().stackedWidget.setCurrentIndex(1)


class SettingsPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Settings Page")
        layout = QVBoxLayout()
        layout.addWidget(QPushButton("Go to Home", clicked=self.go_to_home))
        self.setLayout(layout)

    def go_to_home(self):
        self.window().stackedWidget.setCurrentIndex(0)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.stackedWidget = QStackedWidget()
        self.home_page = HomePage()
        self.settings_page = SettingsPage()
        self.stackedWidget.addWidget(self.home_page)
        self.stackedWidget.addWidget(self.settings_page)
        self.setCentralWidget(self.stackedWidget)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
