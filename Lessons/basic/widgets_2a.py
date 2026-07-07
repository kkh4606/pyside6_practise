import sys

from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QHBoxLayout, QWidget


from pathlib import Path

base_dir = Path.cwd() / "images" / "photo_2025-10-25_13-49-49.jpg"


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")

        my_label = QLabel("Hello")
        my_label.setPixmap(QPixmap(base_dir))
        my_label.setScaledContents(True)

        self.setCentralWidget(my_label)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
