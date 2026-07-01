import sys

from PySide6 import QtGui
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtUiTools import QUiLoader

import resources

loader = QUiLoader()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.dlg_window = loader.load("test_resource.ui", None)

        self.setWindowTitle("Hello World")
        self.button = QPushButton("My button")

        icon = QtGui.QIcon(":/icons/abacus.png")
        self.button.setIcon(icon)
        self.button.clicked.connect(self.change_icon)

        self.setCentralWidget(self.button)

        self.show()

    def change_icon(self):
        icon = QtGui.QIcon(":/icons/acorn.png")
        self.button.setIcon(icon)

        self.dlg_window.show()


app = QApplication(sys.argv)
w = MainWindow()
app.exec()
