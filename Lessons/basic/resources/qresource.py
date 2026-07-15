import sys

from PySide6 import QtGui, QtWidgets

# import resources
from Lessons.basic.resources.MainWindow import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Hello World")
        self.setupUi(self)

        # self.button = QtWidgets.QPushButton("My button")
        #
        # icon = QtGui.QIcon(":/icons/abacus.png")
        # self.button.setIcon(icon)
        #
        # self.setCentralWidget(self.button)

        self.show()


app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
app.exec()
