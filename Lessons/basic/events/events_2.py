import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QTextEdit,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMouseTracking(False)

        self.label = QLabel("Click in this window")

        self.setCentralWidget(self.label)

    def mouseMoveEvent(self, event, /):
        self.label.setText("MouseMove Event")

    # def mousePressEvent(self, event, /):
    #
    #     if event.button() == Qt.LeftButton:
    #         self.label.setText("MousePressEvent Left")
    #     elif event.button() == Qt.RightButton:
    #         self.label.setText("MousePressEvent Right")
    #     elif event.button() == Qt.MiddleButton:
    #         self.label.setText("MousePressEvent Middle")
    #
    # def mouseReleaseEvent(self, event, /):
    #
    #     if event.button() == Qt.LeftButton:
    #         self.label.setText("MouseReleaseEvent Left")
    #     elif event.button() == Qt.RightButton:
    #         self.label.setText("MouseReleaseEvent Right")
    #     elif event.button() == Qt.MiddleButton:
    #         self.label.setText("MouseReleaseEvent Middle")

    # def mouseDoubleClickEvent(self, event, /):
    #
    #     if event.button() == Qt.LeftButton:
    #         self.label.setText("MouseDoubleClickEvent Left")
    #     elif event.button() == Qt.RightButton:
    #         self.label.setText("MouseDoubleClickEvent Right")
    #     elif event.button() == Qt.MiddleButton:
    #         self.label.setText("MouseDloubleClickEvent Middle")


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
