from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QMainWindow, QToolBar, QPushButton, QStatusBar
from PySide6.QtCore import QSize


class MainWindow(QMainWindow):
    def __init__(self, app):

        super().__init__()

        self.app = app
        self.setWindowTitle("Custom MainWindow")

        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("&File")
        quit_action = file_menu.addAction("Exit")
        quit_action.triggered.connect(self.quit_app)

        edit_menu = menu_bar.addMenu("&Edit")
        copy_action = edit_menu.addAction("Copy")
        cut_action = edit_menu.addAction("Cut")
        paste_action = edit_menu.addAction("Paste")
        undo_action = edit_menu.addAction("Undo")
        redo_action = edit_menu.addAction("Redo")

        menu_bar.addMenu("Window")
        menu_bar.addMenu("Setting")
        menu_bar.addMenu("Help")

        toolbar = QToolBar("My main toolbar")
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)

        toolbar.addAction(quit_action)

        action2 = QAction(QIcon("icon.jpg"), "action2", self)
        action2.setStatusTip("Status message for action2")
        action2.triggered.connect(self.toolbar_button_click)
        toolbar.addAction(action2)

        toolbar.addSeparator()
        toolbar.addWidget(QPushButton("Click"))

        self.setStatusBar(QStatusBar(self))

    def quit_app(self):
        self.app.quit()

    def toolbar_button_click(self):
        self.statusBar().showMessage("Message from my app", 3000)
