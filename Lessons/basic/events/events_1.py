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

        self.label = QLabel("Click in this window")

        self.setCentralWidget(self.label)

    def mouseMoveEvent(self, event, /):
        self.label.setText("MouseMove Event")

    def mousePressEvent(self, event, /):
        self.label.setText("MousePress Event")
        print(event.globalPos())

    def mouseReleaseEvent(self, event, /):
        self.label.setText("MouseRelease Event")

    def mouseDoubleClickEvent(self, event, /):
        self.label.setText("MouseDoubleClick Event")


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
