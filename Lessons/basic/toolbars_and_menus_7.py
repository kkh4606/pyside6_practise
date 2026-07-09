import os
import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QAction, QIcon, QKeySequence
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QStatusBar

base_dir = os.path.dirname(__file__)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        label = QLabel("Hello World!")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        font = label.font()
        font.setPointSize(20)
        label.setFont(font)
        self.setCentralWidget(label)

        menu = self.menuBar()
        file_menu = menu.addMenu("&File")
        btn_action = QAction("Open", self)
        btn_action.setShortcut(QKeySequence("Ctrl+O"))
        btn_action.triggered.connect(self.click_btn)
        btn_action.setStatusTip("This is your btn")
        file_menu.addAction(btn_action)

        btn_action2 = QAction(
            QIcon(os.path.join(base_dir, "icons", "acorn")), "New", self
        )
        btn_action2.setStatusTip("btn2")
        file_submenu = file_menu.addMenu("New")
        file_submenu.addAction(btn_action2)

        file_menu.addSeparator()

        btn_action = QAction("Exit", self)
        file_menu.addAction(btn_action)

        self.setStatusBar(QStatusBar(self))

    def click_btn(self, s):
        print(s)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
