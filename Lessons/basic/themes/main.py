from PySide6.QtGui import QPalette, QColor
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
    QComboBox,
)

from PySide6.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        palette = QPalette()
        palette.setColor(QPalette.PlaceholderText, QColor(245, 73, 39))
        palette.setColor(QPalette.WindowText, QColor(245, 73, 39))
        palette.setColor(QPalette.Base, QColor(245, 73, 39))

        self.setPalette(palette)

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


app = QApplication([])
window = MainWindow()
window.show()
app.exec()
