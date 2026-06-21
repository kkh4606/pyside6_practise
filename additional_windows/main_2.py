import sys

from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


from random import randint


class AnotherWindow(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("Another Window % d" % randint(0, 100))
        layout.addWidget(self.label)
        self.setLayout(layout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.w = AnotherWindow()
        self.w2 = AnotherWindow()

        layout = QVBoxLayout()

        self.button = QPushButton("Push for Window")
        self.button.clicked.connect(lambda checked: self.toggle_window(self.w))

        button2 = QPushButton("Push for Window 2")
        button2.clicked.connect(lambda checked: self.toggle_window(self.w2))
        layout.addWidget(self.button)
        layout.addWidget(button2)

        w = QWidget()
        w.setLayout(layout)

        self.setCentralWidget(w)

    def toggle_window(self, checked):
        if self.w.isVisible():
            self.w.hide()
        else:
            self.w.show()


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
