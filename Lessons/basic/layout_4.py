import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QVBoxLayout,
    QWidget,
    QHBoxLayout,
)
from Lessons.basic.layout_colorwidget import Color


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")

        layout1 = QHBoxLayout()
        layout1.setSpacing(20)
        layout1.setContentsMargins(0, 0, 0, 0)

        layout2 = QVBoxLayout()

        layout3 = QVBoxLayout()

        layout4 = QVBoxLayout()

        layout2.addWidget(Color("red"))
        layout2.addWidget(Color("yellow"))
        layout2.addWidget(Color("purple"))

        layout3.addWidget(Color("green"))

        layout4.addWidget(Color("red"))
        layout4.addWidget(Color("purple"))

        layout1.addLayout(layout2)
        layout1.addLayout(layout3)
        layout1.addLayout(layout4)

        container = QWidget()
        container.setLayout(layout1)

        self.setCentralWidget(container)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
