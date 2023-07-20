import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication

from peruse2 import Peruse  # Import the Peruse class from peruse2.py
from CaptchaWindow import CaptchaWindow  # Import the CaptchaWindow class from CaptchaWindow.py

if __name__ == "__main__":
    app = QApplication(sys.argv)

    captcha_window = CaptchaWindow()
    captcha_window.show()

    sys.exit(app.exec())
