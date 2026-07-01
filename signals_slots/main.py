import sys

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QTextEdit,
    QPushButton,
    QGridLayout,
    QWidget,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.text_box = QTextEdit()

        paste_btn = QPushButton("paste")
        cut_btn = QPushButton("cut")

        paste_btn.clicked.connect(self.text_box.paste)
        cut_btn.clicked.connect(self.text_box.cut)

        layout = QGridLayout()

        layout.addWidget(self.text_box, 0, 0, 3, 3)
        layout.addWidget(cut_btn, 4, 2)
        layout.addWidget(paste_btn, 4, 1)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
