from captcha.image import ImageCaptcha
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QPushButton, QWidget
from PySide6.QtGui import QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image Captcha App")
        
        self.image_label = QLabel()
        self.generate_captcha()
        
        generate_button = QPushButton("Reset Captcha")
        generate_button.clicked.connect(self.generate_captcha)
        
        layout = QVBoxLayout()
        layout.addWidget(self.image_label)
        layout.addWidget(generate_button)
        
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        
    def generate_captcha(self):
        image = ImageCaptcha()
        
        # Generate image captcha with text '1234'
        captcha_text = "1234"
        data = image.generate(captcha_text)
        
        # Save the image to a file
        image_path = "captcha.png"
        image.write(captcha_text, image_path)
        
        # Display the captcha image in the app
        pixmap = QPixmap(image_path)
        self.image_label.setPixmap(pixmap)
    
if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
