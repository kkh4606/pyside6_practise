import sys

from PySide6.QtCore import QSize
from PySide6.QtGui import Qt, QAction, QIcon

from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QToolBar, QStatusBar
from pathlib import Path

import os

base_dir = os.path.dirname(__file__)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        label = QLabel("Hello World!")
        current_font = label.font()
        current_font.setPointSize(20)
        label.setFont(current_font)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(label)

        toolbar = QToolBar("main toolbar")
        self.addToolBar(toolbar)

        self.btn_action = QAction(
            QIcon(os.path.join(base_dir, "icons", "acorn.png")), "bnt1", self
        )
        toolbar.setIconSize(QSize(16, 16))

        self.btn_action.setStatusTip("This is your btn action")
        self.btn_action.setCheckable(True)
        self.btn_action.triggered.connect(self.onMyToolbarButtonClick)

        toolbar.addAction(self.btn_action)

        toolbar.addSeparator()

        self.btn_action2 = QAction(
            QIcon(os.path.join(base_dir, "icons", "abacus.png")), "btn2", self
        )

        toolbar.setIconSize(QSize(16, 16))

        self.btn_action2.setStatusTip("This is your btn action 2")
        self.btn_action2.setCheckable(True)
        self.btn_action2.triggered.connect(self.onMyToolbarButtonClick)

        toolbar.addAction(self.btn_action2)

        self.setStatusBar(QStatusBar(self))

    def onMyToolbarButtonClick(self, s):
        print(s)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
