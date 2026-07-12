import os
import sys
from PySide6 import QtWidgets
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QMainWindow

loader = QUiLoader()


def mainwindow_setup(window: QMainWindow):
    window.setWindowTitle("MainWindow Title")


app = QtWidgets.QApplication(sys.argv)

window = loader.load("widget.ui", None)

mainwindow_setup(window)

window.show()

app.exec()
