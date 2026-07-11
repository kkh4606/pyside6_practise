import sys

from PySide6.QtWidgets import QMainWindow, QPushButton, QApplication


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        self.btn = QPushButton("Press Me!")
        self.btn.setCheckable(True)

        self.btn.released.connect(self.the_button_was_clicked)

        print(self.btn.isChecked())

        self.setCentralWidget(self.btn)

    def the_button_was_clicked(self):
        self.btn.setText("You already clicked me.")
        self.btn.setEnabled(False)

        self.setWindowTitle("My Oneshot App")


app = QApplication(sys.argv)
window = MainWindow()

window.show()

app.exec()
