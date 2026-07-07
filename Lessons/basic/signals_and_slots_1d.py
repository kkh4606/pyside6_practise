import sys

from PySide6.QtWidgets import QMainWindow, QPushButton, QApplication


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.button_is_checked = True

        self.setWindowTitle("My App")

        self.btn = QPushButton("Press Me!")
        self.btn.setCheckable(True)

        self.btn.released.connect(self.the_button_was_released)

        self.btn.setChecked(self.button_is_checked)

        print(self.btn.isChecked())

        self.setCentralWidget(self.btn)

    def the_button_was_released(self):

        self.button_is_checked = self.btn.isChecked()

        print(self.button_is_checked)


app = QApplication(sys.argv)
window = MainWindow()

window.show()

app.exec()
