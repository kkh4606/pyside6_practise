import random
import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow
from Lessons.basic.qt_designer.MainWindow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        font = self.label.font()
        font.setPointSize(20)
        self.label.setFont(font)

        self.my_btn.clicked.connect(self.button_click)

    def button_click(self):
        n = random.randint(0, 10)
        self.label.setText("%d" % n)


app = QApplication(sys.argv)
w = MainWindow()
app.exec()
