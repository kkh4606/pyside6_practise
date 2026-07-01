import sys

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QStackedLayout,
    QPushButton,
)
from LayoutWidgets.color_widget import Color


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")

        red = Color("red")
        green = Color("green")
        blue = Color("blue")

        yellow = Color("yellow")
        orange = Color("orange")
        grey = Color("grey")

        red_btn = QPushButton("red")
        red_btn.pressed.connect(self.change_red)

        green_btn = QPushButton("green")
        green_btn.pressed.connect(self.change_green)

        blue_btn = QPushButton("blue")
        blue_btn.pressed.connect(self.change_blue)

        main_layout = QVBoxLayout()

        # horizontal layout
        horizontal_layout = QHBoxLayout()

        # vertical layout
        vertical_layout = QVBoxLayout()

        # stacked layout

        self.stack_layout = QStackedLayout()

        # adding widgets to horizontal
        # horizontal_layout.addWidget(red)
        # horizontal_layout.addWidget(green)
        # horizontal_layout.addWidget(blue)
        horizontal_layout.addWidget(red_btn)
        horizontal_layout.addWidget(green_btn)
        horizontal_layout.addWidget(blue_btn)

        # adding widgets to vertical
        # vertical_layout.addWidget(yellow)
        # vertical_layout.addWidget(orange)
        # vertical_layout.addWidget(grey)

        # adding widgets to stack

        self.stack_layout.addWidget(red)
        self.stack_layout.addWidget(green)
        self.stack_layout.addWidget(blue)

        # adding layouts to main_layout
        main_layout.addLayout(horizontal_layout)
        # main_layout.addLayout(vertical_layout)
        main_layout.addLayout(self.stack_layout)

        # make container widget to store main_layout
        container = QWidget()

        # added main_layout to container widget
        container.setLayout(main_layout)

        # show container widget
        self.setCentralWidget(container)

    def change_red(self):
        self.stack_layout.setCurrentIndex(0)

    def change_green(self):
        self.stack_layout.setCurrentIndex(1)

    def change_blue(self):
        self.stack_layout.setCurrentIndex(2)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
