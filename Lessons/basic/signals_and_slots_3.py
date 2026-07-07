from PySide6.QtWidgets import QMainWindow, QPushButton, QApplication
from random import choice

window_titles = [
    "My App",
    "My App",
    "Still My App",
    "Still My App",
    "What on earth",
    "What on earth",
    "This is surprising",
    "This is surprising",
    "Something went wrong",
]


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")

        self.btn = QPushButton("Click me")
        self.windowTitleChanged.connect(self.window_title_changed)
        self.btn.clicked.connect(self.btn_clicked)

        self.setCentralWidget(self.btn)

    def btn_clicked(self):

        win_title = choice(window_titles)

        self.setWindowTitle(win_title)

    def window_title_changed(self):

        if self.windowTitle() == "What on earth":
            self.btn.setText("window title changed!")
            self.btn.setEnabled(False)


app = QApplication([])
window = MainWindow()
window.show()
app.exec()
