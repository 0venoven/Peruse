import sys
from PySide6.QtWidgets import QApplication
from peruse2 import Peruse

app = QApplication(sys.argv)
w = Peruse(app)

w.show()
app.exec()