import sys

from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QMenu
from PySide6.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.show()

        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.on_context_menu)
        # self.setMouseTracking(True)
        # self.label = QLabel("Click in this window")
        # self.setMouseTracking(True)
        # self.setCentralWidget(self.label)

    def on_context_menu(self, pos):
        context = QMenu(self)
        context.addAction(QAction("test 1", self))
        context.addAction(QAction("test 2", self))
        context.addAction(QAction("test 3", self))

        context.exec(self.mapToGlobal(pos))

    # def contextMenuEvent(self, event, /):
    #     context = QMenu(self)
    #     context.addAction(QAction("test 1", self))
    #     context.addAction(QAction("test 2", self))
    #     context.addAction(QAction("test 3", self))
    #
    #     context.exec(event.globalPos())

    # def mousePressEvent(self, e):
    #     if e.button() == Qt.MouseButton.LeftButton:
    #         self.label.setText("mousePressEvent LEFT")
    #     elif e.button() == Qt.MouseButton.RightButton:
    #         self.label.setText("mousePressEvent RIGHT")
    #     elif e.button() == Qt.MouseButton.MiddleButton:
    #         self.label.setText("MousePressEvent MIDDLE")

    # def mouseReleaseEvent(self, e):
    #     if e.button() == Qt.MouseButton.LeftButton:
    #         self.label.setText("mouseReleaseEvent LEFT")
    #     elif e.button() == Qt.MouseButton.MiddleButton:
    #         self.label.setText("mouseReleaseEvent MIDDLE")
    #     elif e.button() == Qt.MouseButton.RightButton:
    #         self.label.setText("mouseReleaseEvent RIGHT")

    def mouseDoubleClickEvent(self, event, /):
        if event.button() == Qt.MouseButton.LeftButton:
            self.label.setText("mouseDoubleClickEvent LEFT")
        if event.button() == Qt.MouseButton.RightButton:
            self.label.setText("mouseDoubleClickEvent RIGHT")
        if event.button() == Qt.MouseButton.MiddleButton:
            self.label.setText("mouseDoubleClickEvent MIDDLE")


app = QApplication(sys.argv)

window = MainWindow()


app.exec()
