import sys

from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QMainWindow, QLabel, QApplication, QToolBar
from PySide6.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")

        label = QLabel("Hello!")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        toolbar = QToolBar("main toolbar")

        button_action = QAction(QIcon("abacus.png"), "New", self)
        button_action.setStatusTip("btn action")
        button_action.setCheckable(True)
        toolbar.addAction(button_action)

        toolbar.addSeparator()

        button_action2 = QAction(QIcon("abacus.png"), "Open", self)
        button_action2.setStatusTip("btn action")
        button_action2.setCheckable(True)
        toolbar.addAction(button_action2)

        button_action3 = QAction(QIcon("abacus.png"), "Exit", self)
        button_action3.setStatusTip("btn action")
        button_action3.setCheckable(True)
        toolbar.addAction(button_action3)

        menu = self.menuBar()

        file_menu = menu.addMenu("&File")
        file_menu.addAction(button_action)
        file_menu.addAction(button_action2)
        file_menu.addSeparator()
        file_menu.addAction(button_action3)

        edit_menu = menu.addMenu("&Edit")
        edit_menu.addAction(button_action2)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
