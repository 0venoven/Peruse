import random
from skimage import data
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QMessageBox
from PySide6.QtGui import QPixmap, QImage

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image Grid Captcha")
        
        self.categories = {
            "astronaut": data.astronaut(),
            "camera": data.camera(),
            "coins": data.coins(),
            # Add more categories and corresponding sample images as needed
        }
        
        self.selected_images = []
        self.expected_category = ""
        
        self.setup_ui()
        self.generate_captcha()
        
    def setup_ui(self):
        central_widget = QWidget()
        layout = QVBoxLayout()
        
        self.expected_label = QLabel()
        layout.addWidget(self.expected_label)
        
        self.image_labels = [QLabel() for _ in range(9)]
        for label in self.image_labels:
            label.setFixedSize(200, 200)  # Adjust the image label size if needed
            label.setScaledContents(True)
            label.mousePressEvent = self.create_label_click_handler(label)
            layout.addWidget(label)
        
        submit_button = QPushButton("Submit")
        submit_button.clicked.connect(self.verify_selection)
        layout.addWidget(submit_button)
        
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        
    def generate_captcha(self):
        self.expected_category = random.choice(list(self.categories.keys()))
        num_categories = len(self.categories)
        num_images = min(num_categories, 9)
        self.selected_images = random.sample(list(self.categories.keys()), num_images)

        
        self.expected_label.setText(f"Select images with {self.expected_category}")
        
        for i in range(len(self.selected_images)):
            category = self.selected_images[i]
            image = self.categories[category]
            
            pixmap = QPixmap.fromImage(self.convert_image_to_qimage(image))
            self.image_labels[i].setPixmap(pixmap)
        
    def verify_selection(self):
        selected_categories = set(self.selected_images)
        
        if len(selected_categories) == 1 and self.expected_category in selected_categories:
            QMessageBox.information(self, "Captcha Verification", "Captcha verification successful!")
            self.generate_captcha()
        else:
            QMessageBox.warning(self, "Captcha Verification", "Captcha verification failed. Try again.")
    
    @staticmethod
    def convert_image_to_qimage(image):
        height, width = image.shape[:2]
        qimage = QImage(image.data, width, height, QImage.Format_RGB888)
        return qimage.rgbSwapped()
    
    def create_label_click_handler(self, label):
        def on_label_click(event):
            selected_index = self.image_labels.index(label)
            selected_category = self.selected_images[selected_index]
            self.selected_images = [selected_category]  # Only keep the selected image
            self.verify_selection()
        
        return on_label_click
        
if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
