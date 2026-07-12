import os
import sys

from PySide6 import QtWidgets
from PySide6.QtUiTools import QUiLoader

loader = QUiLoader()


app = QtWidgets.QApplication(sys.argv)


window = loader.load("widget.ui", None)


window.show()


app.exec()
