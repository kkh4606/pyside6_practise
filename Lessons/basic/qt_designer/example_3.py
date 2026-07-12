import os
import sys
from PySide6 import QtCore, QtWidgets
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QMainWindow
from Lessons.basic.qt_designer.MainWindow import Ui_MainWindow

loader = QUiLoader()


# class MainUI(QtCore.QObject):
#     def __init__(self):
#         super().__init__()
#
#         self.ui = loader.load("widget.ui", None)
#
#         self.ui.setWindowTitle("MainWindow Title")
#
#         self.ui.show()
#
#         self.button = self.ui


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__()
        self.setupUi(self)


app = QtWidgets.QApplication(sys.argv)
ui = MainWindow()
app.exec()
