import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QLineEdit,QFo3a


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMouseTracking(True)
        self.input = QLineEdit("Click in this window...")
        self.input.setMouseTracking(True)
        self.setCentralWidget(self.input)

    def mousePressEvent(self, e):
        print("you click mouse")
        if e.button() == Qt.MouseButton.LeftButton:
            # handle the left-button press in here
            self.input.setText("mousePressEvent LEFT")


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
