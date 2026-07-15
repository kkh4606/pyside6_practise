from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QLineEdit,
    QPushButton,
    QComboBox,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
)
from PySide6.QtGui import QPalette, QColor
from PySide6.QtCore import Qt

import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        label = QLabel("Hello, World")
        font = label.font()
        font.setPointSize(20)
        label.setFont(font)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        user_input = QLineEdit()
        user_input.setPlaceholderText("Write something ...")
        commit = QPushButton("Commit")

        c_box = QComboBox()
        c_box.addItems(["apple", "banana", "orange"])

        main_layout = QVBoxLayout()

        v_layout = QHBoxLayout()
        v_layout.addWidget(user_input)
        v_layout.addWidget(commit)

        main_layout.addWidget(label)
        main_layout.addLayout(v_layout)
        main_layout.addWidget(c_box)

        container = QWidget()

        container.setLayout(main_layout)

        self.setCentralWidget(container)


darkPalette = QPalette()
darkPalette.setColor(QPalette.Window, QColor(53, 53, 53))
darkPalette.setColor(QPalette.WindowText, Qt.white)
darkPalette.setColor(QPalette.Disabled, QPalette.WindowText, QColor(127, 127, 127))
darkPalette.setColor(QPalette.Base, QColor(42, 42, 42))
darkPalette.setColor(QPalette.AlternateBase, QColor(66, 66, 66))


app = QApplication(sys.argv)
app.setPalette(darkPalette)
w = MainWindow()  # Replace with your QMainWindow instance.
w.show()
app.exec()
