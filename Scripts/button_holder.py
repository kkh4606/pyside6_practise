from PySide6.QtWidgets import QMainWindow, QPushButton


def button_click():
    print("You click the button")


class ButtonHolder(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Button Holder App")
        button = QPushButton("click me")

        button.setChecked(True)
        button.clicked.connect(button_click)
        self.setCentralWidget(button)
