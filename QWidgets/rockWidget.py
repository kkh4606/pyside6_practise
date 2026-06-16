from PySide6.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout


class RockWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Rock Widget")

        button1 = QPushButton("button1")
        button2 = QPushButton("button2")

        button1.clicked.connect(self.click)
        button_layout = QVBoxLayout()
        button_layout.addWidget(button1)
        button_layout.addWidget(button2)

        self.setLayout(button_layout)

    def click(self):
        print("You click the button")
