from captcha.image import ImageCaptcha
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QPushButton, QWidget, QLineEdit, QMessageBox
from PySide6.QtGui import QPixmap, QKeyEvent
import string
import random
import sys

MAX_ATTEMPTS = 3

class CaptchaWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image Captcha App")

        self.attempts = 0  # Counter for the number of attempts

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

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.captcha_input.returnPressed.connect(self.check_captcha)  # Connect returnPressed signal to check_captcha method

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
        entered_text = self.captcha_input.text()
        
        if entered_text == self.correct_captcha_text:
            # Correct captcha entered, proceed to the main app contents
            self.show_main_app()
        else:
            # Incorrect captcha entered, show an error message
            self.attempts += 1  # Increment the attempts counter
            self.update_attempts_label()  # Update the attempts label
            
            if self.attempts >= MAX_ATTEMPTS:
                # Maximum attempts reached, quit the application
                QMessageBox.critical(self, "Incorrect Captcha", "Maximum attempts reached. Quitting the application.")
                QApplication.quit()
            else:
                # Display error message and regenerate captcha
                QMessageBox.critical(self, "Incorrect Captcha", "Incorrect captcha entered. Please try again.")
                self.captcha_input.clear()
                self.generate_captcha()
    
    def show_main_app(self):
        # Implement the logic to show the main app contents here
        # This can include enabling/disabling certain UI elements or showing/hiding specific widgets
        # You can replace this placeholder function with your own implementation
        QMessageBox.information(self, "Success", "Captcha passed! Showing main app contents.")
        self.close()

    def update_attempts_label(self):
        remaining_attempts = MAX_ATTEMPTS - self.attempts
        self.attempts_label.setText(f"Attempts Remaining: {remaining_attempts}")
    

app = QApplication(sys.argv)
window = CaptchaWindow()
window.show()
sys.exit(app.exec())
