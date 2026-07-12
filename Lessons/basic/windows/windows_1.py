import sys
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QLineEdit,
)

from PySide6.QtCore import Qt
from random import randint


class AnotherWindow(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        self.label = QLabel("Hello, World! %d" % randint(0, 100))

        font = self.label.font()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout.addWidget(self.label)

        self.setLayout(layout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.new_window = AnotherWindow()

        self.button = QPushButton("New Window")
        self.button.clicked.connect(self.toggle_window)

        self.input = QLineEdit()
        self.input.textChanged.connect(self.new_window.label.setText)

        layout = QVBoxLayout()

        layout.addWidget(self.input)
        layout.addWidget(self.button)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    def toggle_window(self):
        if self.new_window.isVisible():
            self.new_window.hide()
        else:
            self.new_window.show()


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()
