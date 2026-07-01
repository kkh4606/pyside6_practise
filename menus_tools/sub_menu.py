import sys

from PySide6.QtGui import QAction, QIcon, QKeySequence
from PySide6.QtWidgets import QMainWindow, QLabel, QApplication, QToolBar, QMenuBar
from PySide6.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")

        # toolbar = QToolBar("main toolbar")
        # self.addToolBar(toolbar)

        action1 = QAction(QIcon("abacus.png"), "New", self)
        action1.setShortcut(QKeySequence("Ctrl+p"))
        action1.triggered.connect(self.test_action)
        action2 = QAction(QIcon("abacus.png"), "New", self)
        action3 = QAction(QIcon("abacus.png"), "New", self)
        action4 = QAction(QIcon("abacus.png"), "New", self)
        # toolbar.addAction(action1)

        menu = self.menuBar()

        file_menu = menu.addMenu("File")

        # file_menu.addAction(action1)

        sub_menu = file_menu.addMenu("sub")
        sub_menu.addAction(action1)
        sub_menu.addAction(action2)

        sub_sub = sub_menu.addMenu("sub sub")
        sub_sub.addAction(action4)

    def test_action(self):
        print("you use shortcut")


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
