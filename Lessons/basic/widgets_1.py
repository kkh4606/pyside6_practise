from PySide6.QtWidgets import (
    QMainWindow,
    QPushButton,
    QApplication,
    QLabel,
    QLineEdit,
    QVBoxLayout,
    QWidget,
)

from PySide6.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")

        my_label = QLabel("Hello")
        font = my_label.font()  # get the current font size

        font.setPointSize(30)  # change font size to 30px
        my_label.setFont(font)  # set font to my_label
        my_label.setAlignment(
            Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter
        )  # align label in the center

        self.setCentralWidget(my_label)


app = QApplication([])
window = MainWindow()
window.show()
app.exec()
