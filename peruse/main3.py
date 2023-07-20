import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QDialog, QLabel, QVBoxLayout, QPushButton, QLineEdit, QMessageBox
from PySide6.QtGui import QPixmap
from captcha.image import ImageCaptcha
import string
import random

MAX_ATTEMPTS = 3

from peruse2 import Peruse  # Import the Peruse class from peruse2.py

class CaptchaWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Captcha Verification")

        self.attempts = 0  # Counter for the number of attempts
        self.captcha_checked = False  # Flag to track whether captcha check has been performed

        self.image_label = QLabel()
        self.generate_captcha()

        self.captcha_input = QLineEdit()
        self.submit_button = QPushButton("Submit")
        self.submit_button.clicked.connect(self.check_captcha)

        self.attempts_label = QLabel()  # Label to display the number of attempts
        self.update_attempts_label()

        layout = QVBoxLayout()
        layout.addWidget(self.image_label)
        layout.addWidget(self.captcha_input)
        layout.addWidget(self.submit_button)
        layout.addWidget(self.attempts_label)
        self.setLayout(layout)

    def generate_captcha(self):
        image = ImageCaptcha()

        # Generate image captcha with random text
        captcha_text = self.generate_random_text()
        data = image.generate(captcha_text)

        # Save the image to a file
        image_path = "captcha.png"
        image.write(captcha_text, image_path)

        # Display the captcha image in the app
        pixmap = QPixmap(image_path)
        self.image_label.setPixmap(pixmap)

        # Store the correct captcha text
        self.correct_captcha_text = captcha_text

    def generate_random_text(self):
        # Generate a random combination of numeric and uppercase alphabetic characters
        characters = string.digits + string.ascii_uppercase
        captcha_text = ''.join(random.choice(characters) for _ in range(4))
        return captcha_text

    def check_captcha(self):
        if self.captcha_checked:
            return

        entered_text = self.captcha_input.text()

        if entered_text == self.correct_captcha_text:
            # Correct captcha entered, close the captcha window and open the Peruse application
            self.captcha_checked = True
            self.close()
            self.peruse_app = Peruse(QApplication.instance())  # Pass the QApplication instance to Peruse
            self.peruse_app.show()
        else:
            # Incorrect captcha entered, show an error message
            self.attempts += 1  # Increment the attempts counter
            self.update_attempts_label()  # Update the attempts label

            if self.attempts == MAX_ATTEMPTS:
                # Maximum attempts reached, quit the application
                QMessageBox.critical(self, "Incorrect Captcha", "Maximum attempts reached. Quitting the application.")
                QApplication.quit()
            else:
                if entered_text:
                    # Display error message and regenerate captcha only if there was entered text
                    QMessageBox.critical(self, "Incorrect Captcha", "Incorrect captcha entered. Please try again.")
                    self.captcha_input.clear()
                    self.generate_captcha()

    def update_attempts_label(self):
        remaining_attempts = MAX_ATTEMPTS - self.attempts
        self.attempts_label.setText(f"Attempts Remaining: {remaining_attempts}")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    captcha_window = CaptchaWindow()
    captcha_window.show()

    sys.exit(app.exec())
